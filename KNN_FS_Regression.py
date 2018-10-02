import pandas as pd
from sklearn.model_selection import StratifiedKFold

#def euclideanDistance(test_att, train_att, columns):
#    distance = 0
#    print test_att

def getNeighbor(test_att, X_train, y_train, test_out, column):
    print test_att
#    for j in range(len(X_train)):
#        distance = euclideanDistance(test_att, X_train[j])
#        listDistance.append(distance)

#def testSet(X_train, X_test, y_train, y_test, columns):
#    print X_test[0]
#    for i in range(len(X_test)):
#        print i
#        getNeighbor(X_test[i], X_train, y_train, y_test[i], columns)
    
def testSets(X_train, X_test, y_train, y_test, column):
#    print columns
     for i in range(len(X_test)):
#        print X_test[i]
        getNeighbor(X_test[i], X_train, y_train, y_test[i], column)

def crossValidation(dataset, target_data, column):
    skf = StratifiedKFold(n_splits=5)
    for train_index, test_index in skf.split(dataset, target_data):
        X_train, X_test = dataset[train_index], dataset[test_index]
        y_train, y_test = target_data[train_index], target_data[test_index]
        testSets(X_train, X_test, y_train, y_test, column)

#read File Dataset
dataset = pd.read_csv('iris.csv', skiprows=[0], header=None)
rows, columns = dataset.shape
target_data = dataset[columns-1]
del dataset[columns-1]

dataset = dataset.values
crossValidation(dataset,target_data, columns-1)



