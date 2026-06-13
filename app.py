import streamlit as st

st.set_page_config(page_title="Jasmine Keebler - Resume", page_icon="📊", layout="centered")

st.title("Jasmine Keebler")
st.caption("Glendale, AZ | jrkeebler@liberty.edu | ://github.com")

st.header("Professional Summary")
st.write("""
Dynamic Data Architect and Operations Specialist specializing in symbolic mathematics, 
formal verification, and high-performance analytics...
""")

# Add a download button so recruiters can pull the actual PDF from your URL!
with open("Jasmine_Keebler_Resume.pdf", "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(
    label="📥 Download Official PDF Resume",
    data=PDFbyte,
    file_name="Jasmine_Keebler_Resume.pdf",
    mime="application/octet-stream"
)
