import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import mean_absolute_error

# GET KNN - FIRST STEP OF ALGO

def calculate_KNN(data):
    data = calculate_pct_change(data)
    data = classify_trend(data)
    return data

## FUNCTIONS FOR KNN

def classify_trend(data):
    # Calculate treshold to specify "SIDEWAYS" using standard deviation for adjustment depending on instrument
    std_change = data['pct_change'].std()
    threshold = std_change * 0.5
    print(f"Calculated Threshold: {threshold}")

    # Define trend based on pct_change
    # data = data.copy()
    data['knn-trend'] = data['pct_change'].apply(lambda x: 'Downtrend' if x < -threshold else ('Uptrend' if x > threshold else 'Sideways'))
    data['KNN'] = data['knn-trend']
    # data1.loc[:,'Trend-KNN'] = trend
    # data.drop(['Trend'], axis=1, inplace=True)
    return data

def calculate_pct_change(data):
    # Calculate PCT-CHANGE for closed pas positions 
    data['pct_change'] = data['close'].pct_change() * 100
    data = data.dropna()
    return data


# GET EMA RIBON - SECOND STEP OF ALGO - SECOND CHECK - based on past data from plot

def calculate_EMA_RIBBON(data):
    # Define shorter EMA periods for scalping
    data, ema_periods = create_periods_EMA(data)
    check_conditions_EMA(data, ema_periods)

def create_periods_EMA(data):
    ema_periods = [3, 5, 8, 10, 12, 15]
    for period in ema_periods:
        data[f'EMA_{period}'] = data['close'].ewm(span=period, adjust=False).mean()
    return data, ema_periods

def check_conditions_EMA(data, ema_periods):
    # Find the midpoint - in this approach when there is odd number of elements first list will be always smaller
    midpoint = len(ema_periods) // 2

    # Split the list
    first_half_periods = ema_periods[:midpoint]
    second_half_periods = ema_periods[midpoint:]

    # The nested generator expression - creates cartesian product of all of the values in periods:
    for i in range(len(data)): 
        latest_data = data.iloc[i] # last generated value from data DataFrame
        is_uptrend = all(latest_data[f'EMA_{first}'] > latest_data[f'EMA_{second}'] for first in first_half_periods for second in second_half_periods)
        is_downtrend = all(latest_data[f'EMA_{first}'] < latest_data[f'EMA_{second}'] for first in first_half_periods for second in second_half_periods)
        data.loc[i, 'EMA_TREND_UPTREND'] = str(is_uptrend)


# GET RSI - THIRD STEP OF ALGO

def calculate_RSI(data, period):

    data['delta'] = data['close'].diff()

    # Separate gains and losses
    data['gain'] = data['delta'].apply(lambda x: x if x > 0 else 0)
    data['loss'] = data['delta'].apply(lambda x: -x if x < 0 else 0)
    
    # Calculate the average gains and losses
    data['avg_gain'] = data['gain'].rolling(window=period, min_periods=1).mean()
    data['avg_loss'] = data['loss'].rolling(window=period, min_periods=1).mean()

    # Calculate RS
    data['RS'] = data['avg_gain'] / data['avg_loss']

    # Calculate RSI
    data['RSI'] = 100 - (100 / (1 + data['RS']))

    # Drop not needed columns
    data.drop(['delta', 'gain', 'loss', 'avg_gain', 'avg_loss', 'RS'], axis=1, inplace=True)

    return data
  


