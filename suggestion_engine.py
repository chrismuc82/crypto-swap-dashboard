from indicators import add_fake_rsi

def suggest_swaps(df):
    suggestions = []
    df = add_fake_rsi(df)

    overbought = df[df["rsi"] >= 70]
    oversold = df[df["rsi"] <= 30]

    for _, ob in overbought.iterrows():
        for _, os in oversold.iterrows():
            if ob["symbol"] != os["symbol"]:
                suggestions.append({
                    "from": ob["symbol"],
                    "to": os["symbol"],
                    "reason": f"{ob['symbol']} is overbought (RSI={ob['rsi']}) and {os['symbol']} is oversold (RSI={os['rsi']})"
                })

    return suggestions[:5]  # Limit to top 5 suggestions
