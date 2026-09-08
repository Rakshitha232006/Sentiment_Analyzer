import torch
import gradio as gr
import pandas as pd
import matplotlib.pyplot as plt

from transformers import pipeline
# model_path = (
#    "../Model/models--distilbert--distilbert-base-uncased-finetuned-sst-2-english"
#    "/snapshots/714eb0fa89d2f80546fda750413ed43d93601a13")


# analyzer = pipeline("text-classification",
#                model=model_path)

# print(analyzer("This product is good"))
#
analyzer = pipeline("text-classification",
                 model="distilbert/distilbert-base-uncased-finetuned-sst-2-english")

def sentiment_analyzer(review):
    sentiment = analyzer(review)
    return sentiment[0]['label']

def sentiment_bar_chart(df):
    sentiment_counts = df['Sentiment'].value_counts()
    fig,ax=plt.subplots()
    sentiment_counts.plot(kind='bar',ax=ax,color=['green','red'])
    ax.set_title('Review Sentiment Counts')
    ax.set_xlabel('Sentiment')
    ax.set_ylabel('Count')
    ax.set_xticklabels(['Positive','Negative'],rotation=0)
    return fig


def read_reviews_and_analyze_sentiment(file_object):
    df=pd.read_excel(file_object)
    if 'Reviews' not in df.columns:
        raise ValueError("Excel file must contain 'Review' column")
    df['Sentiment']=df['Reviews'].apply(sentiment_analyzer)
    chart_object= sentiment_bar_chart(df)
    return df,chart_object

# result = read_reviews_and_analyze_sentiment("../files/prod_review.xlsx")
# print(result)
#
demo = gr.Interface(fn=read_reviews_and_analyze_sentiment,
                    inputs=[gr.File(file_types=[".xlsx"],label="Upload your Review file")],
                    outputs=[gr.Dataframe(label="Sentiments"),gr.Plot(label="Sentiment Analysis")],
                    title="Sentiment Analyzer",
                    description="THIS APPLICATION IS USED TO ANALYSE THE SENTIMENT BASED ON THE FILE UPLOADED")
demo.launch()

