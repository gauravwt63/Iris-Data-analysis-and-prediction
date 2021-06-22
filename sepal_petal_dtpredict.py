import numpy as np
import random
import sklearn
def convert_to_float(lst):
    column=0
    while column<4:#2
        lst[column]=float(lst[column])
        column +=1
    return lst
def loadDataset(split,train=[],test=[],train_labels=[],test_labels=[]):
     for line in open(r"iris.txt",'r'):
          temp=line[0:-1].split(",")
          if random.random() < split :
               train.append(convert_to_float(temp[0:-1]))
               train_labels.append(temp[-1])
          else:
                test.append(convert_to_float(temp[0:-1]))
                test_labels.append(temp[-1])
     return train,test,train_labels,test_labels
def pdt(a):
    trainingSet=[]
    testSet=[]
    split=a
    train,test,train_labels,test_labels=loadDataset(split)
    from sklearn.tree import DecisionTreeClassifier
    sl=float(input("Enter sepal length:"))
    sw=float(input("Enter sepal width:"))
    pl=float(input("Enter petal length:"))
    pw=float(input("Enter petal length:"))
    data_in=([[sl,sw,pl,pw]])
    dtc = DecisionTreeClassifier()
    model=dtc.fit(train,train_labels)
    y_pred =dtc.predict(data_in)
    #print(y_pred[0])
    return y_pred[0]
#spdt(0.7)
