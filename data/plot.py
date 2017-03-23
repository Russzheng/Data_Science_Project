#Define No-show ratio: # of no-shows / total # of people
#Define Show-Up ratio: # of Show-Ups / total # of people
#Reference: https://www.kaggle.com/somrikbanerjee/d/joniarroba/noshowappointments/predicting-show-up-no-show
#Age,Gender,AppointmentRegistration,AppointmentData,GapofDays,DayOfTheWeek,Status,Diabetes,Alchoholism,
#Hypertension,Handicap,Smokes,Scholarship,Tuberculosis,Sms_Reminder


import numpy as np
import pandas as pds
import matplotlib.pyplot as plt
import scipy
from matplotlib import pylab
import seaborn as sns
data = pds.read_csv('clean_noshow.csv')

def main():
	#sns.set_style("whitegrid")
	#general_ratio()
	#age()
	#gapofDays()
	sns.set_style("white")
	#gender()
	dayoftheWeek_reg()

def probStatusLR(dataset, group_by):
    df = pds.crosstab(index = dataset[group_by], columns = dataset.Status).reset_index()
    df['probNoShow'] = df[0] / (df[1] + df[0])
    return df[[group_by, 'probNoShow']]

def probStatusBar(group_by):
    rows = []
    for item in group_by:
        for dp in data[item].unique():
            row = {'x': item}
            total = len(data[data[item] == dp])
            n = len(data[(data[item] == dp) & (data.Status == 0)])
            row.update({'Ratio': n / total, 'Hue': dp})
            rows.append(row)
    return pds.DataFrame(rows)

def age():
	sns.lmplot(data = probStatusLR(data, 'Age'), x = 'Age', y = 'probNoShow', fit_reg = True)
	sns.plt.xlim(0, 100)
	sns.plt.title('No-show ratio with respect to Age')
	sns.plt.show()

def gapofDays():
	sns.lmplot(data = probStatusLR(data, 'GapofDays'), x = 'GapofDays', y = 'probNoShow', fit_reg = True)
	sns.plt.title('No-show ratio with respect to GapofDays')
	sns.plt.show()

def gender():
	sns.barplot(data = probStatusBar(['Gender']),
            x = 'x', y = 'Ratio', hue = 'Hue', palette = 'Set1')
	sns.plt.title('No-show Ratio with respect to gender')
	sns.plt.xlabel('Gender')
	sns.plt.ylabel('No-show ratio')
	sns.plt.show()

def dayoftheWeek():
	sns.barplot(data = probStatusBar(['DayOfTheWeek']),
            x = 'x', y = 'Ratio', hue = 'Hue', palette = 'Set1')
	sns.plt.title('No-show Ratio with respect to Day of the Week')
	sns.plt.xlabel('Day of the Week')
	sns.plt.ylabel('No-show ratio')
	sns.plt.show()

def dayoftheWeek_reg():
	add_column()
	sns.barplot(data = probStatusBar(['DayOfTheWeekReg']),
            x = 'x', y = 'Ratio', hue = 'Hue', palette = 'Set1')
	sns.plt.title('No-show Ratio with respect to Day of the Week (Registration)')
	sns.plt.xlabel('Day of the Week')
	sns.plt.ylabel('No-show ratio')
	sns.plt.show()

def add_column():
	#Add columns day of week dfor registration
	li = []
	for index, row in data.iterrows():
		temp = (row['DayOfTheWeek'] - row['GapofDays']) % 7
		if temp == 0:
			temp = 7
		li.append(temp)
	data.insert(4, 'DayOfTheWeekReg', li)
	#print(data['DayOfTheWeekReg'].unique())
	
def general_ratio():
	#first calculate the general no-show ratio
	show_up = 0
	no_show = 0
	for item in data['Status']:
		if item:
			show_up += 1
		else:
			no_show += 1

	print ('No-show ratio is ', (no_show / (show_up + no_show)))

if __name__ == '__main__':
	main()

