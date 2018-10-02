import pandas as pd
from sklearn.model_selection import StratifiedKFold
import math
from operator import itemgetter
from sklearn.metrics import mean_squared_error

dataset = pd.read_csv('abalon.csv', header=None)
rows, columns = dataset.shape
print columns
data = list(dataset[0])
data = pd.get_dummies(data)
del dataset[0]
dataset = pd.concat([data, dataset], axis=1)

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
k_nn = 5
skf = StratifiedKFold(n_splits=n_split)
for train_index, test_index in skf.split(dataset, target_data):
    X_train, X_test = dataset[train_index], dataset[test_index]
    y_train, y_test = target_data[train_index], target_data[test_index]
    result = []
    for i in range(len(X_test)):
        distances = []
        for j in range(len(X_train)):
            distance = 0
            for l in range(columns-1):
                distance += pow((X_test[i][l]-X_train[j][l]),2)
#            print y_train[j]
            distances.append((y_train[j], math.sqrt(distance)))
        sortedVotes = sorted(distances, key=operator.itemgetter(1))
#        sortedVotes = pd.DataFrame(sortedVotes)
        output = 0
        for i in range(k_nn):
#            print sortedVotes[i][0]
            output += sortedVotes[i][0]
        output = output / k_nn
        result.append(output)
    rms = math.sqrt(mean_squared_error(y_test, result))
    print rms
        
        
            
            
    
        
        