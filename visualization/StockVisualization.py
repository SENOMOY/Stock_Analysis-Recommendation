import matplotlib.pyplot as plt
import pandas as pd
from data.Yahoo_Finance_Data import build_stock_dataset

def generateTimeSeriesPlot(company_ticker,company):
    build_stock_dataset([company_ticker])
    data = pd.read_csv("data/stock_prices/"+company_ticker+".csv")
    time = pd.to_datetime(data.iloc[:, 0])
    price = data.iloc[:, 1]
    fig = plt.gcf()
    fig.canvas.set_window_title(company)
    plt.title(company)
    plt.plot(time,price)
    plt.interactive(False)
    plt.show(block=True)