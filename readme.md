# 📊 Social Media Sentiment Dashboard

A Streamlit web app for analyzing sentiment in product or social media reviews using the VADER NLP toolkit.

The app classifies each review as:
- 👍 Positive
- 😐 Neutral
- 👎 Negative

---

## 🚀 Features

- Upload your own CSV file or use a built-in sample dataset
- Real-time sentiment analysis of textual data
- Interactive sentiment distribution charts
- Clean and intuitive Streamlit UI
- Efficient, lightweight NLP processing with VADER

---

## 🧠 Tech Stack

- Python
- Streamlit
- Pandas
- NLTK (VADER Sentiment Analyzer)

---

## ▶️ How to Run

1. **Install dependencies:**
   ```bash
   python3 -m pip install streamlit pandas nltk
   ```

2. **Download VADER lexicon for NLTK (required for sentiment analysis):**
   ```bash
   python -c "import nltk; nltk.download('vader_lexicon')"
   ```

3. **Start the Streamlit app:**
   ```bash
   python -m streamlit run app.py
   ```

The dashboard will open in your browser. You can upload a CSV file with a `review` column, or use the sample data provided.
