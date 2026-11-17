import streamlit as st
import requests
from datetime import date
import pandas as pd

api_url = "http://localhost:8000"

def analytics_monthly_ui():
    st.header("Analytics By Month")
    response = requests.get(f"{api_url}/monthly_analytics")
    if response.status_code == 200:
        df = pd.DataFrame(response.json())
        st.bar_chart(df.reset_index(),x="month_year",y="total_amount")
        st.dataframe(df, hide_index=True)
    else:
        st.error("failed to retrieve data")