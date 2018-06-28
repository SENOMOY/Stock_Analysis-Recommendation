import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn import preprocessing

def linearRegressionPrediction(company_ticker,company):
	data = pd.read_csv("data/stock_prices/"+company_ticker+".csv")
	data.columns = ['Date', 'Adj. Close']
	data = data[['Adj. Close']]
	forecast_out = int(30)  # predicting 30 days into future
	data['Prediction'] = data.shift(-forecast_out)  # label column with data shifted 30 units up
	x = np.array(data.drop(['Prediction'], 1))
	x = preprocessing.scale(x)
	x_forecast = x[-forecast_out:]  # set X_forecast equal to last 30
	x = x[:-forecast_out]  # remove last 30 from X
	y = np.array(data['Prediction'])
	y = y[:-forecast_out]
    # Split train and test data
	x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)
	# Training
	clf = LinearRegression()
	clf.fit(x_train, y_train)
	# Testing
	confidence = clf.score(x_test, y_test)
	print("Confidence: ", confidence)
    # predict our x_forecast
	forecast_prediction = clf.predict(x_forecast)
	print("Next 30 days prediction prices")
	for price in forecast_prediction:
		print(price)
	# Plot
	fig = plt.gcf()
	fig.canvas.set_window_title("Price Prediction")
	plt.title(company)
	plt.plot(forecast_prediction)
	plt.ylabel('Projected Price')
	plt.xlabel('Days')
	plt.show()