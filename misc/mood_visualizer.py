import streamlit as st
import os
from nltk.sentiment import SentimentIntensityAnalyzer
import plotly.express as px
analyzer = SentimentIntensityAnalyzer()

st.title('Diary Tone')
data = {}
for filename in os.listdir('diary'):
    with open(f'diary/{filename}', 'r') as file:
        data[filename.split('.')[0]] = file.read()
scores = {}
for (key, value) in data.items():
    scores[key] = analyzer.polarity_scores(value)

dates = []
positivity = []
negativity = []
for (key, score) in scores.items():
    dates.append(key)
    positivity.append(score['pos'])
    negativity.append(score['neg'])

st.subheader('Positivity')
figure = px.line(x=dates, y=positivity)
st.plotly_chart(figure)
st.subheader('Negativity')
figure_n = px.line(x=dates, y=negativity)
st.plotly_chart(figure_n)
