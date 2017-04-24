import numpy as np
import pandas as pds
import math
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

#Age,Gender,AppointmentRegistration,AppointmentData,GapofDays,DayOfTheWeek,Status,Diabetes,
#Alchoholism,Hypertension,Handicap,Smokes,Scholarship,Tuberculosis,Sms_Reminder

df = pds.read_csv("clean_noshow.csv")
df = df.drop('GapofDays', 1)
df = df.drop('Gender', 1)
df = df.drop('AppointmentRegistration', 1)
df = df.drop('AppointmentData', 1)

for sample_size in [150000, 170000, 200000, 210000, 230000, 250000, 270000, 290000]:
	print('Sample size is: ', sample_size)

	features_train = df[['Age', 'DayOfTheWeek', 'Diabetes', 'Hypertension', 'Tuberculosis', 'Smokes',
	                         'Handicap', 'Alchoholism', 'Scholarship', 'Sms_Reminder']].iloc[:sample_size]
	labels_train = df.Status[:sample_size]

	features_test = df[['Age', 'DayOfTheWeek', 'Diabetes', 'Hypertension', 'Tuberculosis', 'Smokes',
	                         'Handicap', 'Alchoholism', 'Scholarship', 'Sms_Reminder']].iloc[sample_size:]
	labels_test = df.Status[sample_size:]
	
	gnb =  GaussianNB().fit(features_train, labels_train)
	print('Accuracy for GaussianNB:', accuracy_score(labels_test, gnb.predict(features_test), 2))

	clf =  MultinomialNB().fit(features_train, labels_train)
	print('Accuracy for MultinomialNB:', accuracy_score(labels_test, clf.predict(features_test), 2))

