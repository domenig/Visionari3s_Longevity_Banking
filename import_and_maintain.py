############################################
#### IMPORTS:                           ####
############################################
import numpy as np
import pandas as pd
import csv
import datetime as dt
from datetime import datetime
from datetime import date, timedelta
import time
import os
import io
import requests
import yfinance as yf



############################################
#### FUNCTIONS:                         ####
############################################


###############
### FUNCTION 1: Buy/Hold/Sell Recommendation Puller ###
###############

def get_recommendation_data(tickers):
    """
    This function retrieves the Buy/Hold/Sell recommendations for each specific ticker from Yahoo Finance

    Input Parameters:
    tickers:    list of tickers
    """
    recommendations = []

    for ticker in tickers:
        lhs_url = 'https://query2.finance.yahoo.com/v10/finance/quoteSummary/'
        rhs_url = '?formatted=true&crumb=swg7qs5y9UP&lang=en-US&region=US&' \
                'modules=upgradeDowngradeHistory,recommendationTrend,' \
                'financialData,earningsHistory,earningsTrend,industryTrend&' \
                'corsDomain=finance.yahoo.com'
                
        url =  lhs_url + ticker + rhs_url
        r = requests.get(url)
        if not r.ok:
            recommendation = 6
        try:
            result = r.json()['quoteSummary']['result'][0]
            recommendation =result['financialData']['recommendationMean']['fmt']
        except:
            recommendation = 6
        
        recommendations.append(recommendation)
        
        print("--------------------------------------------")
        print ("{} has an average recommendation of: ".format(ticker), recommendation)
        #time.sleep(0.5)
        
    last_recommendation = recommendation

    recommendation_df = pd.DataFrame(list(zip(tickers, recommendations)), columns =['Company', 'Recommendations']) 
    recommendation_df = recommendation_df.set_index('Company')
    recommendation_df.to_csv('recommendations.csv')
    return recommendation_df, last_recommendation



###############
### FUNCTION 2: OHLC (Open-High-Low-Close) Data Puller ###
###############

def get_OHLC_data(tickers, start_date = None, end_date = None):
    """
    This function retrieves the OHLC (Open-High-Low-Close) data for a given time span from Yahoo Finance

    Input Parameters:
    tickers:    list of tickers
    start_date: starting date from which onwards the data gets pulled   (format: YYYY-MM-DD)
    end_date:   ending date up until which the data gets pulled         (format: YYYY-MM-DD)
    """
    OHLC_df = pd.DataFrame()            # create an empty df for the final OHLC data
    for ticker in tickers:              # iterate through all tickers and pull the OHLC data
        OHLC_ticker_df = pd.DataFrame()     # create an empty df for the tickers OHLC data
        yf_ticker = yf.Ticker(ticker)       # initiate the pull from the API

        if(start_date != None and end_date != None):        # IF    we have a time frame with start and end date
            OHLC_ticker_df = yf_ticker.history(start = start_date, end = end_date, interval = "1d")

        elif(start_date != None):                           # IF    we have only a start date
            OHLC_ticker_df = yf_ticker.history(start = start_date, end = date.today(), interval = "1d")

        elif(end_date != None):                             # IF    we have only an end date
            OHLC_ticker_df = yf_ticker.history(start = "1990-01-01", end = end_date, interval = "1d")

        else:                                               # IF    no time span is given
            OHLC_ticker_df = yf_ticker.history(period = "max", interval = "1d")

        OHLC_ticker_df.insert(0, "Ticker", ticker)      # insert the ticker to retrieved data

        OHLC_df = OHLC_df.append(OHLC_ticker_df)        # append the retrieved information to the final OHLC dataframe

    OHLC_df.reset_index(inplace=True)                           # reset the indexes after all ticker information got appended
    OHLC_df.set_index(['Date','Ticker'], inplace=True)          # initiate the the indexes newly
    return OHLC_df          # return the final OHLC dataframe


###############
### FUNCTION 3: Date Puller ###
###############

def get_todays_data(OHLC_df_file):
    """
    This functions retrieves the existing OHLC file each day and adds the values of the newly day to the file

    Input Parameters:
    OHLC_df_file:   existing csv file to which the daily data should be added to
    """
    old_OHLC_df = pd.read_csv(OHLC_df_file)                             # loading the csv file with the old OHLC data
    old_OHLC_df['Date'] = pd.to_datetime(old_OHLC_df['Date'])           # convert the date column to a datetime column
    last_date = max(old_OHLC_df['Date'])                                # get the last date for which records are existing
    #old_OHLC_df['Date'] = old_OHLC_df['Date'].date                      # convert the datetime column to date
    #old_OHLC_df.reset_index(inplace=True)                           # reset the indexes after all ticker information got appended
    old_OHLC_df.set_index(['Date','Ticker'], inplace=True)          # initiate the the indexes newly
    return last_date, old_OHLC_df                       # return the last date for which we have records as well as the updated dataframe with the datatime column





###############
### FUNCTION 4: Call / Update Data Puller (MAIN INTEGRATION) ###
###############

def call_update_data(tickers, OHLC_df_file):

    today = date.today()                                # getting info for today
    tomorrow = today + timedelta(1)                     # getting info for tomorrow

    if os.path.isfile(OHLC_df_file):                                                                    # check if there is already data saved and a csv file exists
        path = str(os.getcwd()) + "\\" + OHLC_df_file
        last_date, OHLC_df = get_todays_data(OHLC_df_file=OHLC_df_file)                                 # get the latest date for which data is existing as well as the existing df

        if last_date == today:                          # if the last information is todays information, new new information will be added
            pass
            os.remove(path)
        else:                                           # otherwise there is new data to add to the dataframe
            missing_data = get_OHLC_data(tickers=tickers, start_date=last_date, end_date=tomorrow)      # get data for the missing dates
            OHLC_df = OHLC_df.append(missing_data)                                                      # append the data from the missing dates to the original dataframe
            OHLC_df.reset_index(inplace=True)                                                           # reset the indexes after all ticker information got appended
            OHLC_df.drop_duplicates(subset=["Date","Ticker"], keep='first')
            OHLC_df = OHLC_df[OHLC_df['Ticker'].notna()]                             # drop duplicates if there are any with the same symbol and date
            OHLC_df.set_index(["Date","Ticker"], inplace=True)                                          # initiate the the indexes newly
            os.remove(path)

    else:
        OHLC_df = get_OHLC_data(tickers=tickers)                          # newly create the csv file (if not existing) & push all the information in the CSV file

    OHLC_df.to_csv(OHLC_df_file, mode="w", index=True)                    # create the adapted or newly created csv file (mode="W" for write)
    return OHLC_df










































    





























