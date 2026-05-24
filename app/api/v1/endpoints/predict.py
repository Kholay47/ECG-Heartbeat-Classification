from fastapi import APIRouter, UploadFile, File, HTTPException
import pandas as pd

from app.services.predictor import predictor
from app.schemas.prediction import PredictionResponse

router = APIRouter()

@router.post(
    "/predict",
    response_model=PredictionResponse
)
async def predict_ecg(
    file: UploadFile = File(...)
):

    try:

        df = pd.read_csv(file.file)

        result = predictor.predict(df)

        return result

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )