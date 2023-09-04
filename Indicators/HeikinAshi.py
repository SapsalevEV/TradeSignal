import pandas as pd

def heikin_ashi(data):
    ha_close = (data['Open'] + data['High'] + data['Low'] + data['Close']) / 4
    ha_open = (data['Open'].shift() + data['Close'].shift()) / 2
    ha_high = data[['High', 'Open', 'Close']].max(axis=1)
    ha_low = data[['Low', 'Open', 'Close']].min(axis=1)

    data['HA_Open'] = ha_open
    data['HA_High'] = ha_high
    data['HA_Low'] = ha_low
    data['HA_Close'] = ha_close

    return data