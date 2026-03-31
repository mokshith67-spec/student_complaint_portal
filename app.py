st.markdown("""
<style>
.big-title {
    font-size:40px;
    font-weight:bold;
    text-align:center;
    color:#4CAF50;
}
</style>
""", unsafe_allow_html=True)

st.markdown('<p class="big-title">Student Complaint Management System</p>', unsafe_allow_html=True)

import streamlit as st
from login import student_login, admin_login
from database import save_complaint, load_complaints, update_status, delete_complaint
from dashboard import show_dashboard

st.set_page_config(page_title="Student Complaint System", layout="wide")

menu = ["Home", "Student Login", "Admin Login"]
choice = st.sidebar.selectbox("Menu", menu)

st.title("Student Complaint Management System")

if choice == "Home":
    st.write("Welcome to Student Complaint Portal")

elif choice == "Student Login":
    st.subheader("Student Login")
    username = st.text_input("Roll Number")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if student_login(username, password):
            st.success("Login Successful")

            category = st.selectbox("Complaint Category",
            ["Academic","Hostel","Transport","Faculty","Infrastructure","Ragging","Exams","Canteen","Other"])

            complaint = st.text_area("Write Complaint")

            if st.button("Submit Complaint"):
                save_complaint(username, category, complaint)
                st.success("Complaint Submitted")

            st.subheader("Your Complaints")
            data = load_complaints()
            st.write(data[data["Roll"] == username])

        else:
            st.error("Invalid Login")


elif choice == "Admin Login":
    st.subheader("Admin Login")
    username = st.text_input("Admin Username")
    password = st.text_input("Admin Password", type="password")

    if st.button("Login"):
        if admin_login(username, password):
            st.success("Admin Login Successful")

            data = load_complaints()

            st.subheader("All Complaints")
            st.write(data)

            show_dashboard(data)

            st.subheader("Update Status")
            index = st.number_input("Enter Complaint Index", min_value=0)
            status = st.selectbox("Select Status", ["Pending","In Progress","Resolved","Rejected"])

            if st.button("Update"):
                update_status(index, status)
                st.success("Status Updated")

            st.subheader("Delete Complaint")
            del_index = st.number_input("Enter Index to Delete", min_value=0)

            if st.button("Delete"):
                delete_complaint(del_index)
                st.success("Deleted")

        else:
            st.error("Invalid Admin Login")
