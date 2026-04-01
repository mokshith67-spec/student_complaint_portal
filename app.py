import nltk
nltk.download('punkt')

import streamlit as st
from login import student_login, admin_login
from database import save_complaint, load_complaints, update_status, delete_complaint
from dashboard import show_dashboard

st.set_page_config(page_title="Student Complaint System", layout="wide")

# Professional UI
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

menu = ["Home", "Student Login", "Admin Login"]
choice = st.sidebar.selectbox("Menu", menu)

# Session states
if "student_logged_in" not in st.session_state:
    st.session_state.student_logged_in = False
    st.session_state.student_roll = ""

if "admin_logged_in" not in st.session_state:
    st.session_state.admin_logged_in = False

# Home
if choice == "Home":
    st.write("Welcome to Student Complaint Portal")

# Student Login
elif choice == "Student Login":
    st.subheader("Student Login")

    if not st.session_state.student_logged_in:
        username = st.text_input("Roll Number")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            if student_login(username, password):
                st.session_state.student_logged_in = True
                st.session_state.student_roll = username
                st.success("Login Successful")
            else:
                st.error("Invalid Login")

    if st.session_state.student_logged_in:
        roll = st.session_state.student_roll

        st.subheader("Submit Complaint")
        category = st.selectbox("Complaint Category",
        ["Academic","Hostel","Transport","Faculty","Infrastructure","Ragging","Exams","Canteen","Other"])

        complaint = st.text_area("Write Complaint")

        if st.button("Submit Complaint"):
            save_complaint(roll, category, complaint)
            st.success("Complaint Submitted")

        st.subheader("Your Complaints")
        data = load_complaints()
        st.dataframe(data[data["Roll"] == roll])

        if st.button("Logout"):
            st.session_state.student_logged_in = False

# Admin Login
elif choice == "Admin Login":
    st.subheader("Admin Login")

    if not st.session_state.admin_logged_in:
        username = st.text_input("Admin Username")
        password = st.text_input("Admin Password", type="password")

        if st.button("Login"):
            if admin_login(username, password):
                st.session_state.admin_logged_in = True
                st.success("Admin Login Successful")
            else:
                st.error("Invalid Admin Login")

    if st.session_state.admin_logged_in:
        st.success("Welcome Admin")

        data = load_complaints()

        st.subheader("All Complaints")
        st.dataframe(data)

        st.subheader("Complaint Index Numbers")
        st.write(data.reset_index()[["index","ComplaintID","Roll","Category","Status"]])

        show_dashboard(data)

        st.subheader("Update Status")
        index = st.number_input("Enter Complaint Index", min_value=0, step=1)
        status = st.selectbox("Select Status", ["Pending","In Progress","Resolved","Rejected"])

        if st.button("Update Status"):
            update_status(index, status)
            st.success("Status Updated")

        st.subheader("Delete Complaint")
        del_index = st.number_input("Enter Index to Delete", min_value=0, step=1)

        if st.button("Delete Complaint"):
            delete_complaint(del_index)
            st.success("Complaint Deleted")

        if st.button("Logout"):
            st.session_state.admin_logged_in = False
