import streamlit as st
import pandas as pd
from utilities import generate_certificate

CSV_FILE = "test.csv"

st.title("CHPC Winter School 2026")
# st.subheader("Download certificate")

# Load CSV
df = pd.read_csv(CSV_FILE)

# --- Session state ---
if "verified_record" not in st.session_state:
    st.session_state.verified_record = None
if "name_for_certificate" not in st.session_state:
    st.session_state.name_for_certificate = ""

# --- Instruction ---
st.info(
    "Enter the **email registered with for Winter School**.  \n"
    "NB: Both email and surname must match to verify."
)


# --- Verify Section ---
email_input = st.text_input("Email address (registered):",placeholder="joedoe@example.com")
name_input = st.text_input("First Name or Surname (registered):",placeholder="John or Doe")

if st.button("Verify"):
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
        st.session_state.name_for_certificate = f"{matches.iloc[0]['first_name']} {matches.iloc[0]['surname']}"
        st.success("Eligible for certification")
    else:
        st.session_state.verified_record = None
        st.error("No matching record found. Make sure both email and surname match.")

# --- Certificate Section ---
name_for_certificate = st.text_input(
    "Name to appear on certificate:",
    value=st.session_state.name_for_certificate,
    disabled=(st.session_state.verified_record is None)
)

if st.button("Generate Certificate", disabled=(st.session_state.verified_record is None)):
    pdf_bytes, date_str, serial = generate_certificate(name_for_certificate)
    st.success(f"Certificate ready! Date: {date_str}, Serial: {serial}")

    st.download_button(
        label="Download Certificate",
        data=pdf_bytes,
        file_name=f"{name_for_certificate}_certificate.pdf",
        mime="application/pdf"
    )

# --- Footer / Acknowledgment ---
st.markdown(
    """
    ---
    Powered by Streamlit • Simplified Version
    """,
)
