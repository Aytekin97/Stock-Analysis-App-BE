# app.py
from flask import Flask, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)
API_KEY = os.getenv('API_KEY')

symbol = 'TSLA'
interval = '5min'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={API_KEY}'


@app.route('/api/stock/<symbol>', methods=['GET'])
def get_stock_data(symbol):
    interval = '5min'
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={API_KEY}'
    response = requests.get(url)
    data = response.json()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
