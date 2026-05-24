from pydantic import BaseModel

class PredictionResponse(BaseModel):
    prediction: str
    normal_count: int
    abnormal_count: int
    total: int
    abnormal_pct: str