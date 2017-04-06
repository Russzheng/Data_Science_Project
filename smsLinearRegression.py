import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import scipy
from matplotlib import pylab
import seaborn 
data = pd.read_csv('clean_noshow.csv')

def main():
	awaitingTimePlot()
	seaborn.set_style("white")

def linearRegression(d, group_by):
    df = pd.crosstab(index = d[group_by], columns = d.Status).reset_index()
    df['LinearReg'] = df[0] / (df[1] + df[0])
    return df[[group_by, 'LinearReg']]

def awaitingTimePlot():
	seaborn.lmplot(data = linearRegression(data, 'Sms_Reminder'), x = 'Sms_Reminder', y = 'LinearReg', fit_reg = True)
	seaborn.plt.ylim(0, 1.1)
	seaborn.plt.title('No show ratio Vs Sms_Reminder')
	seaborn.plt.show()



if __name__ == '__main__':
	main()

