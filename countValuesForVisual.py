
import numpy as numpy
import matplotlib.pyplot as plt 
import csv
import os

# Calculate all values and create a csv.
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

	numShowsWhenDiabetus = 0
	numNoShowsWhenDiabetus = 0

	numShowsWhenAlcohol = 0
	numNoShowsWhenAlcohol = 0

	numShowsWhenHyperTension = 0
	numNoShowsWhenHyperTension = 0

	numShowsWhenHandicap = 0
	numNoShowsWhenHandicap = 0

	numShowsWhenSmoke = 0
	numNoShowsWhenSmoke = 0

	numShowsWhenTuber = 0
	numNoShowsWhenTuber = 0

	totalSmsSent = 0
	totolSmsNotSent = 0
	statusIndex = 6 
	smsIndex = -2
	disbetesIndex = 7
	alcoholIndex = 8
	hyperTensionIndex = 9
	handicapIndex = 10
	smokeIndex = 11
	tuberIndex = 13


	for row in data:
		smsSent = int(row[smsIndex])
		status = int(row[statusIndex])
		diabetus = int(row[disbetesIndex])
		alcohol = int(row[alcoholIndex])
		hyperTension = int(row[hyperTensionIndex])
		handicap = int(row[handicapIndex])
		smoke = int(row[smokeIndex])
		tuber = int(row[tuberIndex])

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

		if status == 1 and diabetus == 1:
			numShowsWhenDiabetus += 1
		if status == 0 and diabetus == 1:
			numNoShowsWhenDiabetus += 1

		if status == 1 and alcohol == 1:
			numNoShowsWhenAlcohol += 1
		if status == 0 and alcohol == 1:
			numShowsWhenAlcohol += 1

		if status == 1 and hyperTension == 1:
			numShowsWhenHyperTension += 1
		if status == 0 and hyperTension == 1:
			numNoShowsWhenHyperTension += 1

		if status == 1 and handicap == 1:
			numNoShowsWhenHandicap += 1
		if status == 0 and handicap == 1:
			numShowsWhenHandicap += 1

		if status == 1 and smoke == 1:
			numShowsWhenSmoke += 1
		if status == 0 and smoke == 1:
			numNoShowsWhenSmoke += 1

		if status == 1 and tuber == 1:
			numNoShowsWhenTuber += 1
		if status == 0 and tuber == 1:
			numShowsWhenTuber += 1	

	os.unlink('./calc.csv')
	with open('./calc.csv','w') as f:
		writer = csv.writer(f)
		writer.writerow(['items','values'])
		writer.writerow(['Total no. of no-shows',numNoShowsInTotal])
		writer.writerow(['Total no. of Show-ups',numShowsInTotal])
		#writer.writerow(['No. of ',totolSmsNotSent])
		#writer.writerow(['totalSmsSent',totalSmsSent])
		
		writer.writerow(['No.of no-shows after SMSreminders',numNoShowsWhenSmsReminderSent])
		writer.writerow(['No.of show-ups after SMSreminders',numShowsWhenSmsReminderSent])

		writer.writerow(['No.of no-shows without SMSreminder',numNoShowsWhenSmsReminderNotSent])
		writer.writerow(['No.of show-ups without SMSreminder',numShowsWhenSmsReminderNotSent])

		writer.writerow(['No.of no-shows among diabetus patients',numNoShowsWhenDiabetus])
		writer.writerow(['No.of show-ups among diabetus patients',numShowsWhenDiabetus])
		
		writer.writerow(['No.of no-shows among alcoholic patients',numNoShowsWhenAlcohol])
		writer.writerow(['No.of show-ups among alcoholic patients',numShowsWhenAlcohol])

		
		writer.writerow(['No.of no-shows among patients with hypertension',numNoShowsWhenHyperTension])
		writer.writerow(['No.of show-ups among patients with hypertension',numShowsWhenHyperTension])

		writer.writerow(['No.of no-shows among handicap patients',numNoShowsWhenHandicap])
		writer.writerow(['No.of show-ups among handicap patients',numShowsWhenHandicap])
		
		writer.writerow(['No.of no-shows among patients who smoke',numNoShowsWhenSmoke])
		writer.writerow(['No.of show-ups among patients who smoke',numShowsWhenSmoke])

		writer.writerow(['No.of no-shows among patients with tuberculosis',numNoShowsWhenTuber])
		writer.writerow(['No.of show-ups among patients with tuberculosis',numShowsWhenTuber])

if __name__=="__main__":
	main()








