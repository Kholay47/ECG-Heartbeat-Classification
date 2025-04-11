from flask import Flask, render_template, request, jsonify
import pandas as pd
import joblib

app = Flask(__name__)

# Load trained model and scaler
model = joblib.load("ecg_model.pkl")
scaler = joblib.load("scaler.pkl")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'file' not in request.files:
            print("No file part in the request")
            return jsonify({'error': 'No file part'})

        file = request.files['file']
        print(f"Received file: {file.filename}")

        # Read uploaded CSV
        df = pd.read_csv(file)
        print(f"Initial shape: {df.shape}")

        # Drop label column if present
        if df.shape[1] == 188:
            df = df.iloc[:, :-1]
            print("Dropped label column. New shape:", df.shape)

        # Validate shape
        if df.shape[1] != 187:
            return jsonify({'error': 'Uploaded file must have exactly 187 features'})

        # Transform and predict
        X = scaler.transform(df)
        preds = model.predict(X)

        # Count predictions
        normal_count = (preds == 0).sum()
        abnormal_count = (preds == 1).sum()
        total = len(preds)
        abnormal_pct = (abnormal_count / total) * 100

        final_result = "Abnormal" if abnormal_pct >= 50 else "Normal"

        print(f"Predictions - Normal: {normal_count}, Abnormal: {abnormal_count}, Final: {final_result}")

        return jsonify({
            'prediction': final_result,
            'normal_count': int(normal_count),
            'abnormal_count': int(abnormal_count),
            'total': int(total),
            'abnormal_pct': f"{abnormal_pct:.2f}%"
        })

    except Exception as e:
        print(f"Error: {str(e)}")
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
