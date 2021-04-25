############################################
#### IMPORTS:                           ####
############################################
import numpy as np
import pandas as pd
from import_and_maintain import *
from key_indicators import *
from investing_merge_backend import *



############################################
#### LAUNCHING APP:                     ####
############################################

# Calling app_start to launch service
app_start()



############################################
#### THE PAGE:                          ####
############################################

###############
### FUNCTION 1: Portfolio Definition ###
###############
tickers_portfolio_1 = ['ICLN', 'XETRA', 'IRBT', 'LRCX', 'INTU', 'BLK']          # ESG
tickers_portfolio_2 = ['NVDA', 'POOL', 'CRM', 'ADBE', 'FIX', 'INTUIT']          # ESG
tickers_portfolio_3 = ['WST', 'VRTX', 'BBY', 'HD', 'IDXX', 'SPDR']              # ESG
tickers_portfolio_4 = ['ADBE', 'RTX', 'CIG', 'UNH', 'MDT', 'IQV']               # ESG
tickers_portfolio_5 = ['JPM', 'JNJ', 'VISA', 'BMY', 'BHC', 'CISCO']
tickers_portfolio_6 = ['BRK', 'AMZN', 'VISA', 'BLK', 'WALMART', 'MA']
tickers_portfolio_7 = ['PEP', 'BAX', 'GE', 'GOLD', 'DAL', 'AAL']
tickers_portfolio_8 = ['NKE', 'CMCSA', 'TSLA', 'MRK', 'CME', 'PYPL']
tickers_portfolio_9 = ['AAPL', 'MSFT', 'DIS', 'GS', 'OCGN', 'DHR']
tickers_portfolio_10 = ['TWTR', 'FB', 'SBUX', 'COIN', 'ADRS', 'ASML']



###############
### FUNCTION 2: Running and Updating OHLC Data ###
###############
# run as an example the main integration with AAPL and MSFT and save it as the portfolio_1.csv
portfolio_1_df = call_update_data(tickers=tickers_portfolio_1, OHLC_df_file = "portfolio_1.csv")
portfolio_2_df = call_update_data(tickers=tickers_portfolio_2, OHLC_df_file = "portfolio_2.csv")
portfolio_3_df = call_update_data(tickers=tickers_portfolio_3, OHLC_df_file = "portfolio_3.csv")
portfolio_4_df = call_update_data(tickers=tickers_portfolio_4, OHLC_df_file = "portfolio_4.csv")
portfolio_5_df = call_update_data(tickers=tickers_portfolio_5, OHLC_df_file = "portfolio_5.csv")
portfolio_6_df = call_update_data(tickers=tickers_portfolio_6, OHLC_df_file = "portfolio_6.csv")
portfolio_7_df = call_update_data(tickers=tickers_portfolio_7, OHLC_df_file = "portfolio_7.csv")
portfolio_8_df = call_update_data(tickers=tickers_portfolio_8, OHLC_df_file = "portfolio_8.csv")
portfolio_9_df = call_update_data(tickers=tickers_portfolio_9, OHLC_df_file = "portfolio_9.csv")
portfolio_10_df = call_update_data(tickers=tickers_portfolio_10, OHLC_df_file = "portfolio_10.csv")


###############
### FUNCTION 3: Running Function for additional Key Indicators ###
###############
portfolio_1_w_indicators, portfolio_1_indicator_df = key_indicators_df(portfolio_1_df)
portfolio_2_w_indicators, portfolio_2_indicator_df = key_indicators_df(portfolio_2_df)
portfolio_3_w_indicators, portfolio_3_indicator_df = key_indicators_df(portfolio_3_df)
portfolio_4_w_indicators, portfolio_4_indicator_df = key_indicators_df(portfolio_4_df)
portfolio_5_w_indicators, portfolio_5_indicator_df = key_indicators_df(portfolio_5_df)
portfolio_6_w_indicators, portfolio_6_indicator_df = key_indicators_df(portfolio_6_df)
portfolio_7_w_indicators, portfolio_7_indicator_df = key_indicators_df(portfolio_7_df)
portfolio_8_w_indicators, portfolio_8_indicator_df = key_indicators_df(portfolio_8_df)
portfolio_9_w_indicators, portfolio_9_indicator_df = key_indicators_df(portfolio_9_df)
portfolio_10_w_indicators, portfolio_10_indicator_df = key_indicators_df(portfolio_10_df)


#print("Portfolio with Indicators:",portfolio_2_w_indicators)                   for testing purposes of function 2
#print("Indicator DF:",portfolio_2_indicator_df)                                for testing purposes of function 3