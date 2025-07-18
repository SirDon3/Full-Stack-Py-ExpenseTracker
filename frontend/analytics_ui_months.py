import pandas as pd
import streamlit as st
from datetime import datetime
import requests

API_URL = "http://localhost:8000"

def analytics_tab_by_months():
    response = requests.get(f"{API_URL}/analytics/monthly")
    if response.status_code == 200:
        monthly_data = response.json()

        # Create DataFrame
        df = pd.DataFrame(monthly_data)

        # Optional: Sort by month (assuming "month" is YYYY-MM format)
        df = df.sort_values(by="month")

        # Plotting bar chart
        st.title("Monthly Expense Overview")
        st.bar_chart(data=df.set_index("month")["total_expense"], use_container_width=True)

        # Optional: Show table with month names
        if "month_name" in df.columns:
            df["total_expense"] = df["total_expense"].map("{:.2f}".format)
            st.table(df[["month_name", "total_expense"]])
        else:
            st.table(df)

    else:
        st.error("Failed to retrieve monthly expenses")