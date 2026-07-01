import streamlit as st
import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

# -----------------------------
# Create Dataset
# -----------------------------
data = {
    "text": [
        "India won the cricket match",
        "Virat Kohli scored a century",
        "Football World Cup begins",
        "Stock market rises today",
        "Company profits increased",
        "New startup gets funding",
        "Artificial Intelligence is changing healthcare",
        "Python is used in Machine Learning",
        "Cloud computing is growing rapidly",
        "Government announced a new policy",
        "Election campaigns started",
        "Parliament passed a bill",
        "New movie released this week",
        "Actor won an award",
        "Music concert attracted thousands"
    ],

    "category": [
        "Sports",
        "Sports",
        "Sports",
        "Business",
        "Business",
        "Business",
        "Technology",
        "Technology",
        "Technology",
        "Politics",
        "Politics",
        "Politics",
        "Entertainment",
        "Entertainment",
        "Entertainment"
    ]
}

df = pd.DataFrame(data)

# -----------------------------
# Train Model
# -----------------------------
X = df["text"]
y = df["category"]

vectorizer = TfidfVectorizer()

X_vector = vectorizer.fit_transform(X)

model = MultinomialNB()

model.fit(X_vector, y)

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("📄 AI Document Classifier")

st.write("Enter any text to classify the document.")

user_input = st.text_area("Enter Document")

if st.button("Predict"):

    if user_input.strip() == "":
        st.warning("Please enter some text.")

    else:
        test = vectorizer.transform([user_input])

        prediction = model.predict(test)

        st.success(f"Predicted Category: {prediction[0]}")