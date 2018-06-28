import matplotlib.pyplot as plt
import pandas as pd

def generateTimeSeriesPlot(company_ticker,company):
    data = pd.read_csv("data/stock_prices/"+company_ticker+".csv")
    data.columns = ['Date', 'Adj. Close']
    fig = plt.gcf()
    fig.canvas.set_window_title("Time series plot")
    plt.title(company)
    plt.plot(range(data.shape[0]), data['Adj. Close'])
    plt.xticks(range(0, data.shape[0], 100), data['Date'].loc[::60], rotation=35)
    plt.xlabel('Date', fontsize=15)
    plt.ylabel('Price', fontsize=15)
    plt.show()