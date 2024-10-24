import os
from typing import Optional

import numpy as np
import pandas as pd
from loguru import logger
from predicting import predict
from prefect import flow
from preprocessing import preprocess_data
from sklearn.calibration import LabelEncoder
from sklearn.ensemble import RandomForestRegressor
from training import train_model
from utils import calculate_rmse, load_pickle, save_pickle

# we save the data on github, and here we directly read from it.
df_path = "https://raw.githubusercontent.com/Trung-Dan-Phan/xhec-mlops-project-student/refs/heads/3/use_prefect/data/abalone.csv"


@flow(name="Train model")
def train_model_workflow(
    df_path: str,
    artifacts_filepath: Optional[str] = None,
) -> dict:
    """Train a model and save it to a file"""
    logger.info("Processing training data...")
    df = pd.read_csv(df_path).head(3000)

    X_train, X_test, y_train, y_test, label_encoder = preprocess_data(df=df)
    logger.info("Training model...")
    model = train_model(X_train, y_train)
    logger.info("Making predictions and evaluating...")
    y_pred = predict(X_test=X_test, model=model)
    rmse = calculate_rmse(y_test, y_pred)

    if artifacts_filepath is not None:
        logger.info(f"Saving artifacts to {artifacts_filepath}...")
        save_pickle(
            os.path.join(artifacts_filepath, "label_encoder.pkl"), label_encoder
        )
        save_pickle(os.path.join(artifacts_filepath, "model.pkl"), model)

    return {"model": model, "rmse": rmse}


@flow(name="Batch predict", retries=1, retry_delay_seconds=30)
def batch_predict_workflow(
    batch_df_path: str,
    model: Optional[RandomForestRegressor] = None,
    label_encoder: Optional[LabelEncoder] = None,
    artifacts_filepath: Optional[str] = None,
) -> np.ndarray:
    """Make predictions on a new dataset"""
    if label_encoder is None:
        label_encoder = load_pickle(
            os.path.join(artifacts_filepath, "label_encoder.pkl")
        )
    if model is None:
        model = load_pickle(os.path.join(artifacts_filepath, "model.pkl"))
    batch_df = pd.read_csv(batch_df_path).tail(1000)
    X = preprocess_data(df=batch_df, label_encoder=label_encoder)
    y_pred = predict(X_test=X, model=model)

    return y_pred


if __name__ == "__main__":
    from config import MODELS_DIRPATH

    train_model_workflow(
        df_path=df_path,
        artifacts_filepath=MODELS_DIRPATH,
    )

    batch_predict_workflow(
        batch_df_path=df_path,
        artifacts_filepath=MODELS_DIRPATH,
    )
