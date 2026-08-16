# 🏡 California House Price Predictor

A professional end-to-end Machine Learning web application that predicts California house prices based on housing characteristics using **Ridge Regression** and **Streamlit**.

---

## 🚀 Live Demo

https://california-house-price-predictor-sahil.streamlit.app/

---

## 📌 Project Overview

This project predicts the estimated market value of houses in California using a Machine Learning model trained on the California Housing Dataset.

The project demonstrates the complete Machine Learning workflow:

- Data Cleaning
- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Feature Engineering
- Model Comparison
- Model Evaluation
- Pipeline Creation
- Web App Deployment using Streamlit

---

## ✨ Features

- 🏠 Predict California house prices instantly
- 📊 Interactive Streamlit dashboard
- 🎯 Ridge Regression model
- 📈 Price gauge visualization
- 📋 Property summary
- 📊 Model performance metrics
- 🎨 Modern responsive UI
- ⚡ Real-time predictions

---

## 🛠 Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Pandas | Data Analysis |
| NumPy | Numerical Computing |
| Scikit-Learn | Machine Learning |
| Streamlit | Web Application |
| Plotly | Interactive Charts |
| Joblib | Model Serialization |

---

## 📂 Dataset

**California Housing Dataset**

Features include:

- Longitude
- Latitude
- Housing Median Age
- Total Rooms
- Total Bedrooms
- Population
- Households
- Median Income
- Ocean Proximity

Target Variable:

- Median House Value

---

## 🤖 Machine Learning Pipeline

The project uses a Scikit-Learn Pipeline containing:

- Missing Value Imputation
- One-Hot Encoding
- Standard Scaling
- Ridge Regression

---

## 📊 Model Performance

| Metric | Value |
|---------|-------|
| Algorithm | Ridge Regression |
| RMSE | 70,066 |
| R² Score | 0.6254 |

---

## 📸 Application Screenshots

### Home Page

![Homepage](assets/homepage.png)

---

### Prediction Result

![Prediction](assets/prediction.png)

---

### Dashboard

![Dashboard](assets/dashboard.png)

---

## 📁 Project Structure

```text
LinearRegressionProject/

│── Data/
│ └── housing.csv

│── models/
│ ├── house_price_model.pkl
│ └── house_price_pipeline.pkl

│── assets/
│ ├── homepage.png
│ ├── prediction.png
│ └── dashboard.png

│── notebooks/
│ ├── task1_ml_linear_regression.ipynb
│ └── AI_ML_Task2_Model_Comparison.ipynb

│── app.py
│── train.py
│── requirements.txt
│── README.md
│── .gitignore
```

---

## ⚙️ Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPOSITORY.git
```

Move into the project folder

```bash
cd YOUR_REPOSITORY
```

Create a virtual environment

```bash
python3 -m venv .venv
```

Activate it

### macOS/Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python3 -m streamlit run app.py
```

---

## 📈 Future Improvements

- Deep Learning model comparison
- Interactive California map
- User authentication
- Cloud deployment
- API integration
- Additional visualization dashboards

---

## 👨‍💻 Author

**Sahil Nabi**

GitHub: https://github.com/sahilnabi279

LinkedIn: https://www.linkedin.com/in/sahil-nabi/
