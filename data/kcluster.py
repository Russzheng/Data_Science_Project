import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
import pandas as pds
import math

def probStatusLR(dataset, group_by):
    df = pds.crosstab(index = dataset[group_by], columns = dataset.Status).reset_index()
    df['probNoShow'] = df[0] / (df[1] + df[0])
    return df[[group_by, 'probNoShow']]

df = pds.read_csv("clean_noshow.csv")
k1 = probStatusLR(df, 'Age')
'''
count = df['Age'].value_counts().reset_index()
count.columns = ['Age', 'count']
count = count.sort('Age', ascending=True)
count.to_csv(r'result.txt', index=None, sep=' ', mode='a')
'''
num = 5
kmeans_model = KMeans(n_clusters=5, random_state=1)

kmeans_model.fit(k1)
labels = kmeans_model.labels_

print('kmeans score:')
score = -kmeans_model.score(k1)
print(score)
average = score / 300000
print('Average distance of samples to their nearest clustering center:')
print(average)

'''
#PCA plotting
pca_2 = PCA(2)
plot_columns = pca_2.fit_transform(k1)
plt.scatter(x=plot_columns[:,0], y=plot_columns[:,1], c=labels)
plt.show()
'''

#Targeted plotting
x = 'Age'
y = 'probNoShow'

plt.scatter(x=k1[x], y=k1[y], c=labels)
plt.title('5-cluster')
plt.xlabel('Age')
plt.ylabel('No-show Ratio')
plt.show()

'''
k1.to_csv('kcluster.csv')
df = pds.read_csv("kcluster.csv")
df['color'] = labels
df.to_csv('final.csv')
'''