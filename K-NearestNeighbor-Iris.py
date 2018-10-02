import csv
import random
import math
import operator
    
def crossVal(kf, kfold, dataset, trainingSet=[] , testSet=[]):
    kfold = kfold * len(dataset) / kf
    awal = kfold - (1*len(dataset)/kf)
    for x in range(len(dataset)):
        for y in range(4):
                dataset[x][y] = float(dataset[x][y])
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
    length = len(testInstance)-1
    for x in range(len(trainingSet)):
        dist = euclideanDistance(testInstance, trainingSet[x], length)
        distances.append((trainingSet[x], dist))
    distances.sort(key=operator.itemgetter(1))
    neighbors = []
    
    for x in range(k):
        neighbors.append(distances[x][0])
#    print neighbors
    return neighbors

def getResponse(neighbors):
    classVotes = {}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedVotes[0][0]

def getAccuracy(testSet, predictions):
    correct = 0
    for x in range(len(testSet)):
        if testSet[x][-1] == predictions[x]:
            correct += 1
    return (correct/float(len(testSet))) * 100.0

def main():
    # prepare data
    kfold_val = 0
    kf = 5
    with open('iris.txt', 'rb') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
    for s in range(5):
        #print s+1
        trainingSet=[]
        testSet=[]
        crossVal(kf, s+1, dataset, trainingSet, testSet)
        predictions = []
        k = 3
        for x in range(len(testSet)):
            neighbors = getNeighbors(trainingSet, testSet[x], k)
            result = getResponse(neighbors)
            predictions.append(result)
        accuracy = getAccuracy(testSet, predictions)
        print('Accuracy: ' + repr(accuracy) + '%')
        kfold_val = kfold_val + accuracy
        
    kfold_val = kfold_val / kf
    print('Last Accuracy: ' + repr(kfold_val) + '%')
        
main()