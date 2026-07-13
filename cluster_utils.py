import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

def create_clusters(df):
    sales_volume = df.groupby("Sub-Category")["Sales"].sum()

    avg_order = df.groupby("Sub-Category")["Sales"].mean()

    monthly = (
        df.groupby([
            "Sub-Category",
            pd.Grouper(key="Order Date", freq="ME")
        ])["Sales"].sum().reset_index()
    )

    volatility = monthly.groupby("Sub-Category")["Sales"].std()

    yearly = (df.groupby([
        "Sub-Category",
        df["Order Date"].dt.year
    ])["Sales"].sum().reset_index()
    )

    yearly["Growth"] = yearly.groupby(
        "Sub-Category"
    )["Sales"].pct_change()

    growth = yearly.groupby(
        "Sub-Category"
    )["Growth"].mean()

    cluster_df = pd.DataFrame({
        "Sales Volume": sales_volume,
        "Growth Rate": growth,
        "Votality":volatility,
        "Average Order": avg_order
    })


    cluster_df.fillna(cluster_df.mean(numeric_only=True),inplace=True)

    scaler = StandardScaler()
    scaled = scaler.fit_transform(cluster_df)

    Kmeans = KMeans(n_clusters=4,random_state=42)
    cluster_df["Cluster"] = Kmeans.fit_predict(scaled)
    pca = PCA(n_components=2)
    point= pca.fit_transform(scaled)

#PCA dataframe makes

    pca_df = pd.DataFrame(
        point,
        columns=["PC1","PC2"]
    )

    pca_df["Cluster"] = cluster_df["Cluster"].values

    pca_df["Sub-Category"] = cluster_df.index
    return cluster_df, pca_df

#Plot functions now

def plot_clusters(pca_df):

    fig, ax = plt.subplots(figsize=(10,6))

    for cluster in sorted(pca_df["Cluster"].unique()):

        temp = pca_df[
            pca_df["Cluster"] == cluster
        ]

        ax.scatter(
            temp["PC1"],
            temp["PC2"],
            s=120,
            label=f"Cluster {cluster}"
        )

        for _, row in temp.iterrows():

            ax.text(

                row["PC1"],

                row["PC2"],

                row["Sub-Category"],

                fontsize=8

            )

    ax.set_title("Demand Segments")

    ax.legend()

    return fig


