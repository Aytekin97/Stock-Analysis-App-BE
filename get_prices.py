import requests

API_KEY = 'RUR10MV03KZ9V50B'
symbol = 'TSLA'
interval = '5min'
url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval={interval}&apikey={API_KEY}'

response = requests.get(url)
data = response.json()

if "Time Series (5min)" in data:
    time_series = data["Time Series (5min)"]
    for time, values in time_series.items():
        print(f"Time: {time}")
        print(f"Open: {values['1. open']}")
        print(f"High: {values['2. high']}")
        print(f"Low: {values['3. low']}")
        print(f"Close: {values['4. close']}")
        print(f"Volume: {values['5. volume']}\n")
else:
    print("Error fetching data:", data.get("Note", "Unknown error"))
