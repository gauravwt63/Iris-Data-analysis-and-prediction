import random
import sklearn
import numpy as np
import matplotlib.pyplot as plt
def convert_to_float(lst):
    column=0
    while column<4:#2
        lst[column]=float(lst[column])
        column +=1
    return lst

def petal_split_data(split,training_data=[],test_data=[]):
    for line in open("iris.txt","r"):
        temp =convert_to_float(line[0:-1].split(','))
        temp=(temp[2:4],temp[-1])
        if random.random()<=split:
            training_data.append(temp)
        else:
            test_data.append(temp)
        training_data_tr=[i[0]  for i in training_data]
        training_data_label=[ i[1] for i in training_data]
        test_data_tr=[i[0]  for i in test_data]
        test_data_label=[i[1] for i in test_data]
    return(training_data_tr,training_data_label,test_data_tr,test_data_label)
def ppNB(a):
    split=a
    train,train_labels,test,test_labels=petal_split_data(split)
    pl=float(input("Enter petal length:"))
    pw=float(input("Enter petal width:"))
    data_in=([[pl,pw]])
    #Building the model
    #Naive Bayes Algorithm
    from sklearn.naive_bayes import GaussianNB
    gnb=GaussianNB()
    model=gnb.fit(train,train_labels)
    #Evaluating the model & its accuracy
    preds=gnb.predict(data_in)
    #print(preds[0])
    return preds[0]

if __name__=='__main__':
    print(ppNB(0.8))
