import streamlit as st
from data_loader import load_data
from cluster_utils import create_clusters,plot_clusters
df = load_data()

st.title("Product Demand Segments")

cluster_df, pca_df= create_clusters(df)

fig = plot_clusters(pca_df)
st.pyplot(fig)

st.subheader("Demand Cluster Table")
st.dataframe(
    cluster_df.reset_index()
)

cluster_names = {
    0: "High value, High volatility",
    1: "Low Volume, Stable Demand",
    2: "High_Volume, Stable Demand",
    3: "Growing Demand"
}
cluster_df["Cluster Name"] = cluster_df["Cluster"].map(cluster_names)

st.dataframe(
    cluster_df.reset_index()[["Sub-Category","Cluster Name"]]
)