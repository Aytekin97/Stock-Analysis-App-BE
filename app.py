# app.py
from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os
from loguru import logger

app = Flask(__name__)
CORS(app)

API_KEY = os.getenv('API_KEY')

@app.route('/api/stock/<symbol>', methods=['GET'])
def get_stock_data(symbol):
    interval = '60min'
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={API_KEY}'

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        
        # Check if the response contains the expected data structure
        data = response.json()
        if "Time Series" in data or "Time Series (60min)" in data:
            logger.info("Request successful")
            return jsonify(data)
        else:
            # Handle cases where the response does not contain expected keys
            logger.error("error: Invalid API response. Please check your API key, symbol, or interval.")
            logger.error(f"details: {data}")
            return jsonify({
                "error": "Invalid API response. Please check your API key, symbol, or interval.",
                "details": data
            }), 400
    except requests.exceptions.RequestException as e:
        # Handle network or HTTP errors
        return jsonify({"error": "Failed to fetch stock data.", "details": str(e)}), 500


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
