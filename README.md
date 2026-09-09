# 📊 Sentiment Analyzer

A Machine Learning web application that analyzes the sentiment of customer reviews using a pre-trained DistilBERT model.

## 🌐 Live Demo

👉 **[Open the Sentiment Analyzer](https://sentimentanalyzer-gvrq5pyvr7sahykc63ped5.streamlit.app/)**

You can upload an Excel file containing customer reviews and the application will analyze the sentiment of each review.

## ✨ Features

- 📁 Upload reviews using an Excel (`.xlsx`) file
- 🤖 Sentiment analysis using a pre-trained DistilBERT model
- 😊 Classifies reviews as Positive or Negative
- 📊 Displays the sentiment of each review
- 📈 Shows a sentiment distribution chart
- ⬇️ Allows users to download the analyzed results
- 🌐 Deployed using Streamlit Community Cloud

## 🧠 Machine Learning Model

This project uses:

**DistilBERT — `distilbert/distilbert-base-uncased-finetuned-sst-2-english`**

The model is a fine-tuned DistilBERT model for sentiment classification.

## 📂 Project Structure

```text
Sentiment_Analyzer/
│
├── main.py
├── requirements.txt
├── README.md
│
├── text-classification/
│   └── sentiment_analyzer.py
│
├── files/
│   └── prod_review.xlsx
│
└── installations/
    └── requirements.txt
📋 Excel File Format

The uploaded Excel file should contain a column named:

Reviews
Example
Reviews
This product is excellent
I really like this product
The quality is terrible
Very disappointing product

The application will add a Sentiment column to the results.

Example Output
Reviews	Sentiment
This product is excellent	POSITIVE
I really like this product	POSITIVE
The quality is terrible	NEGATIVE
Very disappointing product	NEGATIVE
🛠️ Technologies Used
Python
Streamlit
Hugging Face Transformers
DistilBERT
PyTorch
Pandas
Matplotlib
OpenPyXL
💻 Run Locally
1. Clone the repository
git clone https://github.com/Rakshitha232006/Sentiment_Analyzer.git
2. Open the project
cd Sentiment_Analyzer
3. Create a virtual environment
python -m venv .venv
4. Activate the virtual environment

On Windows:

.venv\Scripts\activate
5. Install the required packages
pip install -r requirements.txt
6. Run the application
streamlit run main.py

The application will open in your browser.

☁️ Deployment

This application is deployed using Streamlit Community Cloud.

🌐 Live Application

https://sentimentanalyzer-gvrq5pyvr7sahykc63ped5.streamlit.app/

The application can be accessed online without running the project locally.

📌 Future Improvements
Add Neutral sentiment classification
Display sentiment confidence scores
Add more visualization options
Support CSV files
Add review filtering and search
Improve the user interface
Add more sentiment analysis models
👩‍💻 Author

Rakshitha

GitHub

https://github.com/Rakshitha232006

Project Repository

https://github.com/Rakshitha232006/Sentiment_Analyzer
