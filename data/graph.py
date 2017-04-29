import numpy as np
import pandas as pds
import datetime
from datetime import date

def probStatusLR(dataset, group_by):
    df = pds.crosstab(index = dataset[group_by], columns = dataset.Status).reset_index()
    df['NoShowRatio'] = df[0] / (df[1] + df[0])
    return df[[group_by, 'NoShowRatio']]

df = pds.read_csv('graph.csv')
df = probStatusLR(df, 'AppointmentData')

li = []
li_2 = []
for index, row in df.iterrows():
	date1 = row['AppointmentData'].split('/')
	d1 = date(int(date1[2]), int(date1[1]), int(date1[0]) )
	li.append(d1.weekday() +  1)
	li_2.append(d1)
df = df.drop('AppointmentData', 1)
df.insert(1, 'AppointmentData', li_2)
df.insert(2, 'DayOfTheWeek', li)

df.to_csv('graph_groupby.csv', mode = 'w', index=False)

