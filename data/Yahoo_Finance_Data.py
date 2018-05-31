from pandas_datareader import data as pdr
import fix_yahoo_finance as yf
yf.pdr_override()
import datetime
from datetime import timedelta

END_DATE = datetime.datetime.now().date()
START_DATE = END_DATE - timedelta(days=365)

def build_stock_dataset(companies,start,end):
    for company in companies:
        # Get all Adjusted Close prices for all the tickers in our list, between START_DATE and END_DATE
        all_data = pdr.get_data_yahoo(company, start, end)
        stock_data = all_data['Adj Close']
        # Remove any columns that hold no data, and print their tickers.
        #stock_data.dropna(how='all', axis=1, inplace=True)
        stock_data.ffill(inplace=True)
        stock_data.to_csv('STOCK_PRICES/'+company+'.csv')


#build_stock_dataset(['AMZN','MSFT'],START_DATE,END_DATE)