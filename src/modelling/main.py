# This module is the training flow: it reads the data, preprocesses it, trains a model and saves it.

import argparse
import pandas as pd
from pathlib import Path
from preprocessing import preprocess_data
from training import train_model
from utils import calculate_rmse, pickle_object

def main(trainset_path: Path) -> None:
    """Train a model using the data at the given path and save the model (pickle).

    Args:
        trainset_path (Path): The path to the training dataset.
    """
    # Read data
    df = pd.read_csv(trainset_path)

    # Preprocess data
    X_train, X_test, y_train, y_test, label_encoder = preprocess_data(df)

    # (Optional) Pickle encoder
    encoder_path = Path("src/web_service/local_objects/label_encoder.pkl")
    pickle_object(label_encoder, encoder_path)

    # Train model
    model = train_model(X_train, y_train)

    # Pickle model
    model_path = Path("src/web_service/local_objects/random_forest_model.pkl")
    pickle_object(model, model_path)

    # Optional: Make predictions on the test set and calculate RMSE
    y_pred = model.predict(X_test)
    rmse = calculate_rmse(y_test, y_pred)
    print(f"RMSE: {rmse}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train a model using the data at the given path.")
    parser.add_argument("trainset_path", type=str, help="Path to the training set")
    args = parser.parse_args()
    main(Path(args.trainset_path))

