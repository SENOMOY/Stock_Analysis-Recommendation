from tkinter import messagebox
from visualization.StockVisualization import generateTimeSeriesPlot
from prediction.LinearRegression import linearRegressionPrediction
from data.Yahoo_Finance_Data import build_stock_dataset

def generateReport(company_ticker,company):
	flag = build_stock_dataset([company_ticker])
	if flag:
		generateTimeSeriesPlot(company_ticker,company)
		linearRegressionPrediction(company_ticker,company)
	else:
		messagebox.showinfo('Error fetching data', 'No data available for ' + company)