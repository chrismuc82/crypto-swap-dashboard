import requests
import pandas as pd

COINGECKO_URL = "https://api.coingecko.com/api/v3/coins/markets"

def get_top_30_coins():
    try:
        params = {
            "vs_currency": "usd",
            "order": "market_cap_desc",
            "per_page": 30,
            "page": 1,
            "sparkline": False
        }
        response = requests.get(COINGECKO_URL, params=params)
        data = response.json()

        coins = []
        for coin in data:
            coins.append({
                "symbol": coin["symbol"].upper(),
                "name": coin["name"],
                "price": coin["current_price"],
                "change_24h": coin["price_change_percentage_24h"],
                "volume": coin["total_volume"]
            })

        return pd.DataFrame(coins)

    except Exception as e:
        print(f"Error fetching top 30 coins: {e}")
        return None
