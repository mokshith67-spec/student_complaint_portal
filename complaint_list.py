import streamlit as st
import sqlite3
import pandas as pd

def show_complaints():
    st.title("My Complaints")

    conn = sqlite3.connect("complaints.db")
    df = pd.read_sql("SELECT * FROM complaints", conn)

    st.dataframe(df)
