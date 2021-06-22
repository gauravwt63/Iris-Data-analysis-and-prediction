import numpy as np
import matplotlib.pyplot as plt
import random
import math
import operator
def getNeighbours(trainingSet,testInstance,k):  #Smallest k distances
    distance=[]
    length=4  #4
    for x in range(len(trainingSet)):
        dist=euclideanDistance(testInstance,trainingSet[x],length)
        distance.append((trainingSet[x],dist))
    distance.sort(key=operator.itemgetter(1)) #on the basis of dist
    neighbours=[]
    for x in range(k):
        neighbours.append(distance[x][0])
    return neighbours


def convert_str_to_float(lst,n):#lst=['5.1', '3.5', '1.4', '0.2', 'Iris-setosa']
    for i in range(n):
        lst[i]=float(lst[i]) #changing str data to float
    return(lst)


def loadDataset(split,training_data=[],test_data=[]): 
    for line in open("iris.txt",'r'):
        temp=convert_str_to_float(line[0:-1].split(','),4)
        if random.random()<=split:  
             training_data.append(temp)
        else:
              test_data.append(temp)

    return(training_data,test_data)


def euclideanDistance(instance1,instance2,length):
    distance=0
    for x in range(length):
        distance+=pow((instance1[x]-instance2[x]),2)
    return math.sqrt(distance)

def getResponse(neighbours):
    classVotes={}
    for x in range(len(neighbours)):
        response=neighbours[x][-1]
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

def pknn(a):
    trainingSet=[]
    testSet=[]
    split=a
    trainingSet,_=loadDataset(split)
    sl=float(input("Enter sepal length:"))
    sw=float(input("Enter sepal width:"))
    pl=float(input("Enter petal length:"))
    pw=float(input("Enter petal length:"))
    testSet=[sl,sw,pl,pw]
    k=3  
    neighbours=getNeighbours(trainingSet,testSet,k)
    result=getResponse(neighbours)
    #print('>predicted='+str(result))
    predict=str(result)
    return predict
#main()    



    

