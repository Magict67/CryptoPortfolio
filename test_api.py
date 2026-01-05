import requests

def test_bitcoin_price():
    print("Connecting to CoinGecko...")
    url = "https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd"
    
    try:
        response = requests.get(url)
        data = response.json()
        price = data['bitcoin']['usd']
        print(f"Success! The current price of Bitcoin is: ${price:,.2f}")
    except Exception as e:
        print(f"Something went wrong: {e}")

if __name__ == "__main__":
    test_bitcoin_price()