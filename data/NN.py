import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'
import numpy
import pandas
from keras.models import Sequential
from keras.layers import Dense
from keras.wrappers.scikit_learn import KerasClassifier
from sklearn.model_selection import cross_val_score
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

def normalization(X):
    temp = []
    mean_arr = numpy.mean(X, axis=0) 
    std_arr = numpy.std(X, axis=0) 
    for row in X:
        temp.append((row - mean_arr) / std_arr)
    temp = numpy.array(temp).astype('float32')
    return temp

# fix random seed for reproducibility
seed = 7
numpy.random.seed(seed)

# load dataset
df = pandas.read_csv('for_review.csv')
df = df[df.DayOfTheWeek != 7]
sample_size = 10000
# split into input (X) and output (Y) variables
features_train = df[['Age', 'DayOfTheWeek', 'Diabetes', 'Hypertension', 'Smokes',
                             'Handicap', 'Alchoholism', 'Scholarship', 'Sms_Reminder']].iloc[:sample_size]
features_train.to_csv('temp_1.csv', header=False, index=False)
features_train = pandas.read_csv('temp_1.csv')
features_train = features_train.values
features_train = features_train.astype('float32')
features_train = normalization(features_train)

labels_train = df.Status[:sample_size]
labels_train.to_csv('temp_2.csv', header=False, index=False)
labels_train = pandas.read_csv('temp_2.csv')

labels_train = numpy.array(labels_train)
labels_train = numpy.ravel(labels_train)

# baseline model
def create_baseline():
	# create model
	model = Sequential()
	model.add(Dense(12, input_dim=9, kernel_initializer='normal', activation='relu'))
	model.add(Dense(6, kernel_initializer='normal', activation='relu'))
	model.add(Dense(1, kernel_initializer='normal', activation='sigmoid'))
	# Compile model
	model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
	return model

estimators = []
estimators.append(('standardize', StandardScaler()))
estimators.append(('mlp', KerasClassifier(build_fn=create_baseline, epochs=100, batch_size=10, verbose=0)))
pipeline = Pipeline(estimators)
kfold = StratifiedKFold(n_splits=10, shuffle=True, random_state=seed)
results = cross_val_score(pipeline, features_train, labels_train, cv=kfold)
print('Training size:', sample_size)
print("Standardized: %.2f%% (%.2f%%)" % (results.mean()*100, results.std()*100))

os.remove('temp_1.csv')
os.remove('temp_2.csv')