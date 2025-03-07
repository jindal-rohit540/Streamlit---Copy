import yfinance as yf
import streamlit as st 

import datetime

st.title("This is my stock price application")

# col1, col2, col3 = st.columns(3)

# with col1:
#     st.header("A cat")
#     st.image("https://static.streamlit.io/examples/cat.jpg")

# with col2:
#     st.header("A dog")
#     st.image("https://static.streamlit.io/examples/dog.jpg")

# with col3:
#     st.header("An owl")
#     st.image("https://static.streamlit.io/examples/owl.jpg")

col1, col2= st.columns(2)


with col1:
    start_date = st.date_input("Please enter the start date", datetime.date(2019,1,1))


with col2:
    end_date = st.date_input("Please enter the end date", datetime.date(2022,12,31))






ticker_symbol = st.text_input("Please enter the ticker symbol of the stock", "AAPL")


ticker_data = yf.Ticker(ticker_symbol)


ticker_df = ticker_data.history(period="1d", start=start_date, end= end_date)



st.dataframe(ticker_df)

st.write(f"Daily Closing Price of the stock {ticker_symbol}")

st.line_chart(ticker_df['Close'])


st.write(f"Volumn of the stock {ticker_symbol}")

st.line_chart(ticker_df['Volume'])


