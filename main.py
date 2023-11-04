import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder
import pickle
import streamlit as st
from pyarrow.vendored import docscrape
#print(st.__version__)

with open('naive_bayes_classifier.pkl', 'rb') as file:
    loaded_classifier = pickle.load(file)
    loaded_vectorizer = pickle.load(file)
    loaded_label_encoder = pickle.load(file)

st.title("Sports News Text Classification")


num_test_headlines = st.number_input("Enter the number of test headlines:", min_value=1, step=1)

new_data = []
for i in range(num_test_headlines):
    test_headline = st.text_area(f"Test Headline {i + 1}:", f"Enter your test headline {i + 1} here")
    new_data.append(test_headline)

if st.button("Classify"):
  
    new_data_vectorized = loaded_vectorizer.transform(new_data)

    
    new_data_predictions = loaded_classifier.predict(new_data_vectorized)

    
    predicted_labels = loaded_label_encoder.inverse_transform(new_data_predictions)

    
    for data, label in zip(new_data, predicted_labels):
        st.write(f"Headline: {data}")
        st.write(f"Predicted Sport Name: {label}")
        