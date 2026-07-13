import streamlit as st
from data_loader import load_data
import pandas as pd

df= load_data()

st.title("📈 Sales Overview Dashboard")

df["Year"] = df["Order Date"].dt.year
df["Month"] = df["Order Date"].dt.to_period("M").astype(str)

st.subheader("Total Sales by year")

year_sales = df.groupby("Year")["Sales"].sum()

st.bar_chart(year_sales)

st.subheader("Monthly Sales Trend")

monthly_sales = (
    df.groupby(pd.Grouper(key="Order Date", freq="ME"))["Sales"]
      .sum()
)

st.line_chart(monthly_sales)

st.subheader("Sales by Region and Category")

region = st.selectbox(
    "Select Region",
    sorted(df["Region"].unique())
)

category = st.selectbox(
    "Select Category",
    sorted(df["Category"].unique())
)

filtered_df = df[
    (df["Region"] ==region) &
    (df["Category"] == category)
]

filtered_sales = (filtered_df.groupby(pd.Grouper(key="Order Date", freq="ME"))["Sales"].sum())

st.line_chart(filtered_sales)

st.subheader("filtered_df")
st.dataframe(filtered_df)