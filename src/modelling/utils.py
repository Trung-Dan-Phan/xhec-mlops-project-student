# This module contains utility functions useful for our training pipeline
import numpy as np
import pickle
from sklearn.metrics import mean_squared_error
import random
from typing import Any
from prefect import flow, task

@task(name="Calculate RMSE")
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

@task(name="Load pickle")
def load_pickle(path: str):
    with open(path, "rb") as f:
        loaded_obj = pickle.load(f)
    return loaded_obj


@task(name="Save pickle")
def save_pickle(path: str, obj: Any):
    with open(path, "wb") as f:
        pickle.dump(obj, f)


@task(retries=3, retry_delay_seconds=60)
def failure():
    print("running")
    if random.randint(1, 10) % 2 == 0:
        raise ValueError("This number is not even")


@flow()
def test_failure():
    failure()


@task(name="Load", tags=["Serialize"])
def task_load_pickle(path: str):
    with open(path, "rb") as f:
        loaded_obj = pickle.load(f)
    return loaded_obj


@task(name="Save", tags=["Serialize"])
def task_save_pickle(path: str, obj: dict):
    with open(path, "wb") as f:
        pickle.dump(obj, f)
