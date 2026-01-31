from flask import Flask, render_template, request
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open("loan_model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    features = [
        float(request.form["Gender"]),
        float(request.form["Married"]),
        float(request.form["Dependents"]),
        float(request.form["Education"]),
        float(request.form["Self_Employed"]),
        float(request.form["ApplicantIncome"]),
        float(request.form["CoapplicantIncome"]),
        float(request.form["LoanAmount"]),
        float(request.form["Loan_Amount_Term"]),
        float(request.form["Credit_History"]),
        float(request.form["Property_Area"])
    ]

    features_scaled = scaler.transform([features])
    prediction = model.predict(features_scaled)[0]

    result = "Loan Approved ✅" if prediction == 1 else "Loan Rejected ❌"
    return render_template("index.html", prediction_text=result)

if __name__ == "__main__":
    app.run(debug=True)