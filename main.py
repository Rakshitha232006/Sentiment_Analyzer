import streamlit as st
import sys
from pathlib import Path

# Add text-classification folder to Python path
sys.path.append(
    str(Path(__file__).parent / "text-classification")
)

from sentiment_analyzer import read_reviews_and_analyze_sentiment


st.set_page_config(
    page_title="Sentiment Analyzer",
    page_icon="📊",
    layout="wide"
)

st.title("📊 Sentiment Analyzer")

st.write(
    "Upload an Excel file containing reviews "
    "to analyze the sentiment of each review."
)

uploaded_file = st.file_uploader(
    "Upload your Review file",
    type=["xlsx"]
)


if uploaded_file is not None:

    try:
        df, chart = read_reviews_and_analyze_sentiment(
            uploaded_file
        )

        st.success("Sentiment analysis completed!")

        st.subheader("Review Results")

        st.dataframe(
            df,
            use_container_width=True
        )

        st.subheader("Sentiment Analysis")

        st.pyplot(chart)

        # Download results
        csv = df.to_csv(index=False).encode("utf-8")

        st.download_button(
            label="Download Results",
            data=csv,
            file_name="sentiment_results.csv",
            mime="text/csv"
        )

    except Exception as e:
        st.error(str(e))