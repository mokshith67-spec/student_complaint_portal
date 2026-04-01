import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("complaints.csv")

st.title("Complaint Dashboard")

status_count = data["status"].value_counts()

fig, ax = plt.subplots()
ax.pie(status_count, labels=status_count.index, autopct='%1.1f%%')

st.pyplot(fig)
