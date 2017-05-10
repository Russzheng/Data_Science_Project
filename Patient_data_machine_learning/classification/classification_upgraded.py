#AN UPGRADE CLASSIFICATION
#WITH NORMALIZATION
#COMPOSITE SCORE OF MERGED DATA

import numpy as np
import pandas as pds
import math
import os
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
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier

#Age,Gender,AppointmentRegistration,AppointmentData,GapofDays,DayOfTheWeek,Status,Diabetes,
#Alchoholism,Hypertension,Handicap,Smokes,Scholarship,Tuberculosis,Sms_Reminder
#def add_twitter(X):
    #for row in X:

def normalization(X):
    temp = []
    mean_arr = np.mean(X, axis=0) 
    std_arr = np.std(X, axis=0) 
    for row in X:
        temp.append((row - mean_arr) / std_arr)
    temp = np.array(temp).astype('float32')
    return temp

df = pds.read_csv("clean_noshow.csv")
df = df[df.DayOfTheWeek != 7]

def add_column():
    #Add columns day of week dfor registration
    li = []
    for index, row in df.iterrows():
        temp = (row['DayOfTheWeek'] - row['GapofDays']) % 7
        if temp == 0:
            temp = 7
        li.append(temp)
    df.insert(4, 'DayOfTheWeekReg', li)
    #print(data['DayOfTheWeekReg'].unique())
add_column()

def add_column_time():
    #Add columns time of the day of registration
    count = 0
    li = []
    for index, row in df.iterrows():
        li.append(row['AppointmentRegistration'][-5:-3])
        if row['AppointmentRegistration'][-5:-3] == '22': #'05':
            count += 1
    df.insert(4, 'TimeOfDay', li)
    #print(type(row['AppointmentRegistration'][-5:-3]))
    print(count)
    for index, row in df.iterrows():
        if row['TimeOfDay'] == '05' or row['TimeOfDay'] == '22':
            df.drop(index, inplace=True)
    df['TimeOfDay'] = df['TimeOfDay'].map({'06': 6, '07': 7, '08': 8, '09': 9,
    '10': 10, '11': 11, '12': 12, '13': 13, '14': 14, '15': 15, '16': 16, '17': 17,
    '18': 18, '19': 19, '20': 20, '21': 21, '22': 22})

#add_column_time()

df = df.drop('GapofDays', 1)
df = df.drop('Gender', 1)
df = df.drop('AppointmentRegistration', 1)
df = df.drop('AppointmentData', 1)

#Add composite score.
li = []
for index, row in df.iterrows():
    sentiment = 0
    week = row['DayOfTheWeek']
    if week == 1:
        sentiment = 3.524851242562128117e-01
    elif week == 2:
        sentiment = 3.548204587825241063e-01
    elif week == 3:
        sentiment = 3.797136754988987284e-01
    elif week == 4:
        sentiment = 3.684030205565654859e-01
    elif week == 5:
        sentiment = 3.520065997332023078e-01
    else:
        sentiment = 3.758207041268361026e-01
    li.append(sentiment)

df.insert(4, 'Sentiment', li)

for sample_size in [150000, 170000, 200000, 210000, 230000, 250000, 270000, 290000]:
    print('Sample size is: ', sample_size)

    features_train = df[['Age', 'DayOfTheWeek', 'Diabetes', 'Hypertension', 'Smokes',
                             'Handicap', 'Alchoholism', 'Scholarship']].iloc[:sample_size]
    features_train.to_csv('temp_1.csv', header=False, index=False)
    features_train = pds.read_csv('temp_1.csv')
    features_train = features_train.values
    features_train = features_train.astype('float32')
    
    labels_train = df.Status[:sample_size]
    labels_train.to_csv('temp_2.csv', header=False, index=False)
    labels_train = pds.read_csv('temp_2.csv')
    labels_train = np.array(labels_train)
    labels_train = np.ravel(labels_train)

    features_test = df[['Age', 'DayOfTheWeek', 'Diabetes', 'Hypertension', 'Smokes',
                             'Handicap', 'Alchoholism', 'Scholarship']].iloc[sample_size:]
    features_test.to_csv('temp_3.csv', header=False, index=False)
    features_test = pds.read_csv('temp_3.csv')
    features_test = features_test.values
    features_test = features_test.astype('float32')

    
    labels_test = df.Status[sample_size:]
    labels_test.to_csv('temp_4.csv', header=False, index=False)
    labels_test = pds.read_csv('temp_4.csv')
    labels_test = np.array(labels_test)
    labels_test = np.ravel(labels_test)

    features_train = normalization(features_train)
    features_test = normalization(features_test)

    lr = LogisticRegression().fit(features_train, labels_train)
    print('Accuracy for Logistic Regression:', accuracy_score(labels_test, lr.predict(features_test)))
    print(len(lr.predict(features_test)) - np.count_nonzero(lr.predict(features_test)))

    gnb =  GaussianNB().fit(features_train, labels_train)
    print('Accuracy for GaussianNB:', accuracy_score(labels_test, gnb.predict(features_test), 2))
    print(len(gnb.predict(features_test)) - np.count_nonzero(gnb.predict(features_test)))

    #multinomial does not accept negative values, we can use sk learn's preprocessing or normaliza instead.
    '''clf =  MultinomialNB().fit(features_train, labels_train)
    print('Accuracy for MultinomialNB:', accuracy_score(labels_test, clf.predict(features_test), 2))
    print(len(clf.predict(features_test)) - np.count_nonzero(clf.predict(features_test)))'''

    
    linear_svc = LinearSVC().fit(features_train, labels_train)
    print('Accuracy for linear SVC:', accuracy_score(labels_test, linear_svc.predict(features_test), 2))
    print(len(linear_svc.predict(features_test)) - np.count_nonzero(linear_svc.predict(features_test)))
    '''
    rf = RandomForestClassifier(n_jobs=2)
    rf.fit(features_train, labels_train)
    print('Accuracy for Random Forest:', accuracy_score(labels_test, rf.predict(features_test), 2))
    print(len(rf.predict(features_test)) - np.count_nonzero(rf.predict(features_test)))
    
    dt = DecisionTreeClassifier()
    dt.fit(features_train, labels_train)
    print('Accuracy for Decision Tree:', accuracy_score(labels_test, dt.predict(features_test), 2))
    print(len(rf.predict(features_test)) - np.count_nonzero(dt.predict(features_test)))
    
    kn = KNeighborsClassifier()
    kn.fit(features_train, labels_train)
    print('Accuracy for K nearest neighbor:', accuracy_score(labels_test, kn.predict(features_test), 2))
    print(len(rf.predict(features_test)) - np.count_nonzero(kn.predict(features_test)))
    
    svc = SVC().fit(features_train, labels_train)
    print('Accuracy for SVC:', accuracy_score(labels_test, svc.predict(features_test), 2))
    print(len(linear_svc.predict(features_test)) - np.count_nonzero(svc.predict(features_test)))
    
    n_estimators = 10
    bsvc = OneVsRestClassifier(BaggingClassifier(SVC(kernel='linear'), max_samples=1.0 / n_estimators, n_estimators=n_estimators))
    bsvc.fit(features_train, labels_train)
    print('Accuracy for Bagging SVC:', accuracy_score(labels_test, bsvc.predict(features_test), 2))'''


    print('\n')

df.to_csv('for_review.csv', mode = 'w', index=False)
os.remove('temp_1.csv')
os.remove('temp_2.csv')
os.remove('temp_3.csv')
os.remove('temp_4.csv')