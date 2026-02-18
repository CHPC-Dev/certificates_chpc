import streamlit as st
import pandas as pd
from utilities import generate_certificate

CSV_FILE = "test.csv"

st.title("Winter School Certificate 2026")

# Load CSV
df = pd.read_csv(CSV_FILE)

# Initialize session state
if "verified_record" not in st.session_state:
    st.session_state.verified_record = None

# --- FORM ---
with st.form("certificate_form"):
    email_input = st.text_input("Email address:")
    name_input = st.text_input("Enter First Name or Surname:")
    submit_search = st.form_submit_button("Verify Record")

# --- VERIFY ---
if submit_search:

    email_norm = email_input.strip().lower()
    name_norm = name_input.strip().lower()

    matches = df[
        (df["email"].str.lower() == email_norm) &
        (
            df["surname"].str.lower().str.contains(name_norm) |
            df["first_name"].str.lower().str.contains(name_norm)
        )
    ]

    if not matches.empty:
        st.session_state.verified_record = matches.iloc[0]
        st.success("Record verified ✅")
    else:
        st.error("No matching record found.")

# --- AFTER VERIFICATION ---
if st.session_state.verified_record is not None:

    record = st.session_state.verified_record
    full_name_default = f"{record['first_name']} {record['surname']}"

    name_for_certificate = st.text_input(
        "Name to appear on certificate:",
        value=full_name_default
    )

    if st.button("Generate Certificate"):
        pdf_bytes, date_str, serial = generate_certificate(name_for_certificate)

        st.success(f"Certificate ready! Date: {date_str}, Serial: {serial}")

        st.download_button(
            label="Download Certificate",
            data=pdf_bytes,
            file_name=f"{name_for_certificate}_certificate.pdf",
            mime="application/pdf"
        )
