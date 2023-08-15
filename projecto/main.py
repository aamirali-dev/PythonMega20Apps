import streamlit as st
import pandas as pd

col1, col2 = st.columns(2)

with col1:
    st.image('images/photo.png')

with col2:
    st.title('Aamir Ali')
    st.info('Hey everybody')

st.write('Below you can find some of the apps I have built so feel free to check out')

df = pd.read_csv('data.csv', sep=';')

col3, empty_col ,col4 = st.columns([1.5, 0.5, 1.5])

with col3:
    for index, row in df[:10].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f'[Source Code]({row["url"]})')

with col4:
    for index, row in df[10:].iterrows():
        st.header(row['title'])
        st.write(row['description'])
        st.image("images/" + row['image'])
        st.write(f'[Source Code]({row["url"]})')