import streamlit as st
from data_loader import load_data
from anomaly_utility import plot_anomalies,detect_anomalies

df= load_data()

st.title("Anomaly Report")

weekly_sales, anomalies = detect_anomalies(df)

fig= plot_anomalies(
    weekly_sales,
    anomalies
)
st.pyplot(fig)



st.subheader("Detected Anomalies")
st.dataframe(
    anomalies[
        ["Order Date","Sales"]
    ]
)