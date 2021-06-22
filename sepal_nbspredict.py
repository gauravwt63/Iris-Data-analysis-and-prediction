import random
import sklearn
import numpy as np
import matplotlib.pyplot as plt
import random
def convert_to_float(lst):
    column=0
    while column<4:#2
        lst[column]=float(lst[column])
        column +=1
    return lst

def sepal_split_data(split,training_data=[],test_data=[]):
    for line in open("iris.txt","r"):
        temp =convert_to_float(line[0:-1].split(','))
        temp=(temp[0:2],temp[-1])
        if random.random()<=split:
            training_data.append(temp)
        else:
            test_data.append(temp)
        training_data_tr=[i[0]  for i in training_data]
        training_data_label=[ i[1] for i in training_data]
        test_data_tr=[i[0]  for i in test_data]
        test_data_label=[i[1] for i in test_data]
    return(training_data_tr,training_data_label,test_data_tr,test_data_label)
def spNB(a):
    split=a
    train,train_labels,test,test_labels=sepal_split_data(split)
    sl=float(input("Enter sepal length:"))
    sw=float(input("Enter sepal width:"))
    data_in=([[sl,sw]])
    from sklearn.naive_bayes import GaussianNB
    gnb=GaussianNB()
    model=gnb.fit(train,train_labels)
    #Evaluating the model & its accuracy
    preds=gnb.predict(data_in)
    #print(preds[0])
    return preds[0]
#sNB(0.7)
