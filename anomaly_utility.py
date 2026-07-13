import pandas as pd
from sklearn.ensemble import IsolationForest
import matplotlib.pyplot as plt

def detect_anomalies(df):

    weekly_sales = (
        df.groupby(pd.Grouper(key="Order Date", freq="W"))["Sales"]
          .sum()
          .reset_index()
    )

    model= IsolationForest(contamination=0.05,random_state=42)

    weekly_sales["Anomaly"] = model.fit_predict(weekly_sales[["Sales"]])

    anomalies = weekly_sales[weekly_sales["Anomaly"]== -1]

    return weekly_sales, anomalies


def plot_anomalies(weekly_sales, anomalies):
    fig, ax = plt.subplots(figsize=(12,5))

    ax.plot(
        weekly_sales["Order Date"],
        weekly_sales["Sales"],
        label= "weekly sales"
    )

    ax.scatter(
        anomalies["Order Date"],
        anomalies["Sales"],
        color='red',
        s=100,
        label="Anomaly"
    )
    ax.set_title("Weekly Sales Anomalies")
    ax.legend()
    return fig
