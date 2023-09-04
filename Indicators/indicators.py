import pandas as pd

class indicator():
    def __init__(self):
        data = []

    def calculate_mfi(self, high, low, close, volume, period=14):
        typical_price = (high + low + close) / 3
        raw_money_flow = typical_price * volume

        positive_flow = []
        negative_flow = []

        for i in range(1, len(typical_price)):
            if typical_price[i] > typical_price[i - 1]:
                positive_flow.append(raw_money_flow[i - 1])
                negative_flow.append(0)
            elif typical_price[i] < typical_price[i - 1]:
                negative_flow.append(raw_money_flow[i - 1])
                positive_flow.append(0)
            else:
                positive_flow.append(0)
                negative_flow.append(0)

        positive_flow = positive_flow[-period:]
        negative_flow = negative_flow[-period:]

        positive_money_flow = sum(positive_flow)
        negative_money_flow = sum(negative_flow)

        money_ratio = positive_money_flow / negative_money_flow if negative_money_flow != 0 else 0

        mfi = 100 - (100 / (1 + money_ratio))

        return mfi

    def calculate_sma(self, data, period):
        sma_values = []

        for i in range(period - 1, len(data)):
            sma = sum(data[i - period + 1:i + 1]) / period
            sma_values.append(sma)

        return sma_values

    def calculate_ema(self, data, period):
        ema_values = []

        multiplier = 2 / (period + 1)
        ema = sum(data[:period]) / period
        ema_values.append(ema)

        for i in range(period, len(data)):
            ema = (data[i] - ema) * multiplier + ema
            ema_values.append(ema)

        return ema_values