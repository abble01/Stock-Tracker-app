import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import streamlit as st
import datetime

#Project 2 - Stock visualiser + more.

today = datetime.date.today
options = ["MSFT", "AAPL", "TSLA", "GOOGL"]

def get_data(tick, prd, interval):
    
    if tick:
        data = yf.download(tick, period=prd, interval=interval)
    if data.empty:
        return
    st.write(f"Stock price for {tick} over {prd}")
    st.line_chart(data["Close"])
    
    
    start_date = data.index[0]
    end_date = data.index[-1]
    # add moving average and candlestick graph next session

def main():
    st.sidebar.header("Stock price visualizer")
    
    ticker = st.sidebar.multiselect(label= "Enter ticker(s) eg, AAPL", options=options)
    period = st.sidebar.selectbox(label="Select time period", options=("1d", "5d", "1mo", "1y", "6y"))
    interval = st.sidebar.selectbox(label="Enter the interval you want", options=("2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"))
    avg = st.sidebar.number_input(label="Enter a moving average", value=9)
    
    
    if st.sidebar.button(label="Get Data"):
        get_data(ticker, period, interval)
    
    
    
    

if __name__ == "__main__":
    main()