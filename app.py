from flask import Flask, render_template, request
import pandas as pd
import pickle

# Load model, encoders, and scaler
with open('best_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)
with open('encoder.pkl', 'rb') as encoders_file:
    encoders = pickle.load(encoders_file)
with open('scaler.pkl', 'rb') as scaler_file:
    scaler_data = pickle.load(scaler_file)

app = Flask(__name__)

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

@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None
    probability = None
    if request.method == 'POST':
        input_data = {
            'Age': int(request.form['Age']),
            'Gender': request.form['Gender'],
            'Tenure': int(request.form['Tenure']),
            'MonthlyCharges': float(request.form['MonthlyCharges']),
            'ContractType': request.form['ContractType'],
            'InternetService': request.form['InternetService'],
            'TotalCharges': float(request.form['TotalCharges']),
            'TechSupport': request.form['TechSupport']
        }

        prediction, probability = make_prediction(input_data)

    return render_template('index.html', prediction=prediction, probability=probability)

if __name__ == '__main__':
    app.run(debug=True)