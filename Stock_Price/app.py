import yfinance as yf
import  streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App
Shown are the stock closing proce and volume of ![img](https://99prod.s3.amazonaws.com/uploads/f1350adc-bdfd-43bf-b210-78d1919cbcf5/Google.png) 

""")


#adding a selectbox for the start year
year = 2010
years = ['2010', '2011', '2012', '2013', 2014, '2015', '2016', '2017', '2018', '2019']
st.write("## Select the start year:")
year = st.selectbox('Options:', years)
date = f'{year}-5-31'

st.write(f"Ok! lets go from {year} to 2020.")

# defining the ticker symbol to pass to yf
tickerSymbol = 'GOOGL'
# getting data from this ticker
tickerData = yf.Ticker(tickerSymbol)
# getting the historical prices 
tickerDf = tickerData.history(period='1d', start=date, end='2020-5-31')

# displaying the dataframe
st.write("""
## Want to take a look at the data retrieved?
Let me show you a piece of the table:
""")

st.write(tickerDf)

st.write("## Closing Price")
st.line_chart(tickerDf.Close)

st.write("## Volume Price")
st.line_chart(tickerDf.Volume)
