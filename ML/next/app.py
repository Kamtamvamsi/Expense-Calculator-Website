from flask import Flask, request, jsonify, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the models
try:
    with open('rf_model.pkl', 'rb') as f:
        rf_model = pickle.load(f)
    with open('lr_model.pkl', 'rb') as f:
        lr_model = pickle.load(f)
except FileNotFoundError:
    print("Model files not found. Please ensure 'rf_model.pkl' and 'lr_model.pkl' exist.")
    exit()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        income = float(request.form['income'])
        expenses = float(request.form['expenses'])
    except ValueError:
        return render_template('index.html', error="Please enter valid numeric values for income and expenses.")

    data = np.array([[income, expenses]])
    rf_prediction = rf_model.predict(data)[0]
    lr_prediction = lr_model.predict(data)[0]

    suggestions = []
    if rf_prediction == 1:
        suggestions.append("Your expenses are high. Try to cut down unnecessary expenses.")
    else:
        suggestions.append("Your expenses are under control.")

    return render_template('index.html', rf_result=rf_prediction, lr_result=lr_prediction, suggestions=suggestions)

if __name__ == '__main__':
    app.run(debug=True)

