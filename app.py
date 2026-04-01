import streamlit as st
from dashboard import show_dashboard
from complaint_form import show_complaint_form
from complaint_list import show_complaints
from admin import show_admin_panel
from ai_analysis import show_ai_analysis

st.sidebar.title("Student Portal")

menu = ["Dashboard", "Raise Complaint", "My Complaints", "Admin Panel", "AI Analysis"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Dashboard":
    show_dashboard()

elif choice == "Raise Complaint":
    show_complaint_form()

elif choice == "My Complaints":
    show_complaints()

elif choice == "Admin Panel":
    show_admin_panel()

elif choice == "AI Analysis":
    show_ai_analysis()
