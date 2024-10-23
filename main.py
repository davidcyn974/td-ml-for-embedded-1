from typing import Union

from fastapi import FastAPI
import joblib
app = FastAPI()


model = joblib.load("regression.joblib")

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/test")
def prediction_du_model():
    return {"Hello": "Vincente"}

@app.post("/prediction")
def prediction_du_model(size: float, nb_rooms: int, garden: int):
    input_data = [[size, nb_rooms, garden]]  # Combine inputs into a 2D list (one row of features)
    y_pred = model.predict(input_data)  # Pass the 2D list to the model
    return {"prediction": y_pred.tolist()}  # Convert prediction to list for JSON response




if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

