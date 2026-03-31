elif choice == "Student Login":
    st.subheader("Student Login")

    if "student_logged_in" not in st.session_state:
        st.session_state.student_logged_in = False
        st.session_state.student_roll = ""

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
