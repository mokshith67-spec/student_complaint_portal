import streamlit as st
from database import save_complaint

st.set_page_config(page_title="Student Complaint Portal")

st.title("Student Complaint Portal")

menu = ["Student Login", "Submit Complaint"]
choice = st.sidebar.selectbox("Menu", menu)

if choice == "Student Login":
    st.subheader("Login")
    name = st.text_input("Enter Name")
    roll = st.text_input("Enter Roll Number")

    if st.button("Login"):
        st.success(f"Welcome {name}")

elif choice == "Submit Complaint":
    st.subheader("Submit Your Complaint")

    name = st.text_input("Name")
    roll = st.text_input("Roll Number")

    complaint_type = st.selectbox(
        "Complaint Type",
        ["Academic", "Hostel", "Transport", "Faculty", "Infrastructure", "Other"]
    )

    priority = st.selectbox(
        "Priority",
        ["Low", "Medium", "High"]
    )

    complaint = st.text_area("Write Complaint")

    if st.button("Submit Complaint"):
        save_complaint(name, roll, complaint_type, priority, complaint)
        st.success("Complaint Submitted Successfully")
