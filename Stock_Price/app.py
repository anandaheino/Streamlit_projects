import yfinance as yf
import  streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
Shown are the stock closing proce and volume of ![img](https://99prod.s3.amazonaws.com/uploads/f1350adc-bdfd-43bf-b210-78d1919cbcf5/Google.png) 

""")

# defining the ticker symbol to pass to yf
tickerSymbol = 'GOOGL'
# getting data from this ticker
tickerData = yf.Ticker(tickerSymbol)
# getting the historical prices 
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)
