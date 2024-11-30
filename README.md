
# Trading view for forex index

A Python-based web application that integrates MetaTrader for forex data, pandas for analysis, and Streamlit for an interactive user interface. 
Users can log in, specify a time period, and view interactive charts for **EUR/USD, GBP/USD, and AUD/USD** currency pairs.

Just to login you have to proceed with creating *MetaTrader* account and instaling it on your windows enviroment. 
Whole web application is using *streamlit* as main core and connecting via user with MetaTrader to collect real time data about specified index. 

Index is shown with table and ticker on graph on page. You have also view for your balance and currency of your account. 

*Tickers that are avaliable - M1, M5, M15, M30, H1, H4*

# How to open this application?

First of all please clone this repository to your own enviroment, then go to directory WebApplication with your terminal window and run this command:

**streamlit run app.py**

You should see new window in your browser, just now proceed with your account information and feel free to use the graph in your browser just for free! 

# Planned updates

In next updates I will proceed with taking orders for buying those index at specified leverage. I will also update this view to have also some other indicators for defined ticker by user and make it more flexible to chose between dates and tickers. 

**Current version: 0.01**

# Contact me

If you have any questions please feel free to contact with me using this mail: **sebastiansuwada@gmail.com**

BR,
**Sebastian Suwada**