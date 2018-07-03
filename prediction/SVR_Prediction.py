import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.svm import SVR

def getSVRPrediction(company_ticker,company):
	data = pd.read_csv("../data/stock_prices/"+company_ticker+".csv")
	data.columns = ['Date', 'Adj. Close']
	#Date
	date = []
	price = []
	for index, row in data.iterrows():
		price.append(float(row['Adj. Close']))
		date.append(row['Date'])

	date = range(len(data))
	date = np.reshape(date, (len(date), 1))

	# DATA PREDICTION
	# Initialise svr, fit the models, predict the model values kernel and specifies the kernel type used in algorithm
	# C is the error penalty, gamma is the kernel coefficient and degree is the polynomial degree in poly kernel
	svr_lin=SVR(kernel='linear',C=1e3,cache_size=7000)
	svr_poly=SVR(kernel='poly',C=1e3,degree=2,cache_size=7000)
	svr_rbf=SVR(kernel='rbf',C=1e3,gamma=0.1,cache_size=7000)
	print('1')
	svr_lin.fit(date,price)
	svr_poly.fit(date,price)
	svr_rbf.fit(date,price)
	print('2')
	# PLOT THE DATA ON THE GRAPH
	plt.scatter(date, price, color='black', label='data')
	plt.plot(date, svr_lin.predict(date), color='blue', label='Linear SVR')
	plt.plot(date, svr_poly.predict(date), color='red', label='Polynomial SVR')
	plt.plot(date, svr_rbf.predict(date), color='green', label='RBF SVR')
	plt.xticks(range(0, data.shape[0], 100), data['Date'].loc[::60], rotation=35)
	plt.xlabel('Dates')
	plt.ylabel('Price')
	#figManager = plt.get_current_fig_manager()
	#figManager.window.showMaximized()
	fig = plt.gcf()
	fig.canvas.set_window_title("Price Prediction (SVM)")
	plt.title(company)
	plt.legend()
	plt.show()
	print(svr_lin.predict(10)[0])
	print(svr_poly.predict(10)[0])
	print(svr_rbf.predict(10)[0])

#getSVRPrediction('AMZN','Amazon')


