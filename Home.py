import streamlit as st
import pandas as pd

st.set_page_config(layout='wide', page_title='Home')

df = pd.read_csv('data.csv',sep=';')


col1, col2 = st.columns([3, 3])

with col1:
    st.image('images/photo.jpg', width=400)

with col2:
    st.title("Abhijit Bangal")
    content2 = """Hi ,I am Abhijit Bangal. I am a data analyst ,programmer working in MNC.
                 I have graduated from Ramrao Adik Institute of Technology in 2014.
                 I have total of 8+ years of experience in data warehousing  and data analysis."""
    st.info(content2, icon="ℹ")

st.write('Below you can find some of the apps I built in python. Feel free to contact me ')

col3, empty_col,  col4 = st.columns([3, 1, 3])
with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.subheader(row['description'])
        img = row['image']
        st.image(f'images/{img}')
        st.write(f"[Click to open]({row['url']})")
with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        img = row['image']
        st.image(f'images/{img}')
        st.write(f"[Click to open]({row['url']})")