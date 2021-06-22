import random
import sklearn
import numpy as np
import matplotlib.pyplot as plt
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
               train.append(convert_to_float(temp[0:-1]))
               train_labels.append(temp[-1])
          else:
                test.append(convert_to_float(temp[0:-1]))
                test_labels.append(temp[-1])
     return train,test,train_labels,test_labels
def splg(a):
        trainingSet=[]
        testSet=[]
        split=a
        train,test,train_labels,test_labels=loadDataset(split)       
        sl=float(input("Enter sepal length:"))
        sw=float(input("Enter sepal width:"))
        data_in=([[sl,sw]])
        from sklearn.linear_model import LogisticRegression
        logisticRegr=LogisticRegression()
        logisticRegr.fit(train,train_labels)
        preds=logisticRegr.predict(data_in)
        #print(preds[0])
        return preds[0]
if __name__=='__main__':
    splg(0.7)
    
