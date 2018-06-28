from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
yf.pdr_override()
import datetime
from datetime import timedelta

# Present day
END_DATE = datetime.datetime.now().date()
# 5 years back
START_DATE = END_DATE - timedelta(days=1825)

def build_stock_dataset(companies):
    flag = False
    for company in companies:
        # Get all Adjusted Close prices for all the tickers in our list, between START_DATE and END_DATE
        all_data = pdr.get_data_yahoo(company, START_DATE, END_DATE)
        if(not all_data.empty):
            stock_data = all_data['Adj Close']
            # Remove any columns that hold no data, and print their tickers.
            #stock_data.dropna(how='all',inplace=True)
            stock_data.ffill(inplace=True)
            stock_data.to_csv('data/stock_prices/'+company+'.csv')
            flag = True
        else:
            flag = False
    return flag