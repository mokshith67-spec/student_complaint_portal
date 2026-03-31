import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_dashboard(data):
    st.subheader("Complaint Statistics")

    if len(data) > 0:
        category_counts = data["Category"].value_counts()

        fig = plt.figure()
        plt.pie(category_counts, labels=category_counts.index, autopct='%1.1f%%')
        st.pyplot(fig)

        status_counts = data["Status"].value_counts()
        fig2 = plt.figure()
        plt.bar(status_counts.index, status_counts.values)
        st.pyplot(fig2)
    else:
        st.write("No complaints yet.")
