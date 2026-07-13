# 📊 Sales Forecasting & Demand Analytics Dashboard

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Dashboard-red)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-green)
![Time Series](https://img.shields.io/badge/Time-Series-orange)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A complete **Machine Learning & Time Series Forecasting** project built using **Python**, **Streamlit**, **Facebook Prophet**, **SARIMA**, **XGBoost**, **Isolation Forest**, and **K-Means Clustering**.

The application analyzes historical sales data, forecasts future sales, detects anomalies, segments product demand, and provides an interactive dashboard for business decision-making.

---

# 🎯 Project Objectives

- Analyze historical sales performance.
- Forecast future sales using multiple forecasting techniques.
- Compare forecasting models using evaluation metrics.
- Detect unusual sales patterns (anomalies).
- Segment products into demand groups.
- Build an interactive business dashboard.

---

# 🚀 Live Demo

**Streamlit App**

[https://salesforecastdashboard.streamlit.app](https://end-to-end-sales-forecasting-intelligent-demand-5gzlcqfvw4f5nw.streamlit.app/)

---

# 📂 Project Structure

```text
Sales_Forecasting_Dashboard/
│
├── app.py
├── data_loader.py
├── forecast_utils.py
├── anomaly_utils.py
├── cluster_utils.py
├── requirements.txt
├── README.md
├── .gitignore
├── Superstore.csv
│
├── pages/
│   ├── 1_Sales_Overview.py
│   ├── 2_Forecast_Explorer.py
│   ├── 3_Anomaly_Report.py
│   └── 4_Product_Demand_Segments.py
│
└── assets/
    ├── overview.png
    ├── forecast.png
    ├── anomaly.png
    └── clustering.png
```

---

# 📊 Dataset

Dataset Used:

**Sample Superstore Dataset**

Important Features

- Order Date
- Sales
- Category
- Sub-Category
- Region
- Quantity
- Profit
- Discount

---

# 🛠 Tech Stack

## Programming

- Python

## Dashboard

- Streamlit

## Data Analysis

- Pandas
- NumPy

## Visualization

- Matplotlib

## Machine Learning

- Scikit-Learn
- XGBoost
- Isolation Forest
- PCA
- K-Means

## Time Series Forecasting

- Facebook Prophet
- Statsmodels (SARIMA)

---

# 📈 Dashboard Features

## 📌 Page 1 — Sales Overview

- Total Sales by Year
- Monthly Sales Trend
- Interactive Region Filter
- Interactive Category Filter

---

## 📌 Page 2 — Forecast Explorer

Forecast future sales using **Facebook Prophet**.

Features

- Forecast by Category
- Forecast by Region
- Forecast Horizon (1–3 Months)
- Forecast Visualization
- MAE
- RMSE

---

## 📌 Page 3 — Anomaly Report

Detect unusual sales patterns using

- Isolation Forest
- Rolling Z-Score

Displays

- Weekly Sales
- Detected Anomalies
- Sales Values
- Anomaly Dates

---

## 📌 Page 4 — Product Demand Segments

Demand segmentation using

- K-Means Clustering
- PCA

Displays

- Cluster Visualization
- Product Groups
- Stocking Strategy

---

# 🤖 Machine Learning Models

## Model 1 — SARIMA

Purpose

Statistical Time Series Forecasting

Forecast Horizon

3 Months

Metrics

- MAE
- RMSE
- MAPE

---

## Model 2 — Facebook Prophet

Purpose

Business Forecasting

Features

- Trend
- Seasonality
- Confidence Interval

Forecast Horizon

3 Months

Metrics

- MAE
- RMSE
- MAPE

Selected as the **Best Forecasting Model**.

---

## Model 3 — XGBoost

Features Used

- Lag 1
- Lag 2
- Lag 3
- Rolling Mean
- Month
- Quarter
- Season

Forecast Horizon

3 Months

Metrics

- MAE
- RMSE
- MAPE

---

# 📊 Model Comparison

| Model | MAE | RMSE | MAPE |
|------|------:|------:|------:|
| SARIMA | 14399.08 | 19332.21 | 28.42 |
| Facebook Prophet | **9839.84** | **14133.08** | **15.67** |
| XGBoost | 23672.75 | 28366.20 | 51.06 |

### Best Model

Facebook Prophet achieved the lowest forecasting error and was selected for deployment in the Streamlit dashboard.

---

# 🚨 Anomaly Detection

Algorithms Used

- Isolation Forest
- Rolling Z-Score

Purpose

Identify unusually high or low weekly sales that may indicate promotions, seasonal demand, or unexpected business events.

---

# 📦 Product Demand Segmentation

Algorithm

K-Means Clustering

Features Used

- Sales Volume
- Growth Rate
- Sales Volatility
- Average Order Value

Optimal Clusters

**K = 4**

Demand Groups

- High Volume, Stable Demand
- High Value, High Volatility
- Growing Demand
- Low Volume, Stable Demand

---

# 📌 Business Insights

- Facebook Prophet provided the most accurate sales forecasts.
- Technology and Furniture categories showed stronger future growth.
- Isolation Forest successfully identified unusual weekly sales spikes.
- K-Means segmented products into actionable demand groups for inventory planning.
- High-demand products should be stocked aggressively, while volatile products require careful monitoring.

---

# ⚙ Installation
```

Move into project

```bash
cd Sales_Forecasting_Dashboard
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run application

```bash
streamlit run app.py
```

---

# 📋 Requirements

```text
streamlit
pandas
numpy
matplotlib
scikit-learn
statsmodels
prophet
xgboost
```

---

# 🔮 Future Improvements

- LSTM-based Deep Learning Forecasting
- Hyperparameter Optimization
- AutoML Model Selection
- Inventory Optimization
- Demand Forecasting by Customer
- Real-time Dashboard Updates
- Database Integration
- Cloud Deployment

---

# 👨‍💻 Author

**Pavan Kumar Verma**

B.Tech CSE (Artificial Intelligence & Data Science)

AKS University
