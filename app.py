elif choice == "Admin Login":
    st.subheader("Admin Login")

    if "admin_logged_in" not in st.session_state:
        st.session_state.admin_logged_in = False

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
