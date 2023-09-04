import pandas as pd
import numpy as np

def super_trend(data, period=10, multiplier=3):
    # Вычисление True Range (TR) и Average True Range (ATR)
    data['High-Low'] = data['High'] - data['Low']
    data['High-PreviousClose'] = np.abs(data['High'] - data['Close'].shift())
    data['Low-PreviousClose'] = np.abs(data['Low'] - data['Close'].shift())
    data['TR'] = data[['High-Low', 'High-PreviousClose', 'Low-PreviousClose']].max(axis=1)
    data['ATR'] = data['TR'].rolling(period).mean()

    # Вычисление верхней и нижней полосы Супер Тренда
    data['UpperBand'] = data['High'] + multiplier * data['ATR']
    data['LowerBand'] = data['Low'] - multiplier * data['ATR']

    # Определение направления тренда
    data['Trend'] = 0
    data.loc[data['Close'] > data['UpperBand'], 'Trend'] = 1
    data.loc[data['Close'] < data['LowerBand'], 'Trend'] = -1

    # Определение сигналов покупки и продажи
    data['Signal'] = 0
    data.loc[data['Trend'].shift() == -1, 'Signal'] = 1
    data.loc[data['Trend'].shift() == 1, 'Signal'] = -1

    return data