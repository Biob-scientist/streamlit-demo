import streamlit as st
import pandas as pd


st.set_page_config(page_title="Streamlit Demo",
                   page_icon=":barchart",
                   layout='wide')

with open('style.css') as style:
    st.markdown(f'<style>{style.read()}</style>',unsafe_allow_html=True)

st.write('Hello world')
st.markdown ("# Streamlit Demo")
""" # Tech talk
 This tech talk is usually of Fridays

"""
st.checkbox("I am a human")
st.sidebar.write('This is side bar')

df=pd.DataFrame({'state':['Lagos','Ibadan','Kogi'],
              'gdp':[54,45,20]})

st.write(df)
st.table(df)


name=st.text_input('My name')
st.write(name)
#
#  Layout
col1,col2,col3=st.columns([2,2,2])

with col1:
    st.bar_chart(df, x='state',y='gdp')

with col2:
    st.markdown('## Demo')

with col2:
    st.table(df)