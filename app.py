# app.py
from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv('API_KEY')

@app.route('/api/stock/<symbol>', methods=['GET'])
def get_stock_data(symbol):
    interval = '60min'
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

@app.route('/api/test', methods=['GET'])
def test_route():
    return jsonify({"message": "Test route working"})

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Stock Analysis API"})



if __name__ == '__main__':
    # Get the port number from the environment variable or default to 5000 for local development
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
