from tkinter import messagebox
from analysis.TimeSeriesPlot import generateTimeSeriesPlot
from prediction.LinearRegression_Prediction import linearRegressionPrediction
from prediction.LSTM_Prediction import lstmPrediction
from data.Yahoo_Finance_Data import build_stock_dataset
from data.Twitter_Data import getSentimentResult

def generateReport(company_ticker,company):
	flag = build_stock_dataset([company_ticker])
	if flag:
		print('Running Time Series Analysis...')
		generateTimeSeriesPlot(company_ticker,company)
		print('Running Linear Regression Prediction...')
		linearRegressionPrediction(company_ticker,company)
		print('Running LSTM Prediction...')
		lstmPrediction(company_ticker,company)
		print('Running Sentiment Analysis...')
		getSentimentResult(company)
	else:
		messagebox.showinfo('Error fetching data', 'No data available for ' + company)