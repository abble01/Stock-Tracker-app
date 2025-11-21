import yfinance as yf
import matplotlib.pyplot as plt
import streamlit as st


def get_data(tick, prd):
     
    data = yf.download(tick, period=prd)
    if not data:
        return
    ...
    

def main():
    st.write("Simple Stock tracker.")
    
    ticker = st.text_input(label= "Enter ticker eg, AAPL")
    period = st.selectbox(label="Select time period", options=("1d", "1mo", "6mo", "1y", "5y"))
    
    if st.button(label="Get Data"):
        get_data
    
if __name__ == "__main__":
    main()
