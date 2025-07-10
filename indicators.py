import pandas as pd
import numpy as np

def calculate_rsi(prices: list, period: int = 14):
    if len(prices) < period:
        return None

    deltas = np.diff(prices)
    seed = deltas[:period]
    up = seed[seed > 0].sum() / period
    down = -seed[seed < 0].sum() / period
    rs = up / down if down != 0 else 0
    rsi = 100 - (100 / (1 + rs))

    return round(rsi, 2)

def add_fake_rsi(df: pd.DataFrame):
    # Since we don't have historical prices in this MVP,
    # we'll fake RSI based on 24h change just for demo purposes.
    df = df.copy()
    df["rsi"] = df["change_24h"].apply(lambda x: 70 if x > 5 else (30 if x < -5 else 50))
    return df
