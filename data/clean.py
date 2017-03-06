import pandas as pd

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

df.to_csv('clean_noshow.csv', mode = 'w', index=False)