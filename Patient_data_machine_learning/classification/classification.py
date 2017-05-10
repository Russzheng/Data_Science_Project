#CLASSIFIERS.

import numpy as np
import pandas as pds
import math
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.svm import LinearSVR
from sklearn.svm import SVR
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
import sklearn.svm
import optunity
import optunity.metrics
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier
from sklearn.multiclass import OneVsRestClassifier

#Age,Gender,AppointmentRegistration,AppointmentData,GapofDays,DayOfTheWeek,Status,Diabetes,
#Alchoholism,Hypertension,Handicap,Smokes,Scholarship,Tuberculosis,Sms_Reminder

df = pds.read_csv("../data/clean_noshow.csv")
df = df.drop('GapofDays', 1)
df = df.drop('Gender', 1)
df = df.drop('AppointmentRegistration', 1)
df = df.drop('AppointmentData', 1)
df = df[df.DayOfTheWeek != 7]

for sample_size in [150000, 170000, 200000, 210000, 230000, 250000, 270000, 290000]:
    print('Sample size is: ', sample_size)

    features_train = df[['Age', 'DayOfTheWeek', 'Diabetes', 'Hypertension', 'Smokes',
                             'Handicap', 'Alchoholism', 'Scholarship', 'Sms_Reminder']].iloc[:sample_size]
    labels_train = df.Status[:sample_size]

    features_test = df[['Age', 'DayOfTheWeek', 'Diabetes', 'Hypertension', 'Smokes',
                             'Handicap', 'Alchoholism', 'Scholarship', 'Sms_Reminder']].iloc[sample_size:]
    labels_test = df.Status[sample_size:]

    features_train = features_train.astype('float32')
    features_test = features_test.astype('float32')

    lr = LogisticRegression().fit(features_train, labels_train)
    print('Accuracy for Logistic Regression:', accuracy_score(labels_test, lr.predict(features_test)))
    print(len(lr.predict(features_test)) - np.count_nonzero(lr.predict(features_test)))

    gnb =  GaussianNB().fit(features_train, labels_train)
    print('Accuracy for GaussianNB:', accuracy_score(labels_test, gnb.predict(features_test), 2))
    print(len(gnb.predict(features_test)) - np.count_nonzero(gnb.predict(features_test)))

    clf =  MultinomialNB().fit(features_train, labels_train)
    print('Accuracy for MultinomialNB:', accuracy_score(labels_test, clf.predict(features_test), 2))
    print(len(clf.predict(features_test)) - np.count_nonzero(clf.predict(features_test)))
    
    linear_svc = LinearSVC().fit(features_train, labels_train)
    print('Accuracy for linear SVC:', accuracy_score(labels_test, linear_svc.predict(features_test), 2))
    print(len(linear_svc.predict(features_test)) - np.count_nonzero(linear_svc.predict(features_test)))

    rf = RandomForestClassifier(n_jobs=2)
    rf.fit(features_train, labels_train)
    print('Accuracy for Random Forest:', accuracy_score(labels_test, rf.predict(features_test), 2))
    print(len(rf.predict(features_test)) - np.count_nonzero(rf.predict(features_test)))

    #Parameter tuning in SVM using bagging classifier and onevsrest classifier.
    '''svc = SVC().fit(features_train, labels_train)
    print('Accuracy for SVC:', accuracy_score(labels_test, svc.predict(features_test), 2))
    print(len(linear_svc.predict(features_test)) - np.count_nonzero(svc.predict(features_test)))'''
    '''
    n_estimators = 10
    bsvc = OneVsRestClassifier(BaggingClassifier(SVC(kernel='linear'), max_samples=1.0 / n_estimators, n_estimators=n_estimators))
    bsvc.fit(features_train, labels_train)
    print('Accuracy for Bagging SVC:', accuracy_score(labels_test, bsvc.predict(features_test), 2))'''


    print('\n')

df.to_csv('for_review.csv', mode = 'w', index=False)