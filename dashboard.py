import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_dashboard():
    st.title("Complaint Dashboard")

    data = {
        "Status": ["Pending", "In Progress", "Resolved"],
        "Count": [10, 5, 15]
    }

    df = pd.DataFrame(data)

    fig, ax = plt.subplots()
    ax.pie(df["Count"], labels=df["Status"], autopct='%1.1f%%')

    st.pyplot(fig)
