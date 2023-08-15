import streamlit as st
import pandas as pd

from mailer import send_email

st.header('Contact Me')

with st.form(key='contact'):
    user_email = st.text_input('Your Email Address')
    topic = st.selectbox('What topic do you want to discuss', ['Job Inquires', 'Project Proposals', 'Others'])
    message = st.text_area('Text')
    message = f'''
Subject: New Email From {user_email}
From: {user_email}
{message} 
    '''
    submit = st.form_submit_button('Submit')
    if submit:
        send_email(message)
        st.info('Your email has been sent')
