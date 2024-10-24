import os
from typing import Optional
import pandas as pd
import numpy as np
from sklearn.calibration import LabelEncoder
from utils import load_pickle, save_pickle, calculate_rmse
from loguru import logger
from training import train_model
from predicting import predict
from prefect import flow
from preprocessing import preprocess_data
from sklearn.feature_extraction import DictVectorizer
from sklearn.ensemble import RandomForestRegressor


@flow(name="Train model")
def train_model_workflow(
    df: pd.DataFrame,
    artifacts_filepath: Optional[str] = None,
) -> dict:
    """Train a model and save it to a file"""
    logger.info("Processing training data...")
    X_train, X_test, y_train, y_test, label_encoder = preprocess_data(df=df)
    logger.info("Training model...")
    model = train_model(X_train, y_train)
    logger.info("Making predictions and evaluating...")
    y_pred = predict(X_test, model)
    rmse = calculate_rmse(y_test, y_pred)

    if artifacts_filepath is not None:
        logger.info(f"Saving artifacts to {artifacts_filepath}...")
        save_pickle(os.path.join(artifacts_filepath, "label_encoder.pkl"), label_encoder)
        save_pickle(os.path.join(artifacts_filepath, "model.pkl"), model)

    return {"model": model, "rmse": rmse}


@flow(name="Batch predict", retries=1, retry_delay_seconds=30)
def batch_predict_workflow(
    batch_df: pd.DataFrame, labelsaFrame,
    model: Optional[RandomForestRegressor] = None,
    label_encoder: Optional[LabelEncoder] = None,
    artifacts_filepath: Optional[str] = None,
) -> np.ndarray:
    """Make predictions on a new dataset"""
    if label_encoder is None:
        label_encoder = load_pickle(os.path.join(artifacts_filepath, "label_encoder.pkl"))
    if model is None:
        model = load_pickle(os.path.join(artifacts_filepath, "model.pkl"))

    X = preprocess_data(df=batch_df, label_encoder=label_encoder)
    y_pred = predict(X, model)

    return y_pred


if __name__ == "__main__":
    from config import DATA_DIRPATH, MODELS_DIRPATH

    train_model_workflow(
        df=pd.read_csv(os.path.join(DATA_DIRPATH, "abalone.csv")).head(3000),
        artifacts_filepath=MODELS_DIRPATH,
    )

    batch_predict_workflow(
        df=pd.read_csv(os.path.join(DATA_DIRPATH, "abalone.csv")).tail(1000),
        artifacts_filepath=MODELS_DIRPATH,
    )
