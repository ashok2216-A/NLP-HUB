import pandas as pd
import streamlit as st
import seaborn as sns
from data_cleaning import preprocess
from transformers import pipeline
from data_integration import scrape_all_pages

# st.image("logo.png", width=200, height=200)
st.image("logo.png", width=100)
st.subheader(':blue[NLP HUB®]')
st.header('Amazon Sentiment Analysis using FineTuned :green[GPT-2] Pre-Trained Model')

sentiment_model = pipeline(model="ashok2216/gpt2-amazon-sentiment-classifier")
# Example usage:-
sample_url = 'https://www.amazon.in/Dell-Inspiron-i7-1255U-Processor-Platinum/product-reviews/B0C9F142V6/ref=cm_cr_dp_d_show_all_btm?ie=UTF8&reviewerType=all_reviews'
url = st.text_input("Amazon product link", sample_url)
st.write("Done")
st.subheader('', divider='rainbow')
all_reviews = scrape_all_pages(url)
# Convert to DataFrame for further analysis
reviews = pd.DataFrame(all_reviews)
reviews['processed_text'] = reviews['content'].apply(preprocess)

# st.dataframe(reviews, use_container_width=True)
# st.markdown(sentiment_model(['It is Super!']))

sentiments = []
for text in reviews['processed_text']:
    if list(sentiment_model(text)[0].values())[0] == 'LABEL_1':
        output = 'Positive'
    else:
        output = 'Negative'
    sentiments.append(output)

reviews['sentiments'] = sentiments
st.markdown(':rainbow[Output]')
st.dataframe(reviews, use_container_width=True)
# sns.countplot(reviews['sentiments'])
