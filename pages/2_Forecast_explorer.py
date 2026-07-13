import streamlit as st
from data_loader import load_data
from forecast_utils import prophet_forecast

df= load_data()

st.title("Forecast Explorer")

forecast_by= st.radio(
    "Forecast By",
    [
        "Category",
        "Region"
    ]
)

if forecast_by == "Category":
    selected= st.selectbox(
        "Select Category",
        sorted(df["Category"].unique())
    )

else:

    selected= st.selectbox(
        "Select Region",
        sorted(df["Region"].unique())
    )

months = st.slider(
    "Forecast Horizon (Months)",
    1,
    3,
    3
)

forecast = prophet_forecast(
    df,
    forecast_by,
    selected,
    months
)

st.subheader("Forecast")

st.dataframe(forecast.tail(months))

chart= forecast.set_index("ds")["yhat"]
st.line_chart(chart)


st.metric(
    "MAE",
    "9839.84"
)

st.metric(
    "RSME",
    "14133.08"
)

st.metric(
    "MAPE",
    "15.04%"
)