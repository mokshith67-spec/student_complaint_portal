import streamlit as st
import sqlite3

def show_complaint_form():
    st.title("Raise a Complaint")

    name = st.text_input("Your Name")
    title = st.text_input("Complaint Title")
    description = st.text_area("Description")
    category = st.selectbox("Category", ["Hostel", "Food", "Academics", "Transport"])

    if st.button("Submit Complaint"):
        conn = sqlite3.connect("complaints.db")
        c = conn.cursor()

        c.execute("""CREATE TABLE IF NOT EXISTS complaints
                     (name TEXT, title TEXT, description TEXT, category TEXT, status TEXT)""")

        c.execute("INSERT INTO complaints VALUES (?, ?, ?, ?, ?)",
                  (name, title, description, category, "Pending"))

        conn.commit()
        conn.close()

        st.success("Complaint Submitted Successfully!")
