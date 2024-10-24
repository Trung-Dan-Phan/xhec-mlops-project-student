from fastapi import FastAPI

from src.web_service.lib.inference import make_prediction  # Inference logic
from src.web_service.lib.models import (PredictionRequest,  # Pydantic models
                                        PredictionResponse)
from src.web_service.utils import load_object  # Import the utility function

app = FastAPI(
    title="Prediction API",
    description="API for predicting the number of rings based on abalone features",
)


@app.on_event("startup")
def load_model_and_encoder():
    global model, label_encoder
    model = load_object("src/web_service/local_objects/random_forest_model.pkl")
    label_encoder = load_object("src/web_service/local_objects/label_encoder.pkl")


@app.get("/")
def home() -> dict:
    return {"health_check": "App up and running!"}


@app.post("/predict", response_model=PredictionResponse, status_code=201)
def predict(payload: PredictionRequest) -> PredictionResponse:
    # Pydantic model
    input_data = payload.dict()

    # inference function
    prediction = make_prediction(input_data)

    return PredictionResponse(prediction=prediction)
