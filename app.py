import streamlit as st
import pandas as pd
from src.sentiment import get_sentiment
from src.data_loader import load_data

st.set_page_config(page_title="Sentiment Dashboard", layout="wide")

st.title("📊 Social Media Sentiment Dashboard")

option = st.radio("Choose input type:", ["Upload CSV", "Use Sample Data"])

if option == "Upload CSV":
    file = st.file_uploader("Upload a CSV file with a 'review' column")

    if file:
        df = pd.read_csv(file)
    else:
        df = None
else:
    df = load_data()

if df is not None:
    if "review" not in df.columns:
        st.error("CSV must contain a 'review' column")
    else:
        df["sentiment"] = df["review"].apply(get_sentiment)

        st.subheader("🔍 Sample Data")
        st.dataframe(df.head())

        st.subheader("📊 Sentiment Distribution")
        sentiment_counts = df["sentiment"].value_counts()
        st.bar_chart(sentiment_counts)

        st.subheader("📈 Detailed View")
        st.dataframe(df)

st.write("DEBUG option:", option)
st.write("DEBUG df:", df)
