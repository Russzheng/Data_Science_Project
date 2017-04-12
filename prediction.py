import pandas as pd
import numpy as np
import datetime
import matplotlib.pyplot as plt

from sklearn.ensemble import GradientBoostingClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import cross_val_score
import os
import csv

def splitTheDataForTrainingAndTest():
	file = './clean_noshow.csv'
	trainFile = './training_noshow.csv'
	testFile = './test_noshow.csv'
	with open(file) as f:
		reader = csv.reader(f)
		header = next(reader)
		count = 200000

		with open(trainFile,'w') as train:
			with open(testFile,'w') as test:
				trainWriter = csv.writer(train)
				testWriter = csv.writer(test)
				trainWriter.writerow(header)
				testWriter.writerow(header)
				i = 0
				for row in reader:
					if i <= count:
						trainWriter.writerow(row)
					else:
						testWriter.writerow(row)
					i += 1

def trainAndTestData():
	# Read the dataset for training
	dataset = pd.read_csv('./training_noshow.csv')
	dataset = dataset.drop(['AppointmentRegistration', 'ApointmentData','GapofDays','AwaitingTime'], 1)
	dataset = pd.get_dummies(dataset)
	dfidx = dataset.dropna('index')
	dfcol = dataset.dropna('columns')

	# Set up the training
	#print(dataset.head())
	msk = np.random.rand(len(dfcol)) < 0.8
	dftrain = dfcol[msk]
	dftest = dfcol[~msk]
	xtrain = dftrain.drop('Status', 1).astype(int).as_matrix()
	ytrain = dftrain['Status'].astype(int).as_matrix()
	clfGB = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=1, 
                                   random_state=0)

	clfGB.fit(xtrain, ytrain, sample_weight=[i*1+1 for i in ytrain])

	# Training mean accuracy
	print('Training mean Accuracy')
	print(clfGB.score(xtrain,ytrain))

	# Cross-validation.
	print("Mean and std deviation for cross validation score")
	cross_valid_score = cross_val_score(clfGB,xtrain,ytrain,scoring='accuracy')
	print("Mean:",cross_valid_score.mean())
	print("Std deviation:",cross_valid_score.std())


	# Test the model.
	testdataset = pd.read_csv('./test_noshow.csv')
	testdataset = testdataset.drop(['AppointmentRegistration', 'ApointmentData','GapofDays','AwaitingTime'], 1)
	testdataset = pd.get_dummies(testdataset)
	dfidx = testdataset.dropna('index')
	dfcol = testdataset.dropna('columns')

	# Set up the training
	#print(dataset.head())
	msk = np.random.rand(len(dfcol)) < 0.8
	dftrain = dfcol[msk]
	dftest = dfcol[~msk]
	xtest = dftrain.drop('Status', 1).astype(int).as_matrix()
	ytest = dftrain['Status'].astype(int).as_matrix()
	predictions = clfGB.predict(xtest)
	print('')
	print("Predicted the patient no-show Status")
	print(predictions)
	print('Predicted mean accuracy:')
	score = clfGB.score(xtest,ytest)
	print(score)
	

	confusion_mat = confusion_matrix(predictions, ytest)
	precision = confusion_mat[1,1] / float(confusion_mat[1,1] + confusion_mat[1,0])
	recall = confusion_mat[1,1] / float(confusion_mat[1,1] + confusion_mat[0,1])

	print('Confusion Matrix:')
	print(confusion_mat)

	print('Precision:')
	print(precision)

	print('Recall:')
	print(recall)


def main():

	trainFile = './training_noshow.csv'
	testFile = './test_noshow.csv'

	if not os.path.exists(trainFile):
		splitTheDataForTrainingAndTest()

	trainAndTestData()
	




if __name__=="__main__":
	main()