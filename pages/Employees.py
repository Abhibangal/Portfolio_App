import streamlit as st
import pandas as pd

st.set_page_config(layout='wide', page_title='Employees')

st.title('The Best Company')
st.write("""According to the Pew Research Center, 97% of adult Americans have a cell phone capable of receiving text 
        messages.As time spent on phones continues to increase, it’s no surprise that businesses are pursuing text 
        message marketing campaigns. There are dozens of quality services on the market, but a few stand out, especially
        for small businesses looking to please subscribers. We researched 13 text message marketing services and chose 
        our five best picks based on their features, pricing, ease of use, setup process and customer service.""")
st.header('Our team')
emp_df = pd.read_csv('pages/data.csv')

col1, col2, col3 = st.columns([2, 2, 2])


with col1:
    for index, dat in emp_df[:4].iterrows():
        st.header(dat['first_name'].title() + ' ' + dat['last_name'].title())
        st.write(dat['role'])
        img = dat['image']
        st.image(f'pages/images/{img}', width=175)

with col2:
    for index, dat in emp_df[4:8].iterrows():
        st.header(dat['first_name'].title() + ' ' + dat['last_name'].title())
        st.write(dat['role'])
        img = dat['image']
        st.image(f'pages/images/{img}', width=175)

with col3:
    for index, dat in emp_df[8:].iterrows():
        st.header(dat['first_name'].title() + ' ' + dat['last_name'].title())
        st.write(dat['role'])
        img = dat['image']
        st.image(f'pages/images/{img}', width=175)
