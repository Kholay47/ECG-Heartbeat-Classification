# 🫀 ECG Classification Web App

This is a machine learning-powered web application that classifies heartbeat (ECG) signals as **Normal** or **Abnormal** using the [PTB-XL ECG dataset](https://www.kaggle.com/datasets/shayanfazeli/heartbeat). The project features:

- A RandomForestClassifier-based model
- A Flask backend for serving predictions

---

## 🚀 Features

✅ Real-time ECG classification  
✅ Clean web interface  
✅ Model trained using stratified sampling  
✅ Prediction summary with counts and percentage

---

## 🧠 Model Details

- **Algorithm**: RandomForestClassifier
- **Input Shape**: 187 features per sample
- **Dataset**: PTB-XL (binary labels - 0: normal, 1: abnormal)
- **Training split**: 80% training, 20% testing
- **Preprocessing**: StandardScaler for feature normalization

---

## 📁 Folder Structure (for reference)

 - your_project/
- ├── app.py
- ├── model.pkl
- ├── scaler.pkl
- ├── templates/
  - └── index.html

## 
### 📝 Install Required Packages

Install all dependencies:
- flask
- pandas
- scikit-learn
- joblib

---

## 📤 How to Use the App

1. **Start the Flask server**  
  Open the app in your browser
Visit: http://127.0.0.1:5000

##

2. **Upload an ECG .csv file**

  - Click Choose File

  - Select a .csv file containing ECG samples

  - Make sure the file contains only 187 columns (no headers or labels)

##

3. **Click "Classify"**

  - The app will preprocess and classify each sample

  - You'll get a result showing:

    - ✅ Overall Prediction: Normal or Abnormal

    - 📊 Count of Normal and Abnormal predictions

    - 📈 Percentage of Abnormal samples

---

## ✅ Example Output

  - Prediction: Abnormal
  - Normal: 3
  - Abnormal: 97
  - Total Samples: 100
  - Abnormal percentage: 97.00%

---

## 📎 Dataset Reference
🔗 https://www.kaggle.com/datasets/shayanfazeli/heartbeat
