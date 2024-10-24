import pickle
import os

def load_object(file_path):
    """
    Load a pickle object from a file.

    Parameters:
        file_path (str): The path to the pickle file.

    Returns:
        object: The deserialized object from the pickle file.

    Raises:
        FileNotFoundError: If the file does not exist.
        pickle.UnpicklingError: If the file is not a valid pickle file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'rb') as file:
        try:
            return pickle.load(file)
        except pickle.UnpicklingError as e:
            raise pickle.UnpicklingError(f"Could not unpickle the file {file_path}: {e}")