import smtplib, ssl
import streamlit as st
import os

def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = str(st.secrets["db_username"])  # Corrected to use square brackets
    password = str(st.secrets["db_password"])  # Corrected to use square brackets
    receiver = "muffinshafin@gmail.com"
    my_context = ssl.create_default_context()  # to send email securely

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
