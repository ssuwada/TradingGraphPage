#################################
## Functions to execute in MT5 ##
#################################

import MetaTrader5 as MT
from datetime import datetime as dt
import pandas as pd
import streamlit as st
import plotly.express as px

class metaTrader:

    def __init__(self, login, password, server):
        self.login = login  # Attribute
        self.password = password # Attribute
        self.server = server   # Attribute
        # self.initializeMT(login,password,server)

    def getLoginInfo(self):
        return self.login, self.password, self.server

    def initializeMT(self, login, password, server):

        # Initialization 
        if not MT.initialize():
            print("Initialization Failure..")
            print("initialize() failed, error code =",MT.last_error())
        else:
            print("Initialization completed..")

        # Login initialization
        if not MT.login(login,password,server):
            print("Credentials failure..")
            print("initialize() failed, error code =",MT.last_error())
            loginReturn = False
        else:
            print("Connected to account: %d" % login)
            print("Server: %s" % server)
            loginReturn = True

        return loginReturn


    def accountInformations(self):

        # Get account info 

        account_info = MT.account_info()
        if account_info is None:
            print("There was issue with getting account information, error code =",MT.last_error())
            return None
        else:
            # Show account informations
            balance = account_info.balance
            profit = account_info.profit
            leverage = account_info.leverage
            currency = account_info.currency

            # Creating a dictionary to store the account information
            account_info = {
                "Balance": balance,
                "Profit": profit,
                "Leverage": leverage,
                "Currency": currency
            }

            accountInformationPd = pd.DataFrame([account_info])

            print("---------------- ==== ----------------")
            print(accountInformationPd)
            print("---------------- ==== ----------------")

            return accountInformationPd

    def getRealtimeData(symbol, timeframe, date_from ,date_to):

        print(timeframe)

        timeframe_mapping = {
            'M1': MT.TIMEFRAME_M1,
            'M5': MT.TIMEFRAME_M5,
            'M15': MT.TIMEFRAME_M15,
            'M30': MT.TIMEFRAME_M30,
            'H1': MT.TIMEFRAME_H1,
            'H4': MT.TIMEFRAME_H4
        }

        print(timeframe_mapping[timeframe])

        # Get information about prices
        
        prices = MT.copy_rates_range(symbol, timeframe_mapping[timeframe], date_from, date_to)
        prices = pd.DataFrame(prices)
        if prices is None or prices.empty:
            print("There was issue with collecting rates from MT5, error code =",MT.last_error())
            return None
        else:
            return prices
    
    def shutDownConnection():
        MT.shutdown()
        print("Connection shutdown..")

# obj = metaTrader(87838469, '@a5bTnOx', 'MetaQuotes-Demo')
# obj = metaTrader(10004883482, '8lVl-dGd', 'MetaQuotes-Demo')

# obj.accountInformations()
# obj.getRealtimeData("EURUSD",MT.TIMEFRAME_M1, dt(2024,11,5),dt.now())
# 10004883482  8lVl-dGd  investor: *p6jXpWy