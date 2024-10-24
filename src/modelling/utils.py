# This module contains utility functions useful for our training pipeline
import numpy as np
import pickle
from sklearn.metrics import mean_squared_error

def calculate_rmse(y_test, y_pred):
    """
    Calculate the Root Mean Squared Error (RMSE) between the actual and predicted values.

    Args:
        y_test (array-like): Actual target values.
        y_pred (array-like): Predicted target values.

    Returns:
        float: The calculated RMSE value.
    """
    rmse = np.sqrt(mean_squared_error(y_test, y_pred))
    return rmse

def pickle_object(obj, filename):
    """
    Serialize an object to a file using pickle.

    Args:
        obj: The object to serialize (e.g., model or encoder).
        filename (str): The file path where the object will be saved.

    Returns:
        None
    """
    with open(filename, 'wb') as file:
        pickle.dump(obj, file)
