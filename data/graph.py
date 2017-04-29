import numpy as np
import pandas as pds

def probStatusLR(dataset, group_by):
    df = pds.crosstab(index = dataset[group_by], columns = dataset.Status).reset_index()
    df['NoShowRatio'] = df[0] / (df[1] + df[0])
    return df[[group_by, 'NoShowRatio']]

df = pds.read_csv('graph.csv')
df = probStatusLR(df, 'AppointmentData')

df.to_csv('graph_groupby.csv', mode = 'w', index=False)

