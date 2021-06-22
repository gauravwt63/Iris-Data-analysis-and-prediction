import numpy as np
import random
import sklearn
def convert_to_float(lst):
    column=0
    while column<2:#2
        lst[column]=float(lst[column])
        column +=1
    return lst
def loadDataset(split,train=[],test=[],train_labels=[],test_labels=[]):
     for line in open(r"iris.txt",'r'):
          temp=line[0:-1].split(",")
          temp.pop(3)
          temp.pop(2)
           
          if random.random() < split :
               train.append(convert_to_float(temp[0:2]))
               train_labels.append(temp[-1])
          else:
                test.append(convert_to_float(temp[0:2]))
                test_labels.append(temp[-1])
     return train,test,train_labels,test_labels
def spdt(a):
    trainingSet=[]
    testSet=[]
    split=a
    train,test,train_labels,test_labels=loadDataset(split)
    from sklearn.tree import DecisionTreeClassifier
    sl=float(input("Enter sepal length:"))
    sw=float(input("Enter sepal width:")) 
    data_in=([[sl,sw]])
    dtc = DecisionTreeClassifier()
    model=dtc.fit(train,train_labels)
    y_pred =dtc.predict(data_in)
    #print(y_pred[0])
    return y_pred[0]  
#spdt(0.7)
