############################################
#### IMPORTS:                           ####
############################################
import numpy as np
import pandas as pd
from import_and_maintain import *


############################################
#### FUNCTIONS:                         ####
############################################

###############
### FUNCTION 1: Key Indicator Puller ###
###############

def key_indicators_df(portfolio):
    
    portfolio_w_indicators = pd.DataFrame()
    indicator_df = pd.DataFrame()

    index_lst = len(portfolio)
    index_lst = list(range(index_lst))
    index_lst = [x+1 for x in index_lst]
    portfolio.reset_index(inplace=True)
    portfolio.set_index([index_lst])
    
    ticker_lst = portfolio['Ticker'].tolist()
    ticker_lst = [x for x in ticker_lst if x != 'nan']
    ticker_lst = list(dict.fromkeys(ticker_lst))

    for i in ticker_lst:
        k = 0                                                               # specify the row which is targeted in this iteration
        subset = portfolio[portfolio['Ticker'] == i]                        # select a subset of the currently selected ticker
        subset = subset.tail(756)                                           # select a subset of three years to get the three year trend
        subset['Close_shifted'] = subset.Close.shift(periods=1)                                             # reference the previous days closing price
        subset['Trend'] = (subset['Close'] - subset['Close_shifted']) / subset['Close_shifted'] * 100       # make the percentage change (trend) calculation

        trend_lst_3y = subset['Trend'].tolist()                                        # converge the column of trends to a list
        trend_lst_3y = trend_lst_3y[1:]                                                         # drop NaN elements of list as no trend could be calculated for that one as there was no preceding value accessible
        trend_3y = sum(trend_lst_3y)                                                 # calculate the product of all trends to get an overall scale


        subset = subset.tail(252)                                           # only select the previous years records (usually around 253 days a year the stock markets are open)

        subset['Close_shifted'] = subset.Close.shift(periods=1)                                             # reference the previous days closing price
        subset['Trend'] = (subset['Close'] - subset['Close_shifted']) / subset['Close_shifted'] * 100       # make the percentage change (trend) calculation

        trend_lst_1y = []
        trend_lst_1y = subset['Trend'].tolist()                                         # converge the column of trends to a list
        trend_lst_1y = trend_lst_1y[1:]                                                 # drop NaN elements of list as no trend could be calculated for that one as there was no preceding value accessible
        trend_1y = sum(trend_lst_1y)                                                    # calculate the product of all trends to get an overall scale

        subset['Volatility'] = np.std(subset.Trend)                                                         # standard deviation als volatility
        annualized_volatility = subset['Volatility'].mean() * 252 ** 0.5                                    # calculate the annualized volatility

        recommendation_df, last_recommendation = get_recommendation_data([i])             # get the recommendaiton of the ticker

        curr_indicator_df = pd.DataFrame(columns=['Ticker','One_Year_Trend', 'Three_Year_Trend', 'Annualized Volatility', 'Recommendations'])           # initiate the indicator df and specify the column names
        curr_indicator_df.loc[k] = [i, trend_1y, trend_3y, annualized_volatility, last_recommendation]                                                  # fill the tickers data in the indicator df

        indicator_df = indicator_df.append(curr_indicator_df)               # add newly created indicator df to other indicators, where each ticker is grouped to only one record 
        portfolio_w_indicators = portfolio_w_indicators.append(subset)      # add newly created subset with the indicators to the portfolio with indicators
        k += 1                                                              # for next iteration

    return portfolio_w_indicators, indicator_df














