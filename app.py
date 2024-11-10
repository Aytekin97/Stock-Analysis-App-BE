# app.py
from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/stock/<symbol>', methods=['GET'])
def get_stock_data(symbol):
    # Replace this with actual code to fetch data from Alpha Vantage
    data = {"symbol": symbol, "price": 100}  # Placeholder data
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
