import streamlit as st
import seaborn as sns
from transformers import pipeline


sentiment_model = pipeline(model="sentiment-analysis")

st.write('Hi')

sentiments = []
for text in df['clean_text']:
    if list(sentiment_model(text)[0].values())[0] == 'LABEL_1':
        output = 'Positive'
    else:
        output = 'Negative'
    sentiments.append(output)

df['sentiments'] = sentiments
sns.countplot(df['sentiments'])
