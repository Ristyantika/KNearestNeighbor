import csv
import random
import math
import operator

data = [[1, 2, 3, 4, 'first'],
        [2, 3, 4, 5, 'second'],
        [3, 1, 5, 6, 'second'],
        [4, 5, 6, 7, 'fourth'],
        [5, 6, 7, 8, 'second']]
 
def loadDataset(fold, kfold, dataset, trainingSet=[] , testSet=[]):
    kfold = kfold * len(dataset) / fold
    #print kfold
    awal = kfold - (1*len(dataset)/fold)
    #print awal
    for x in range(len(data)):
        if x >= awal and x < kfold:
            testSet.append(dataset[x])
        else:
            trainingSet.append(dataset[x]) 
            
def euclideanDistance(instance1, instance2, length):
    distance = 0
    for x in range(length):
        distance += pow((instance1[x] - instance2[x]), 2)
    return math.sqrt(distance)
    
def getNeighbors(trainingSet, testInstance, k):
    distances = []
    # ada -1 soalnya kolom terakhir itu class
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    #sort berdasarkan pada list ke 1 yaitu berdasarkan pada dist yang terpendek 
    # list ke 0 adalah datanya
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    for x in range(k):
        neighbors.append(distances[x][0])
    #print neighbors
    #data sebanyak k yang telah di sort dan disimpan di list neighbor
    return neighbors

def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        #print response
        #pada list neighbor dihitung prediksi kelas terbayak dari k data 
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    #print sortedVotes[0][0]
    return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/len(testSet)) * 100
    
    
def main():
    # prepare data
    kfold_val = 0
    fold = 5
    for s in range(5):
        #print s+1
        trainingSet=[]
        testSet=[]
        loadDataset(fold, s+1, data, trainingSet, testSet)
        #print 'Train set: ' + repr(len(trainingSet))
        #print 'Test set: ' + repr(len(testSet))
        predictions = []
        k = 3
        for x in range(len(testSet)):
            neighbors = getNeighbors(trainingSet, testSet[x], k)
            result = getResponse(neighbors)
            predictions.append(result)
            print('> predicted=' + repr(result) + ', actual=' + repr(testSet[x][-1]))
        accuracy = getAccuracy(testSet, predictions)
        print('Accuracy: ' + repr(accuracy) + '%')
        kfold_val = kfold_val + accuracy
        
    kfold_val = kfold_val / fold
    print('Last Accuracy: ' + repr(kfold_val) + '%')
        
	
main()