import streamlit as st
import requests
from datetime import date
import pandas as pd

api_url = "http://localhost:8000"

def analytics_setup():
    cln1, cln2 = st.columns(2)
    with cln1:
        start_date = st.date_input("Start Date", date(2024,8,1))
    with cln2:
        end_date = st.date_input("End Date", date(2024,8,5))

    if st.button("Get Analytics"):
        payload = {
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }

        response = requests.post(f"{api_url}/analytics", json=payload)
        if response.status_code == 200 and response.json() is not None:
            if response.json() == {}:
                st.error("Data not available")
            else:
                data = response.json()
                df = pd.DataFrame(data)
                df_chart = df.drop("percentage")
                st.bar_chart(df_chart.T, use_container_width=True,height=400)
                st.dataframe(df.T)
        else:
            st.error("Data not available")
