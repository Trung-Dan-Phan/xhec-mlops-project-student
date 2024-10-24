import numpy as np
import scipy.sparse
from prefect import task
from sklearn.metrics import mean_squared_error
from sklearn.ensemble import RandomForestRegressor

@task(name="Train model")
def train_model(X_train, y_train):
    """
    Train a Random Forest Regressor model on the training data.

    Args:
        X_train (pd.DataFrame): The input features for training.
        y_train (pd.Series): The target values for training.

    Returns:
        RandomForestRegressor: The trained Random Forest model.
    """
    # Initialize the model
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

    # Train the model
    rf_model.fit(X_train, y_train)

    return rf_model

@task(name="Make predictions")
def predict(model, X_test):
    """
    Make predictions using the trained model on the test data.

    Args:
        model (RandomForestRegressor): The trained model to use for predictions.
        X_test (pd.DataFrame): The input features for testing.

    Returns:
        np.ndarray: The predicted target values.
    """
    return model.predict(X_test)


@task(name="Evaluate model")
def evaluate_model(y_true: np.ndarray, y_pred: np.ndarray) -> float:
    """Calculate mean squared error for two arrays"""
    return np.sqrt(mean_squared_error(y_true, y_pred))
