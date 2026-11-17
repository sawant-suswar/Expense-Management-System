import streamlit as st
import requests
from datetime import date

api_url = "http://localhost:8000"

def add_upload_setup():
    required_date = st.date_input("Enter the date to fetch details", date(2024, 8, 1), label_visibility='collapsed')
    expenses = requests.get(f"{api_url}/expenses/{required_date}")
    if expenses.status_code == 200:
        expenses_data = expenses.json()
        #st.write(expenses_data)
    else:
        expenses_data = []
        st.error("Unable to fetch expenses data")

    categories = ['Entertainment', 'Shopping', 'Food', 'Rent', 'Other']
    new_data = []

    with st.form(key="expenses_form"):
        cln1, cln2, cln3 = st.columns(3)
        with cln1:
            cln1.subheader("Amount")
        with cln2:
            cln2.subheader("Category")
        with cln3:
            cln3.subheader("Notes")

        for i in range(0, 5):
            if i < len(expenses_data):
                amount = expenses_data[i]["amount"]
                category = expenses_data[i]["category"]
                notes = expenses_data[i]["notes"]
            else:
                amount = 0.0
                category = "Other"
                notes = ""
            cln1, cln2, cln3 = st.columns(3)
            with cln1:
                amount_input = st.number_input(label="Amount", value=round(float(amount), 2), min_value=0.0, step=1.0,
                                               key=f"amount_{required_date}_{i}", label_visibility='collapsed')
            with cln2:
                category_input = st.selectbox(label="category", options=categories, index=categories.index(category),
                                              key=f"category_{required_date}_{i}", label_visibility='collapsed')
            with cln3:
                notes_input = st.text_input(label="notes", value=notes, key=f"notes_{required_date}_{i}",
                                            label_visibility='collapsed')

            new_data.append({
                "amount": amount_input,
                "category": category_input,
                "notes": notes_input
            })

        button = st.form_submit_button("Submit")
        if button:
            new_data = [i for i in new_data if i["amount"] > 0]
            post_status = requests.post(f"{api_url}/expenses/{required_date}/", json=new_data)
            if post_status.status_code == 200:
                st.write("Updated the expenses database successfully")


