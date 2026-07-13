import pandas as pd
from prophet import Prophet

def prophet_forecast(df, forecast_by, selected_value, months):
    if forecast_by == "Category":
        temp= df[df["Category"]==selected_value]
    
    else:
        temp= df[df["Region"]==selected_value]

    monthly= temp.groupby(pd.Grouper(key="Order Date",freq='ME'))["Sales"].sum().reset_index()

    prophet_df = monthly.rename(
        columns={"Order Date":"ds",
                 "Sales":"y"
        }
    )

    model = Prophet(yearly_seasonality=True, weekly_seasonality=False)

    model.fit(prophet_df)

    future = model.make_future_dataframe(periods=months,freq="ME")
    forecast= model.predict(future)

    return forecast[
        ["ds","yhat","yhat_lower","yhat_upper"]
    ]
