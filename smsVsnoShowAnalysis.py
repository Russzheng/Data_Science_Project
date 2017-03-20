
import numpy as numpy
import matplotlib.pyplot as plt 
import csv

def main():
	data = []
	try:
		with open('./clean_noshow.csv','r') as f:
			reader = csv.reader(f)
			next(reader)
			for row in reader:
				data.append(row)
	except:
		print("Exception occurred")

	numNoShowsWhenSmsReminderSent = 0
	numShowsWhenSmsReminderSent = 0
	numNoShowsWhenSmsReminderNotSent = 0
	numShowsWhenSmsReminderNotSent = 0
	numNoShowsInTotal = 0
	numShowsInTotal = 0
	totalSmsSent = 0
	totolSmsNotSent = 0
	statusIndex = 6 
	smsIndex = -2
	for row in data:
		smsSent = int(row[smsIndex])
		status = int(row[statusIndex])

		if status == 0:
			numNoShowsInTotal += 1
		if status == 1:
			numShowsInTotal += 1
		if smsSent == 1:
			totalSmsSent += 1
		if smsSent == 0:
			totolSmsNotSent += 1
		if smsSent == 1 and status == 1:
			numShowsWhenSmsReminderSent += 1
		if smsSent == 1 and status == 0:
			numNoShowsWhenSmsReminderSent += 1
		if smsSent == 0 and status == 0:
			numNoShowsWhenSmsReminderNotSent += 1
		if smsSent == 0 and status == 1:
			numShowsWhenSmsReminderNotSent += 1


	print('Finished processing')

	print('numNoShowsInTotal', numNoShowsInTotal)
	print('numShowsInTotal',numShowsInTotal)
	print('totolSmsNotSent',totolSmsNotSent)
	print('totalSmsSent',totalSmsSent)
	print('numShowsWhenSmsReminderSent',numShowsWhenSmsReminderSent)
	print('numNoShowsWhenSmsReminderSent',numNoShowsWhenSmsReminderSent)
	print('numNoShowsWhenSmsReminderNotSent',numNoShowsWhenSmsReminderNotSent)
	print('numShowsWhenSmsReminderNotSent',numShowsWhenSmsReminderNotSent)



if __name__=="__main__":
	main()








