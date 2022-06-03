#!/usr/bin/env python3
""" Available functions to scrape data
 when needed from Financial modeling Prep."""
import requests
import pandas as pd


def get_income_statement(ticker, limit, key, period):
    """Get the Income Statement."""
    URL = 'https://financialmodelingprep.com/api/v3/income-statement/'
    try:
        r = requests.get(
            '{}{}?period={}&limit={}&apikey={}'.format(URL,
                                                       ticker,
                                                       period,
                                                       limit,
                                                       key))
        incomeStatement = pd.DataFrame.from_dict(r.json()).transpose()
        incomeStatement.columns = incomeStatement.loc['fillingDate']
        return incomeStatement
    except requests.exceptions.HTTPError as e:
        # We want a 200 value
        print('Requesting Income statement sheet ERROR: ', str(e))


def get_balance_sheet(ticker, limit, key, period):
    """Get the Balance sheet."""
    URL = 'https://financialmodelingprep.com/api/v3/balance-sheet-statement/'
    try:
        r = requests.get(
            '{}{}?period={}&?limit={}&apikey={}'.format(URL,
                                                        ticker,
                                                        period,
                                                        limit,
                                                        key))
        balanceSheet = pd.DataFrame.from_dict(r.json()).transpose()
        balanceSheet.columns = balanceSheet.loc['fillingDate']
        return balanceSheet
    except requests.exceptions.HTTPError as e:
        # We want a 200 value
        print('Requesting Balance sheet statement ERROR: ', str(e))


def get_cash_flow_statement(ticker, limit, key, period):
    """Get the Cash flow statements."""
    URL = 'https://financialmodelingprep.com/api/v3/cash-flow-statement/'
    try:
        r = requests.get(
            '{}{}?period={}&?limit={}&apikey={}'.format(URL,
                                                        ticker,
                                                        period,
                                                        limit,
                                                        key))
        cashFlow = pd.DataFrame.from_dict(r.json()).transpose()
        cashFlow.columns = cashFlow.loc['fillingDate']
        return cashFlow
    except requests.exceptions.HTTPError as e:
        print('Requesting Cash flow statement ERROR: ', str(e))


def get_market_capital(ticker, key):
    URL = 'https://financialmodelingprep.com/api/v3/market-capitalization/'
    try:
        r = requests.get(
            '{}{}?apikey={}'.format(URL,
                                    ticker,
                                    key))
        # mcap = pd.DataFrame.from_dict(r.json()).transpose()
        return r.json()[0]['marketCap']
    except requests.exceptions.HTTPError as e:
        print('Requesting Market capitalization ERROR: ', str(e))


def get_full_financial_statement_as_reported(ticker, key, period):
    URL = 'https://financialmodelingprep.com/api/v3/financial-statement-full-as-reported/'
    try:
        r = requests.get(
            '{}{}?period={}&apikey={}'.format(URL,
                                              ticker,
                                              period,
                                              key))
        full_statement = pd.DataFrame.from_dict(r.json()).transpose()
        # full_statement.columns = full_statement.loc['fillingDate']
        return full_statement
    except requests.exceptions.HTTPError as e:
        print('Requesting full financial statement ERROR: ', str(e))


def get_quote(ticker, key):
    """Getting the current quote of the company."""
    URL = 'https://financialmodelingprep.com/api/v3/quote/'
    try:
        r = requests.get('{}{}?apikey={}'.format(URL,
                                                 ticker,
                                                 key))
        quote = pd.DataFrame.from_dict(r.json()).transpose()
        return(quote)
    except requests.exceptions.HTTPError as e:
        print('Requesting quote estimate ERROR: ', str(e))


def get_industry_multiples():
    """Getting the Industry Multiples value from NYU. """
    URL = 'http://pages.stern.nyu.edu/~adamodar/New_Home_Page/datafile/vebitda.html'
    html = requests.get(URL).content
    df_list = pd.read_html(html)
    df = df_list[-1]
    df.columns = df.iloc[1]
    df = df.drop(1)
    df['Industry Name'][0] = 'Category'
    df.iloc[0][0] = 'Category'
    df = df.set_index(df['Industry Name'])
    del df['Industry Name']
    return df
