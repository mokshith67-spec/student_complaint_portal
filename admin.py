import streamlit as st
from database import load_complaints
from pdf_report import generate_pdf

st.title("Admin Panel - Student Complaints")

password = st.text_input("Enter Admin Password", type="password")

if password == "admin123":
    data = load_complaints()
    st.write(data)

    if st.button("Generate PDF Report"):
        generate_pdf(data)
        with open("complaints_report.pdf", "rb") as f:
            st.download_button("Download Report", f, file_name="Complaints_Report.pdf")
else:
    st.warning("Enter Admin Password to View Complaints")
