#!/usr/bin/env python
# coding: utf-8

# In[2]:
import streamlit as st
import joblib
import re
import nltk
import numpy as np
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from scipy.sparse import hstack

nltk.download('stopwords')

# Load model + vectorizer
model = joblib.load("model.pkl")
vectorizer = joblib.load("vectorizer.pkl")

stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

# ----------------------------
# PREPROCESS (same as training)
# ----------------------------
def preprocess_text(text):
    text = str(text).lower()
    text = re.sub(r'http\S+|www\S+', ' url ', text)
    text = re.sub(r'\S+@\S+', ' email ', text)
    text = re.sub(r'[^a-zA-Z]', ' ', text)

    words = text.split()
    words = [
        stemmer.stem(word)
        for word in words
        if word not in stop_words
    ]

    return " ".join(words)


# ----------------------------
# EXTRA FEATURES (MUST MATCH TRAINING)
# ----------------------------
def extract_features(text):
    text = str(text).lower()

    return [
        int(bool(re.search(r'\d', text))),      # numbers
        int('%' in text or 'off' in text),      # discount
        int('free' in text),                    # free
        int('urgent' in text or 'hurry' in text),
        int('win' in text or 'winner' in text),
        len(text)
    ]


# ----------------------------
# UI
# ----------------------------
st.set_page_config(page_title="Spam Detector", page_icon="📧")

st.title("📧 Email Spam Detection System")
st.write("Enter an email message to check whether it is Spam or Ham.")

email = st.text_area("✉️ Enter Email Content")

if st.button("🔍 Predict"):

    if email.strip() == "":
        st.warning("Please enter some text!")

    else:
        cleaned = preprocess_text(email)

        # TF-IDF part
        tfidf_vec = vectorizer.transform([cleaned])

        # Extra features part
        extra_vec = np.array([extract_features(email)])

        # Combine (CRITICAL FIX)
        final_vec = hstack([tfidf_vec, extra_vec])

        pred = model.predict(final_vec)[0]

        if pred == 1:
            st.error("🚫 Spam Email Detected")
        else:
            st.success("✅ This is a Legitimate Email (Ham)")


# In[ ]:




