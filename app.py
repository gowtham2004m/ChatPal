from flask import Flask, request, render_template, jsonify
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json
import random

app = Flask(__name__)


# Initialize VADER sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Load responses from JSON file
with open('responses.json', 'r', encoding='utf-8') as file:
    responses = json.load(file)

# Precompute sentiment thresholds
sentiment_thresholds = {
    "positive": 0.05,
    "negative": -0.05,
}

# Function to determine sentiment and provide a response
def get_response(text):
    sentiment = analyze_sentiment(text)
    response = random.choice(responses[sentiment])
    return response

# Function to analyze sentiment
def analyze_sentiment(text):
    sentiment = sia.polarity_scores(text)
    for sentiment_label, threshold in sentiment_thresholds.items():
        if sentiment['compound'] >= threshold:
            return sentiment_label
    return "neutral"

@app.route('/')
def chat_interface():
    return render_template('chatbot.html')

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_input = request.form['message']
    sentiment_response = get_response(user_input)
    return jsonify({"response": sentiment_response})

if __name__ == '__main__':
    app.run(debug=True)
