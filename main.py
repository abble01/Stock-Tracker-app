import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import streamlit as st


#Project 2 - Stock visualiser + more.


options = ["MSFT", "AAPL", "TSLA", "GOOGL"]

def get_data(tick, prd, interval, avg1, avg2):
    
    if not tick:
        data = yf.download("AAPL", period=prd, interval=interval)
    else:
        data = yf.download(tickers=tick, period=prd, interval=interval)
    
    if data.empty:
        st,Warning("No data found")
        return None
        
    
    if not data.empty and isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.droplevel(1)
        
    
    st.write(f"Stock price for {tick} over {prd}")
    st.line_chart(data["Close"])
    
    
    #start_date = pd.to_datetime(data.index[0])
    #end_date = pd.to_datetime(data.index[-1])
    
    st.dataframe(data=data)
    
    data.index = pd.to_datetime(data.index)
    
    data["MA1"] = data["Close"].rolling(avg1).mean()
    data["MA2"] = data["Close"].rolling(avg2).mean()
    
    fig1 = go.Figure(
        data=[
            go.Scatter(
                x=data.index, 
                y=data["MA1"], 
                line=dict(color="orange", width=1),
                name="Candlestick moving average 1"
            ),
            
            go.Scatter(
                x=data.index,
                y=data["MA2"],
                line=dict(color="red", width=1),
                name="Moving average 2"),
            
            go.Candlestick(
                x=data.index, 
                open=data["Open"], 
                high=data["High"], 
                close=data["Close"], 
                low=data["Low"], 
                name=f"Candlestick for {tick}"
            )
        ]
    )


    fig1.update_layout(autosize=False, width=2600, height=1000, xaxis_rangeslider_visible=False)
    
    #st.plotly_chart(fig2, theme="streamlit")
    return fig1

def main():
    st.sidebar.header("Stock price visualizer")
    
    ticker = st.sidebar.selectbox(label= "Enter ticker(s) eg, AAPL", options=options)
    period = st.sidebar.selectbox(label="Select time period", options=("1d", "5d", "1mo", "1y", "6y"))
    interval = st.sidebar.selectbox(label="Enter the interval you want", options=("2m", "5m", "15m", "30m", "60m", "90m", "1h", "1d", "5d", "1wk", "1mo", "3mo"))
    
    avg1 = st.sidebar.number_input(label="Enter a moving average", value=9)
    avg2 = st.sidebar.number_input(label="Enter a moving average", value=18)
    
    if st.sidebar.button(label="Get Data"):
        fig = get_data(ticker, period, interval, avg1, avg2)
        if fig is not None:
            st.plotly_chart(fig)
    
    
    

if __name__ == "__main__":
    main()
