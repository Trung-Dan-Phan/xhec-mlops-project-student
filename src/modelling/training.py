# This module trains a Regression model
from sklearn.ensemble import RandomForestRegressor
from prefect import task

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
