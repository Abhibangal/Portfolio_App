import streamlit as st
import send_email as se
import pandas as pd


st.title('Contact Me')
df = pd.read_csv('pages/topics.csv')

with st.form(key='contact_form', clear_on_submit=True):
    st.text_input(label="Your email address", key='email', placeholder='abc@xyz.com')
    st.selectbox('What topic to you want to discuss?',
                 options=df,
                 key='topic')
    st.text_area(label="Your message", key='msg', height=100)
    sub_button = st.form_submit_button(label='SUBMIT')
    if sub_button:
        send_by = st.session_state['email']
        topic = st.session_state['topic']
        actual_message = st.session_state['msg']
        message = f"""\
Subject: New message from {send_by}

From: {send_by}  
topic: {topic}

{actual_message}
        """
        if actual_message != '' and send_by != '':
            se.send(message)
            st.info('Mail sent successfully!!')
        else:
            st.info('Insert valid email-id /content')

