import streamlit as st
from data_fetcher import get_top_30_coins
from suggestion_engine import suggest_swaps

st.set_page_config(page_title="Crypto Swap AI", layout="wide")
st.title("🔁 AI-Powered Crypto Swap Suggestions")

st.markdown("""
This dashboard analyzes the top 30 cryptocurrencies in real-time and suggests profitable short-term swaps based on momentum, RSI, and volume.
""")

with st.spinner("Fetching latest market data..."):
    market_data = get_top_30_coins()

if market_data is None or market_data.empty:
    st.error("Failed to fetch market data. Please try again later.")
    st.stop()

st.subheader("📊 Current Market Overview")
st.dataframe(market_data.style.format({"price": "${:,.2f}", "change_24h": "{:+.2f}%"}))

st.subheader("💡 Suggested Swaps")
suggestions = suggest_swaps(market_data)

if suggestions:
    for suggestion in suggestions:
        st.success(f"Swap **{suggestion['from']} → {suggestion['to']}**: {suggestion['reason']}")
else:
    st.info("No profitable swaps detected at the moment. Try again in a few minutes.")
