import streamlit as st
from textblob import TextBlob

def show_ai_analysis():
    st.title("AI Complaint Analysis")

    text = st.text_area("Enter Complaint Text")

    if st.button("Analyze"):
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity

        if sentiment < 0:
            st.error("Negative Complaint")
        elif sentiment == 0:
            st.warning("Neutral Complaint")
        else:
            st.success("Positive Complaint")

        if "food" in text.lower():
            st.write("Category: Food")
        elif "hostel" in text.lower():
            st.write("Category: Hostel")
        elif "teacher" in text.lower():
            st.write("Category: Academics")
        else:
            st.write("Category: Other")
