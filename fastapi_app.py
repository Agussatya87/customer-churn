from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
import pandas as pd
import pickle

# Load model, encoders, and scaler
with open('best_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)
with open('encoder.pkl', 'rb') as encoders_file:
    encoders = pickle.load(encoders_file)
with open('scaler.pkl', 'rb') as scaler_file:
    scaler_data = pickle.load(scaler_file)

app = FastAPI()
templates = Jinja2Templates(directory="templates")
# Add GET endpoint for root URL to serve index.html
@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

def make_prediction(input_data):
    input_df = pd.DataFrame([input_data])

    # Apply encoder ke kolom kategorikal
    for col, encoder in encoders.items():
        if col in input_df.columns:
            input_df[col] = encoder.transform(input_df[col])

    # Gunakan kolom yang dipakai saat scaler fit
    numerical_cols = scaler_data.feature_names_in_
    input_df[numerical_cols] = scaler_data.transform(input_df[numerical_cols])

    # Prediksi
    prediction = loaded_model.predict(input_df)[0]
    probability = loaded_model.predict_proba(input_df)[0, 1]

    return ("Churn" if prediction == 1 else "No Churn"), probability

# Pydantic schema sesuai dataset kamu
class PredictionRequest(BaseModel):
    Age: int
    Gender: str
    Tenure: int
    MonthlyCharges: float
    ContractType: str
    InternetService: str
    TotalCharges: float
    TechSupport: str

@app.post("/predict")
async def predict(data: PredictionRequest):
    input_data = data.dict()
    prediction, probability = make_prediction(input_data)
    return {"prediction": prediction, "probability": probability}
