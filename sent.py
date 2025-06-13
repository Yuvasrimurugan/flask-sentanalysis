from flask import Flask, request, jsonify
from sentiment_model import analyze_sentiment

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Sentiment Analysis API!"

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()

    if 'text' not in data:
        return jsonify({"error": "Missing 'text' in request"}), 400

    text = data['text']
    result = analyze_sentiment(text)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True) 