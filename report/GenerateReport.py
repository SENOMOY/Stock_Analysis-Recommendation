from tkinter import messagebox
from visualization.StockVisualization import generateTimeSeriesPlot
from prediction.LinearRegression import linearRegressionPrediction
from data.Yahoo_Finance_Data import build_stock_dataset
from data.Twitter_Data import getSentimentResult

def generateReport(company_ticker,company):
	flag = build_stock_dataset([company_ticker])
	if flag:
		print('Running Time Series Analysis...')
		generateTimeSeriesPlot(company_ticker,company)
		print('Running Linear Regression Prediction...')
		linearRegressionPrediction(company_ticker,company)
		print('Running Sentiment Analysis...')
		getSentimentResult(company)
	else:
		messagebox.showinfo('Error fetching data', 'No data available for ' + company)