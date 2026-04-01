import streamlit as st
import sqlite3
import pandas as pd

def show_admin_panel():
    st.title("Admin Panel")

    conn = sqlite3.connect("complaints.db")
    df = pd.read_sql("SELECT rowid, * FROM complaints", conn)

    st.dataframe(df)

    complaint_id = st.number_input("Enter Complaint ID to Update", min_value=1)
    status = st.selectbox("Update Status", ["Pending", "In Progress", "Resolved"])

    if st.button("Update Status"):
        conn.execute("UPDATE complaints SET status=? WHERE rowid=?",
                     (status, complaint_id))
        conn.commit()
        st.success("Status Updated!")
