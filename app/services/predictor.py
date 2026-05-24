import joblib 
import pandas as pd

from app.core.config import MODEL_PATH, SCALER_PATH
from app.core.logging import logger
from app.utils.preprocessing import validate_ecg_dataframe

class ECGPredictor:
    def __init__(self):
        logger.info("Loading ECG model and scaler...")

        self.model = joblib.load(MODEL_PATH)
        self.scaler = joblib.load(SCALER_PATH)

        logger.info("Model loaded successfully.")
    
    def predict(self, df: pd.DataFrame):
        df = validate_ecg_dataframe(df)

        X = self.scaler.transform(df)

        preds = self.model.predict(X)

        normal_count = int((preds == 0).sum())
        abnormal_count = int((preds == 1).sum())

        total = len(preds)

        abnormal_pct = (abnormal_count / total) * 100

        final_result = (
            "Abnormal" if abnormal_pct >= 50 else "Normal"
        )

        return {
            "prediction": final_result,
            "normal_count": normal_count,
            "abnormal_count": abnormal_count,
            "total": total,
            "abnormal_pct": f"{abnormal_pct:.2f}%"
        }

predictor = ECGPredictor()