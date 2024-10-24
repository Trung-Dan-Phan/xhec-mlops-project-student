# predicting.py
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
