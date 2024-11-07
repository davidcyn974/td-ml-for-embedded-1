# main.py
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import numpy as np
import joblib
from eurybia import SmartDrift

# Load model and baseline data for drift detection
model = joblib.load("model.pkl")
baseline_data = pd.read_csv("baseline_data.csv")
stored_predictions = []

# Initialize Eurybia SmartDrift object
sd = SmartDrift(
    df_current=None, # to be set when drift is checked
    df_baseline=baseline_data,
    dataset_names={"df_current": "Production Data", "df_baseline": "Training Data"}
)

# FastAPI app
app = FastAPI()

class HouseData(BaseModel):
    size: float
    nb_rooms: int
    garden: int
    orientation: str

def preprocess_input(data):
    orientation_map = {"Nord": 0, "Sud": 1, "Est": 2, "Ouest": 3}
    data["orientation"] = orientation_map.get(data["orientation"], -1)
    return pd.DataFrame([data])

@app.post("/predict")
def predict(data: HouseData):
    input_data = preprocess_input(data.dict())
    
    if -1 in input_data["orientation"].values:
        raise HTTPException(status_code=400, detail="Invalid orientation value")

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Store prediction input data
    stored_predictions.append(input_data)

    return {"prediction": prediction}

@app.get("/detect-drift")
def detect_drift():
    if not stored_predictions:
        raise HTTPException(status_code=400, detail="No production data available for drift detection")

    # Combine stored data for drift detection
    df_current = pd.concat(stored_predictions, ignore_index=True)

    # Update SmartDrift object with production data
    sd.df_current = df_current
    sd.compile(full_validation=True)

    drift_report = sd.generate_report(title_story="Drift Detection Report")
    drift_detected = sd.datadrift_metric > 0.6

    return {
        "drift_detected": drift_detected,
        "drift_report": "Drift report generated as drift_detection_report.html",
    }
