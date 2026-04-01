import streamlit as st
import pandas as pd

def show_dashboard():
    st.title("Complaint Dashboard")

    data = {
        "Status": ["Pending", "In Progress", "Resolved"],
        "Count": [10, 5, 15]
    }

    df = pd.DataFrame(data)

    st.subheader("Complaint Status")
    st.bar_chart(df.set_index("Status"))
    st.line_chart(df.set_index("Status"))
