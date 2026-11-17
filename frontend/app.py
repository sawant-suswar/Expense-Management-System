import streamlit as st
from add_upload_ui import add_upload_setup
from analytics_ui import  analytics_setup
from analytics_monthly_ui import analytics_monthly_ui


st.header("Expense Tracker Management")

tab1, tab2, tab3 = st.tabs(["Add/Update","Analytics_Category","Analytics_Monthly"])

with tab1:
    add_upload_setup()

with tab2:
    analytics_setup()

with tab3:
    analytics_monthly_ui()