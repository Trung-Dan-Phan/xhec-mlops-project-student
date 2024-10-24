# Pydantic models for the web service
from pydantic import BaseModel

# Request model for prediction
class PredictionRequest(BaseModel):
    sex: str
    length: float
    diameter: float
    height: float
    whole_weight: float
    shucked_weight: float
    viscera_weight: float
    shell_weight: float

# Response model for prediction
class PredictionResponse(BaseModel):
    prediction: float
