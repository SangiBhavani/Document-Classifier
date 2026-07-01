import streamlit as st
import pandas as pd
import numpy as np

st.title("📄 Simple Document Classifier")

st.write("Enter a document to classify.")

user_input = st.text_area("Enter Document")

categories = {
    "Sports": ["cricket", "football", "tennis", "match", "player", "score"],
    "Technology": ["python", "ai", "artificial intelligence", "machine learning", "computer", "software"],
    "Business": ["market", "company", "business", "profit", "startup", "investment"],
    "Politics": ["government", "election", "minister", "parliament", "policy"],
    "Entertainment": ["movie", "actor", "music", "film", "concert", "award"]
}

if st.button("Predict"):

    if user_input.strip() == "":
        st.warning("Please enter some text.")

    else:
        text = user_input.lower()
        prediction = "Unknown"

        for category, keywords in categories.items():
            if any(keyword in text for keyword in keywords):
                prediction = category
                break

        st.success(f"Predicted Category: {prediction}")