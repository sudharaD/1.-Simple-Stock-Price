import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
#Simple Stock Price App

shown are the stock closing price and volume of google!

""")

#define the ticker sysmbol
tickerSymbol = 'GOOGL'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

# Open  High    Low Close   Volume  Dividents   Stock Splits

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)