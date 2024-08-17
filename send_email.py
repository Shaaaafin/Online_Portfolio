import smtplib, ssl
import streamlit as st
import os


def send_email(message):
    host = "smtp.gmail.com"
    port = 465
    username = st.secrets("db_username")
    password = st.secrets("db_password")
    receiver = "muffinshafin@gmail.com"
    my_context = ssl.create_default_context()  # to send email securely

    with smtplib.SMTP_SSL(host, port, context=my_context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


send_email()
