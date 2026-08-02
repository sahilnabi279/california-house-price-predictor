# 🏠 California Housing Price Prediction using Linear Regression

## 📌 Project Overview

This project predicts California housing prices using the Linear Regression algorithm from Scikit-learn.

The project demonstrates the complete Machine Learning workflow, including:

- Data Loading
- Exploratory Data Analysis (EDA)
- Data Cleaning
- Missing Value Handling
- One-Hot Encoding
- Feature Selection
- Train-Test Split
- Linear Regression Model Training
- Model Evaluation
- Model Saving

---

## 📂 Dataset

California Housing Dataset (Kaggle)

Rows: **20,640**

Features:

- Longitude
- Latitude
- Housing Median Age
- Total Rooms
- Total Bedrooms
- Population
- Households
- Median Income
- Ocean Proximity

Target:

- Median House Value

---

## 📊 Model Performance

| Metric | Value |
|---------|---------|
| MAE | 50,670.74 |
| RMSE | 70,060.52 |
| R² Score | 0.6254 |

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Jupyter Notebook

---

## 📈 Workflow

1. Load Dataset
2. Perform EDA
3. Handle Missing Values
4. Encode Categorical Features
5. Split Data
6. Train Linear Regression Model
7. Evaluate Performance
8. Save Trained Model

---

## 🚀 Future Improvements

- Random Forest Regressor
- XGBoost
- Hyperparameter Tuning
- Streamlit Deployment

## Task 2 – Regression Model Comparison

### Models Implemented
- Linear Regression
- Ridge Regression
- Decision Tree Regressor

### Evaluation Metrics
- RMSE
- R² Score

### Results

| Model | RMSE | R² Score |
|--------|------:|---------:|
| Linear Regression | 70060.52 | 0.625424 |
| Ridge Regression | 70057.42 | 0.625457 |
| Decision Tree | 71510.90 | 0.609755 |

**Best Model:** Ridge Regression