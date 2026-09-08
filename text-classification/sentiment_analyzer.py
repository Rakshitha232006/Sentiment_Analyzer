import pandas as pd
import matplotlib.pyplot as plt

from transformers import pipeline

analyzer = pipeline(
    "text-classification",
    model="distilbert/distilbert-base-uncased-finetuned-sst-2-english"
)


def sentiment_analyzer(review):
    sentiment = analyzer(str(review))
    return sentiment[0]["label"]


def sentiment_bar_chart(df):
    sentiment_counts = (
        df["Sentiment"]
        .value_counts()
        .reindex(["POSITIVE", "NEGATIVE"], fill_value=0)
    )

    fig, ax = plt.subplots()

    sentiment_counts.plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Review Sentiment Counts")
    ax.set_xlabel("Sentiment")
    ax.set_ylabel("Count")
    ax.set_xticklabels(
        ["Positive", "Negative"],
        rotation=0
    )

    return fig


def read_reviews_and_analyze_sentiment(file_object):
    df = pd.read_excel(file_object)

    if "Reviews" not in df.columns:
        raise ValueError("Excel file must contain 'Reviews' column")

    df["Sentiment"] = df["Reviews"].apply(sentiment_analyzer)

    chart_object = sentiment_bar_chart(df)

    return df, chart_object