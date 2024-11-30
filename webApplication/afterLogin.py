#########################################
## Provide information about dashboard ##
#########################################

import streamlit as st
from metatraderGetInfo import metaTrader as mt
from datetime import datetime as dt
from datetime import timedelta as tdelta
# import indicators as indi
import plotly.express as px
import pandas as pd



# Show account information

def displayAccountInfo(obj):
    user, passw, server = obj.getLoginInfo()
    st.title(f"Welcome, {user}.")
    st.write("Here are your account details:")
    accountInfo = obj.accountInformations()
    if accountInfo is not None:
        st.write(accountInfo)

# Provide data from MT5 about symbols


def getDataSymbols(obj):
    st.write('**Provide required information**')
    
    symbol = str(st.selectbox('Ticker', options=('EURUSD', 'AUDUSD', 'GBPUSD')))
    
    timeFrame = str(st.selectbox('Timeframe', options=('M1', 'M5', 'M15', 'M30', 'H1', 'H4')))
    
    date_select = st.date_input(
    "Pick a start date",
    value = dt.today(),  # Default value
    min_value = dt(2010, 1, 1),  # Minimum selectable date
    max_value = dt.now()  # Maximum selectable date
    )

    selected_datetime = dt.combine(date_select, dt.now().time())
    # yesterday1 = dt.now() - tdelta(days=1) # yesterday

    if st.button("Create dashboard"):
        prices = mt.getRealtimeData(symbol, timeFrame, selected_datetime, dt.now())
        if prices is not None:

            # Change prcies for minute display
            prices['time'] = pd.to_datetime(prices['time'], unit='s') 
            
            # Create figure - put it to other file
            fig = px.line(prices, x = prices['time'], y = prices['close'], title = symbol)
            st.plotly_chart(fig)

            # Show dataframe
            st.dataframe(prices)

            # # Create data operations
            # data_indicators = get_indicators(prices)
            # print(data_indicators)
        else:
            st.write("There is an issue with collecting data from MT5, please try, check if market is Online or select other period of time.")

# def get_indicators(prices):
#     data = indi.calculate_KNN(prices)
#     print(data)
#     data = indi.calculate_EMA_RIBBON(prices)
#     data = indi.calculate_RSI(prices, 7)
#     data.drop(['open', 'high', 'low', 'tick_volume', 'spread', 'real_volume'], axis=1, inplace=True)
#     return data

# Logout button

def show_logout_button():
    if st.button("Logout"):
        st.session_state["logged_in"] = False
        mt.shutDownConnection()
        st.experimental_rerun()  # Trigger a page rerun to show the login page
