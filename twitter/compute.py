#Computes basic information about the cleaned data, like average and standard deviation for 
#positive and negative sentiment as well as the ratio of positive average to negative average

import csv
import numpy

#word = "hospital appointment"
#word = "hospital"
word = "appointment"

day_of_week = {"Sun": 0, "Mon": 1, "Tue": 2, "Wed": 3, "Thu":4, "Fri": 5, "Sat": 6}
pos_values = [[],[],[],[],[],[],[]]
neg_values = [[],[],[],[],[],[],[]]
no_show_percentage = numpy.array([0.166667,0.297960,0.289112,0.296207,0.307858,0.321309,0.368270])

with open("/Users/khsia/Desktop/finalproject/" + word+".csv", 'rb') as infile:
  reader = csv.DictReader(infile)
  for row in reader:
    try:
      day = day_of_week[row['date'][0:3]]
      positive = float(row['positive'])
      negative = float(row['negative'])
      pos_values[day].append(positive)
      neg_values[day].append(negative)
    except:
      pass

  pos_values = numpy.array(pos_values)
  neg_values = numpy.array(neg_values)

  pos_week_average = numpy.zeros(len(day_of_week))
  pos_week_std = numpy.zeros(len(day_of_week))
  neg_week_average = numpy.zeros(len(day_of_week))
  neg_week_std = numpy.zeros(len(day_of_week))
  for i in range(0,len(day_of_week)):
    pos_week_average[i] = numpy.mean(pos_values[i])
    pos_week_std[i] = numpy.std(pos_values[i])
    neg_week_average[i] = numpy.mean(neg_values[i])
    neg_week_std[i] = numpy.std(neg_values[i])
  ratio_average = numpy.divide(pos_week_average, neg_week_average)
  


  output = numpy.column_stack((pos_week_average, pos_week_std, neg_week_average, neg_week_std, ratio_average, no_show_percentage))
  numpy.savetxt(
    word + "_computed.csv", 
    output, 
    delimiter=',', 
    header="Positive Average,Positive Standard Deviation,Negative Average,Negative Standard Deviation,Positive-to-Negative Ratio Average,Percent No Show", 
    comments="")

  print "Positive Average"
  print pos_week_average
  print "Positive Standard Deviation"
  print pos_week_std
  print "Negative Average"
  print neg_week_average
  print "Negative Standard Deviation"
  print neg_week_std
  print "Positive Average/Negative Average Ratio"
  print ratio_average

  