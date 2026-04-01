import streamlit as st
from dashboard import show_dashboard

st.sidebar.title("Student Portal")

menu = ["Dashboard"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Dashboard":
    show_dashboard()
