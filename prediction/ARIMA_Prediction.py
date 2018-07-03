import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.stattools import acf, pacf
import statsmodels.tsa.stattools as ts
from statsmodels.tsa.arima_model import ARIMA

def getARIMAPrediction(company_ticker,company):
	data = pd.read_csv("../data/stock_prices/"+company_ticker+".csv")
	data.columns = ['Date', 'Adj. Close']
	price = data['Adj. Close']
	lnprice = np.log(price)
	print(lnprice)
	plt.plot(lnprice)
	plt.show()
	# ACF plot
	acf_1 = acf(lnprice)[1:20]
	plt.plot(acf_1)
	plt.show()
	test_df = pd.DataFrame([acf_1]).T
	test_df.columns = ['Pandas Autocorrelation']
	test_df.index += 1
	test_df.plot(kind='bar')
	# PACF PLot
	pacf_1 = pacf(lnprice)[1:20]
	plt.plot(pacf_1)
	plt.show()
	test_df = pd.DataFrame([pacf_1]).T
	test_df.columns = ['Pandas Partial Autocorrelation']
	test_df.index += 1
	test_df.plot(kind='bar')
	result = ts.adfuller(lnprice, 1)
	print(result)
	lnprice_diff = lnprice - lnprice.shift()
	diff = lnprice_diff.dropna()
	acf_1_diff = acf(diff)[1:20]
	test_df = pd.DataFrame([acf_1_diff]).T
	test_df.columns = ['First Difference Autocorrelation']
	test_df.index += 1
	test_df.plot(kind='bar')
	pacf_1_diff = pacf(diff)[1:20]
	plt.plot(pacf_1_diff)
	plt.show()
    # ARIMA Model Generation
	price_matrix = lnprice.as_matrix()
	model = ARIMA(price_matrix, order=(0, 1, 0))
	model_fit = model.fit(disp=0)
	#print(model_fit.summary())
	# ARIMA Predictions
	predictions = model_fit.predict(122, 127, typ='levels')
	print(predictions)
	predictionsadjusted = np.exp(predictions)
	print(predictionsadjusted)
	# Plot Predictions
	plt.plot(predictionsadjusted)
	plt.title(company)
	fig = plt.gcf()
	fig.canvas.set_window_title("Price Prediction (ARIMA)")
	#figManager = plt.get_current_fig_manager()
	#figManager.window.showMaximized()
	plt.show()

#getARIMAPrediction('AMZN','Amazon')