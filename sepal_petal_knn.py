import random
import math
import operator

def convert_string_to_float(lst,n):
    for i in range(n):
        lst[i]=float(lst[i])
    return lst
def sepal_petal_split_data(split,training_data=[],test_data=[]):

    for line in open("iris.txt","r"):
        temp =convert_string_to_float(line[0:-1].split(','),4)
              
        if random.random()<=split:
            training_data.append(temp)
        else:
            test_data.append(temp)
    return(training_data,test_data)

def euclideanDistance(instance1,instance2,length=4):
    distance=0
    for x in range(length):
        distance +=pow((instance1[x]-instance2[x]),2)
    return math.sqrt(distance)
def getneighbors(trainingSet,testInstance,k,length=4):
    distance=[]
    for x in range(len(trainingSet)):
        dist=euclideanDistance(testInstance,trainingSet[x])
        distance.append((trainingSet[x],dist))
    distance.sort(key=operator.itemgetter(1))
    neighbors=[]
    for x in range(k):
        neighbors.append(distance[x][0])
    return neighbors
def getResponse(neighbors):
    classVotes={}
    for x in range(len(neighbors)):
        response = neighbors[x][-1]
        if response in classVotes:
            classVotes[response]+=1
        else:
            classVotes[response]=1
    sortedVotes=sorted(classVotes.items(),key=operator.itemgetter(1),reverse=True)
    return sortedVotes[0][0]

def getAccuracy(testSet,predictions):
    correct=0
    for x in range(len(testSet)):
        if testSet[x][-1]==predictions[x]:
            correct+=1
    return(correct/float(len(testSet)))*100.0

def knnSP(a):
    trainingSet=[]
    testSet=[]
    split=a
    trainingSet,testSet =sepal_petal_split_data(split)
    predictions=[]
    k=3
    for x in range(len(testSet)):
        neighbors=getneighbors(trainingSet,testSet[x],k,4)
        result=getResponse(neighbors)
        predictions.append(result)
        #print('>predicted='+str(result)+',actual='+str(testSet[x][-1]))
    accuracy = getAccuracy(testSet,predictions)
    #print('Accuracy of PETAL with KNN:'+str(accuracy)+'%')
    return accuracy

