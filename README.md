# 🫀 ECG Heartbeat Classification using 1D CNN

This project focuses on the detection and classification of cardiovascular diseases using ECG heartbeat signals from the [MIT-BIH Arrhythmia Dataset](https://www.kaggle.com/datasets/shayanfazeli/heartbeat). The dataset is provided in CSV format where each row represents one heartbeat as a 1D time-series signal.

---

## 📌 Project Objective

To build a machine learning and deep learning pipeline that classifies ECG signals into five heartbeat categories using:

- **Classical ML methods (Random Forest)**
- **Deep Learning using 1D Convolutional Neural Networks (1D-CNN)**

---

## 🗂️ Dataset

- Source: [Kaggle - ECG Heartbeat Categorization Dataset](https://www.kaggle.com/datasets/shayanfazeli/heartbeat)
- Files used:
  - `mitbih_train.csv`
  - `mitbih_test.csv`
- Each row represents a heartbeat as 187 ECG data points + 1 label.

### 🏷️ Classes:
| Label | Heartbeat Type              |
|-------|------------------------------|
| 0     | Normal                       |
| 1     | Supraventricular Premature  |
| 2     | Premature Ventricular       |
| 3     | Fusion of Ventricular       |
| 4     | Unclassified                |

---

## 🧪 Model Overview

### ✅ 1D Convolutional Neural Network (CNN)

- **Input:** 187-length time-series ECG signal
- **Architecture:**
  - Conv1D layers
  - MaxPooling
  - Dropout
  - Dense output layer with softmax

### ✅ Random Forest

- Used as a traditional machine learning baseline
- Trained on flattened ECG signals

---

## 📉 Results (Example)

| Model         | Accuracy |
|---------------|----------|
| Random Forest | ~91%     |
| 1D CNN        | ~98%     |

---

## ⚙️ Requirements

Install all dependencies
--
- numpy
- pandas
- matplotlib
-  scikit-learn
-  tensorflow
-  keras 

## 🚀 How to Run
- Download dataset from Kaggle

- Place mitbih_train.csv and mitbih_test.csv in the project directory.

- Run the Jupyter notebook

## 📌 Notes
- Large .csv files are not uploaded to GitHub due to size restrictions.

- You can download the dataset from [Kaggle](https://www.kaggle.com/datasets/shayanfazeli/heartbeat).
