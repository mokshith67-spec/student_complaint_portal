import streamlit as st
import pandas as pd

def show_dashboard(data):
    st.subheader("Complaint Statistics")

    if len(data) > 0:
        st.write("Complaints by Category")
        st.bar_chart(data["Category"].value_counts())

        st.write("Complaints by Status")
        st.bar_chart(data["Status"].value_counts())
    else:
        st.write("No complaints yet.")
