import streamlit as st
import plotly.express as px
import pandas as pd

st.title('In Search for Happiness')

x = st.selectbox('Select the data for the x-axis', ('GDP', 'Happiness', 'Generosity'))
y = st.selectbox('Select the data for the y-axis', ('GDP', 'Happiness', 'Generosity'))

st.subheader(f'{x} and {y}')

data = pd.read_csv('data_small/happy.csv')


def get_data(x, y):
    return data[x.lower()], data[y.lower()]


figure = px.line(data_frame=data, x=data[x.lower()], y=data[y.lower()])
st.plotly_chart(figure)
