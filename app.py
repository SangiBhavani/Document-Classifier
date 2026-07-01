import streamlit as st
import numpy as np
import pandas as pd

st.title("🖼️ Image Prediction Demo")

uploaded_file = st.file_uploader(
    "Upload an Image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    st.image(uploaded_file, caption="Uploaded Image")

    info = {
        "Property": [
            "File Name",
            "File Type",
            "File Size (KB)"
        ],
        "Value": [
            uploaded_file.name,
            uploaded_file.type,
            round(uploaded_file.size / 1024, 2)
        ]
    }

    df = pd.DataFrame(info)

    st.subheader("Image Information")

    st.table(df)

    st.success("Prediction: Demo Image")