from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.v1.endpoints.predict import router as predict_router

app = FastAPI(
    title="ECG Heartbeat Classification API",
    version="1.0.0"
)

app.include_router(
    predict_router,
    prefix="/api/v1",
    tags=["Prediction"]
)

@app.get("/")
def root():
    return {
        "message": "ECG Classification API Running"
    }

@app.get("/health")
def health():
    return {
        "status": "healthy"
    }