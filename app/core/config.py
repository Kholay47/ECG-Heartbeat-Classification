from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

MODEL_PATH = BASE_DIR / "app/models/ecg_model.pkl"
SCALER_PATH = BASE_DIR / "app/models/scaler.pkl"