import simfin as sf
from simfin.names import *
from datetime import timedelta
import pandas as pd
import matplotlib.pyplot as plt

import os
import sys

sys.path.append('..')
simfin_api_key = 'df7a5fa0-176f-4273-827f-7d7cd158f736'
sf.set_data_dir('~/simfin_data/')

def get_fundamental_data(asset_ticker): 
    # Setting API key in config
    sf.config.set_api_key(api_key=simfin_api_key)

    # Setting market as US and the stock ticker
    market = 'us'
    stock_ticker = asset_ticker

    # Fetching data in bulk for all stocks
    income_data_all_stocks = sf.load_income(variant='quarterly', market=market)
    balance_sheet_data_all_stocks = sf.load_balance(variant='quarterly', market=market)
    cash_flow_data_all_stocks = sf.load_cashflow(variant='quarterly', market=market)

    # Picking data for our specific ticker
    income_data_asset_ticker = income_data_all_stocks.loc[stock_ticker,:]
    balance_sheet_data_asset_ticker = balance_sheet_data_all_stocks.loc[stock_ticker,:]
    cash_flow_data_asset_ticker = cash_flow_data_all_stocks.loc[stock_ticker,:]

    return income_data_asset_ticker, balance_sheet_data_asset_ticker, cash_flow_data_asset_ticker
