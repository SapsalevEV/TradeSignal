
class candls():
    def __init__(self):
        self.data = []

    #Функция для определения доджи
    def is_doji(self, candle):
        body_size = abs(candle['Open'] - candle['Close'])
        total_range = candle['High'] - candle['Low']

        if body_size <= total_range * 0.1:  # Параметр 0.1 может быть настроен в зависимости от вашего определения доджи
            return True
        else:
            return False

    #Функция для определения медвежьего поглощения
    def is_bearish_engulfing(self, candles):
        previous_candle = candles.iloc[-2]
        current_candle = candles.iloc[-1]

        if previous_candle['Open'] > previous_candle['Close'] and current_candle['Open'] < current_candle['Close'] and current_candle['Open'] > previous_candle['Close'] and current_candle['Close'] < previous_candle['Open']:
            return True
        else:
            return False

    #Функция для определения бычьего поглощения
    def is_bullish_engulfing(self, candles):
        previous_candle = candles.iloc[-2]
        current_candle = candles.iloc[-1]

        if previous_candle['Open'] < previous_candle['Close'] and current_candle['Open'] > current_candle['Close'] and current_candle['Open'] < previous_candle['Close'] and current_candle['Close'] > previous_candle['Open']:
            return True
        else:
            return False

    #Функция для определения молота
    def is_hammer(self, candle):
        body_size = abs(candle['Open'] - candle['Close'])
        total_range = candle['High'] - candle['Low']

        if body_size <= total_range * 0.3 and candle['Close'] > candle['Open'] and (candle['Close'] - candle['Low']) / (candle['High'] - candle['Low']) >= 0.7:
            return True
        else:
            return False

    #Функция для определения доджи-стрекоза (дракон)
    def is_dragonfly_doji(self, candle):
        body_size = abs(candle['Open'] - candle['Close'])
        total_range = candle['High'] - candle['Low']

        if body_size <= total_range * 0.1 and (candle['High'] - candle['Close']) / total_range <= 0.1:
            return True
        else:
            return False

    #Функция для определения доджи-надгробие
    def is_gravestone_doji(self, candle):
        body_size = abs(candle['Open'] - candle['Close'])
        total_range = candle['High'] - candle['Low']

        if body_size <= total_range * 0.1 and (candle['Open'] - candle['Low']) / total_range <= 0.1:
            return True
        else:
            return False

    #Функция для определения утренней звезды
    def is_morning_star(self, candles):
        previous_candle = candles.iloc[-3]
        middle_candle = candles.iloc[-2]
        current_candle = candles.iloc[-1]

        if previous_candle['Close'] < previous_candle['Open'] and  middle_candle['Close'] > previous_candle['Close'] and middle_candle['Open'] < previous_candle['Close'] and \
                current_candle['Open'] > middle_candle['Close'] and current_candle['Close'] > current_candle['Open'] and  current_candle['Close'] > middle_candle['Open']:
            return True
        else:
            return False
