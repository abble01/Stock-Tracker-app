import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


def get_data(tick, prd):
    
    
    
    data = yf.download(tick, period=prd)
    
    
    

def main():
    st.write("Simple Stock tracker.")
    
    ticker = st.text_input(label= "Enter ticker eg, AAPL")
    period = st.selectbox(label="Select time period", options=("1d", "1mo", "1y"))
    
    if st.button(label="Get Data"):
        get_data
    
if __name__ == "__main__":
    main()