
import pandas as pd 
import numpy as np 
from fbprophet import Prophet
import csv
import sys
import matplotlib.pyplot as pp

def createCsvForProphet(file):
	output = []
	with open(file) as f:
		reader = csv.reader(f)
		cols = ['ds','y']
		with open('./ds.csv','w') as out:
			writer = csv.writer(out)
			writer.writerow(cols)
			next(reader)
			for row in reader:
				date = row[3]
				sp = date.split('/')
				#print(sp)
				ds = '20' + sp[-1] + '-' + sp[0] + '-' + sp[1]
				ds = str(ds)
				status = float(row[4])
				if ds.startswith('2015'):
					writer.writerow([ds,status])

def main():
	file = './clean_noshow.csv'
	#createCsvForProphet(file)

	pfile = './ds.csv'
	df = pd.read_csv(pfile)
	df.sort_values(by='ds')
	#df[['Time', 'Product']].query('Product == p_id and start_time <= Time < end_time')
	
	print(df.head())

	
	#return
	#df.rename(columns={'ApointmentData': 'ds', 'Status':'y'}, inplace=True)
	#df = df[['ds','y']]
	df['y'] = np.array(df['y'])
	m = Prophet()
	
	m.fit(df);


	print('Data Fit already')
	future = m.make_future_dataframe(periods=10)

	print(future.tail())
	forecast = m.predict(future)

	m.plot(forecast)
	pp.show()
	#m.plot_components(forecast)




if __name__=="__main__":
	main()