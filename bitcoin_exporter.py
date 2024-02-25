from prometheus_client import start_http_server, Gauge
import requests
import time

# Define a Prometheus Gauge metric
bitcoin_price_metric = Gauge('bitcoin_price', 'Current price of Bitcoin in USD')

# Function to fetch Bitcoin price from Coindesk API
def fetch_bitcoin_price():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        data = response.json()
        price = data['bpi']['USD']['rate_float']
        return price
    except Exception as e:
        print(f"Error fetching Bitcoin price: {e}")
        return None

# Function to update the Prometheus metric with the current Bitcoin price
def update_bitcoin_price_metric():
    price = fetch_bitcoin_price()
    if price is not None:
        bitcoin_price_metric.set(price)

if __name__ == '__main__':
    # Start the Prometheus HTTP server on port 8000
    start_http_server(8000)
    
    # Periodically update the Bitcoin price metric
    while True:
        update_bitcoin_price_metric()
        time.sleep(60)  # Update every 60 seconds
