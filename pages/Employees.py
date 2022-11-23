import streamlit as st
import pandas as pd

st.set_page_config(layout='wide', page_title='Employees')

st.title('The Best Company')
st.write("""According to the Pew Research Center, 97% of adult Americans have a cell phone capable of receiving text 
        messages.As time spent on phones continues to increase, it’s no surprise that businesses are pursuing text 
        message marketing campaigns. There are dozens of quality services on the market, but a few stand out, especially
        for small businesses looking to please subscribers. We researched 13 text message marketing services and chose 
        our five best picks based on their features, pricing, ease of use, setup process and customer service.""")

emp_df = pd.read_csv('data.csv')