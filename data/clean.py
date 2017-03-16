import pandas as pd
from datetime import date

df = pd.read_csv("No-show-Issue-Comma-300k.csv")

#Cleaning AwaitingTime
df['AwaitingTime'] = -df['AwaitingTime']

#Cleaning Status
df['Status'] = df['Status'].map({'Show-Up': 1, 'No-Show': 0})

#Cleaning DayOfTheWeek
df['DayOfTheWeek'] = df['DayOfTheWeek'].map({'Monday': 1, 'Tuesday': 2, 'Wednesday': 3, 'Thursday': 4,
	'Friday': 5, 'Saturday': 6, 'Sunday': 7})

#Cleaning ApointmentData
df['ApointmentData'] = df['ApointmentData'].map(lambda x: str(x)[:-10])

#Cleaning AppointmentRegistration
df['AppointmentRegistration'] = df['AppointmentRegistration'].map(lambda x: str(x)[:-4])

#Add columns days inbetween
li = []
for index, row in df.iterrows():
	date1 = row['AppointmentRegistration'].split('-')
	date2 = row['ApointmentData'].split('-')
	d1 = date(int(date1[0]), int(date1[1]), int(date1[2][0:2]))
	d2 = date(int(date2[0]), int(date2[1]), int(date2[2]))
	delta = d2 - d1
	li.append(delta.days)
df.insert(4, 'GapofDays', li)

#rename typos
df.rename(columns = {'ApointmentData':'AppointmentData',
                         'Alcoolism': 'Alchoholism',
                         'HiperTension': 'Hypertension',
                         'Handcap': 'Handicap'}, inplace = True)

df.to_csv('clean_noshow.csv', mode = 'w', index=False)





'''
d0 = date(2008, 8, 18)
d1 = date(2008, 9, 26)
delta = d0 - d1
print delta.days
df.insert(idx, col_name, value)
'''