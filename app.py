import sys
import os
sys.path.append(os.path.dirname(__file__))

import streamlit as st
import pandas as pd
import sqlite3
from textblob import TextBlob

st.set_page_config(page_title="Student Complaint Portal", layout="wide")

st.title("AI-Powered Student Complaint Portal")

menu = st.sidebar.selectbox("Menu", [
    "Dashboard",
    "Raise Complaint",
    "View Complaints",
    "Admin Panel",
    "AI Analysis"
])

# Create DB
conn = sqlite3.connect("complaints.db")
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS complaints
             (name TEXT, title TEXT, description TEXT, category TEXT, status TEXT)""")
conn.commit()

# Dashboard
if menu == "Dashboard":
    st.subheader("Complaint Dashboard")

    data = pd.read_sql("SELECT status, COUNT(*) as count FROM complaints GROUP BY status", conn)

    if not data.empty:
        st.bar_chart(data.set_index("status"))
    else:
        st.write("No complaints yet")

# Raise Complaint
elif menu == "Raise Complaint":
    st.subheader("Raise Complaint")

    name = st.text_input("Your Name")
    title = st.text_input("Complaint Title")
    description = st.text_area("Description")
    category = st.selectbox("Category", ["Hostel", "Food", "Academics", "Transport"])

    if st.button("Submit"):
        c.execute("INSERT INTO complaints VALUES (?, ?, ?, ?, ?)",
                  (name, title, description, category, "Pending"))
        conn.commit()
        st.success("Complaint Submitted")

# View Complaints
elif menu == "View Complaints":
    st.subheader("All Complaints")
    df = pd.read_sql("SELECT * FROM complaints", conn)
    st.dataframe(df)

# Admin Panel
elif menu == "Admin Panel":
    st.subheader("Update Complaint Status")

    df = pd.read_sql("SELECT rowid, * FROM complaints", conn)
    st.dataframe(df)

    cid = st.number_input("Enter Complaint ID", min_value=1)
    status = st.selectbox("Status", ["Pending", "In Progress", "Resolved"])

    if st.button("Update Status"):
        c.execute("UPDATE complaints SET status=? WHERE rowid=?", (status, cid))
        conn.commit()
        st.success("Updated")

# AI Analysis
elif menu == "AI Analysis":
    st.subheader("AI Complaint Sentiment")

    text = st.text_area("Enter complaint text")

    if st.button("Analyze"):
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity

        if sentiment < 0:
            st.error("Negative Complaint")
        elif sentiment == 0:
            st.warning("Neutral Complaint")
        else:
            st.success("Positive Complaint")

conn.close()
