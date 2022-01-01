import ta
import pandas as pd
from finta import TA

df_btc = pd.read_csv('datasets/bitcoin_data.csv', parse_dates=True)


# parabolic sar
def psar_value(dataframe):
    parabolic_sar_obj = ta.trend.PSARIndicator(df_btc['High'], df_btc['Low'], df_btc['Close'], step=2, max_step=2)
    return parabolic_sar_obj.psar()


print(psar_value(df_btc))


# kaufman ama
def calculate_kama(dataframe):
    number_of_period = 20
    number_of_fastest_EMA_constant = 2
    number_of_slowest_EMA_constant = 3
    kama_obj = ta.momentum.KAMAIndicator(dataframe['Close'], number_of_period, number_of_fastest_EMA_constant,
                                         number_of_slowest_EMA_constant)
    return kama_obj.kama()


calculate_kama(df_btc)


# ichimoku cloud
def calculate_senkou_Span_A(dataframe):
    low_period = 20
    medium_period = 60
    high_period = 120
    Ichimoku_obj = ta.trend.IchimokuIndicator(dataframe['High'], dataframe['Low'], low_period, medium_period,
                                              high_period)
    return Ichimoku_obj.ichimoku_a()


calculate_senkou_Span_A(df_btc)


def calculate_senkou_Span_B(dataframe):
    low_period = 20
    medium_period = 60
    high_period = 120
    Ichimoku_obj = ta.trend.IchimokuIndicator(dataframe['High'], dataframe['Low'], low_period, medium_period,
                                              high_period)
    return Ichimoku_obj.ichimoku_b()


calculate_senkou_Span_B(df_btc)


def calculate_ichimoku_base_line(dataframe):
    low_period = 20
    medium_period = 60
    high_period = 120
    Ichimoku_obj = ta.trend.IchimokuIndicator(dataframe['High'], dataframe['Low'], low_period, medium_period,
                                              high_period)
    return Ichimoku_obj.ichimoku_base_line()


calculate_ichimoku_base_line(df_btc)


def calculate_ichimoku_conversion_line(dataframe):
    low_period = 20
    medium_period = 60
    high_period = 120
    Ichimoku_obj = ta.trend.IchimokuIndicator(dataframe['High'], dataframe['Low'], low_period, medium_period,
                                              high_period)
    return Ichimoku_obj.ichimoku_conversion_line()


calculate_ichimoku_conversion_line(df_btc)


# VFI
def calculate_vfi(dataframe):
    dataframe.columns = map(str.lower, dataframe.columns)
    dataframe_new = dataframe[['high', 'open', 'low', 'close', 'volume (currency)']]
    dataframe_new.rename(columns={'volume (currency)': 'volume'}, inplace=True)
    return TA.VFI(dataframe_new)


calculate_vfi(df_btc)


# Leledc Exhausion
def Leledc_Exhausion(dataframe):
    return 0
