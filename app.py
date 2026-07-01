import streamlit as st
import pandas as pd
import numpy as np

# Knowledge Base
data = {
    "Question": [
        "What is Python?",
        "What is AI?",
        "What is Machine Learning?",
        "What is Streamlit?",
        "What is Pandas?",
        "What is NumPy?",
        "Who developed Python?",
        "What is Data Science?"
    ],

    "Answer": [
        "Python is a high-level programming language.",
        "Artificial Intelligence enables machines to think and learn.",
        "Machine Learning is a subset of Artificial Intelligence.",
        "Streamlit is used to build web applications in Python.",
        "Pandas is used for data analysis and manipulation.",
        "NumPy is used for numerical computations with arrays.",
        "Python was developed by Guido van Rossum.",
        "Data Science is the process of extracting insights from data."
    ]
}

df = pd.DataFrame(data)

st.title("🤖 Simple Retrieval Chatbot")

st.write("Ask a question from the knowledge base.")

user_question = st.text_input("Enter your question")

if st.button("Ask"):

    if user_question.strip() == "":
        st.warning("Please enter a question.")

    else:

        found = False

        for i in range(len(df)):

            if user_question.lower() == df.loc[i, "Question"].lower():

                st.success(df.loc[i, "Answer"])
                found = True
                break

        if not found:

            st.error("Sorry! I don't know the answer.")