import numpy as np
from src.web_service.utils import load_object

# Load the model and label encoder
model = load_object("src/web_service/local_objects/random_forest_model.pkl")
label_encoder = load_object("src/web_service/local_objects/label_encoder.pkl")

def make_prediction(input_data):
    """
    Preprocesses the input data, makes a prediction using the loaded model, and returns the result.

    Args:
        input_data (dict): A dictionary containing the input features for prediction.

    Returns:
        float: The predicted number of rings.
    """
    # Encode the 'sex' feature using the label encoder
    encoded_sex = label_encoder.transform([input_data['sex']])[0]

    # Prepare the input features array for the model
    input_features = np.array([[
        encoded_sex,
        input_data['length'],
        input_data['diameter'],
        input_data['height'],
        input_data['whole_weight'],
        input_data['shucked_weight'],
        input_data['viscera_weight'],
        input_data['shell_weight']
    ]])

    # Make prediction using the loaded model
    prediction = model.predict(input_features)

    return float(prediction[0])  # Return the prediction as a float
