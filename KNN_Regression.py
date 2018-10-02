import pandas as pd
from sklearn.model_selection import StratifiedKFold
import math

dataset = pd.read_csv('iris.csv', skiprows=[0], header=None)
rows, columns = dataset.shape
print columns
target_data = dataset[columns-1]
del dataset[columns-1]

target_data = pd.DataFrame(target_data)
dataset = dataset.values
target_data = target_data.values

X_train =[]
X_test = []
y_train = []
y_test = []
n_split = 5
skf = StratifiedKFold(n_splits=n_split)
for train_index, test_index in skf.split(dataset, target_data):
    X_train, X_test = dataset[train_index], dataset[test_index]
    y_train, y_test = target_data[train_index], target_data[test_index]
    for i in range(len(X_test)):
        distances = []
        for j in range(len(X_train)):
            distance = 0
            for l in range(columns-1):
                distance += pow((X_test[i][l]-X_train[j][l]),2)
            distances.append((y_train[j], math.sqrt(distance)))
    
        
        