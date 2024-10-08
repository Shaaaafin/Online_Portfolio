import streamlit as st
from send_email import send_email

st.header("Contact Me")

with st.form(key="email"):
    user_email = st.text_input("Enter your email address here.")
    raw_message = st.text_area("Your message")
    # Ensure proper formatting without unwanted spaces
    message = f"""\
Subject: New email from {user_email}

From: {user_email}

{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully!")
