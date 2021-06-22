import random
import sklearn
import numpy as np
def convert_to_float(lst):
    column=0
    while column<2:#2
        lst[column]=float(lst[column])
        column +=1
    return lst
def loadDataset(split,train=[],test=[],train_labels=[],test_labels=[]):
     for line in open(r"iris.txt",'r'):
          temp=line[0:-1].split(",")
          temp.pop(0)
          temp.pop(0)
          if random.random() < split :
               train.append(convert_to_float(temp[0:-1]))
               train_labels.append(temp[-1])
          else:
                test.append(convert_to_float(temp[0:-1]))
                test_labels.append(temp[-1])
     return train,test,train_labels,test_labels
def pplg(a):
        trainingSet=[]
        testSet=[]
        split=a
        train,test,train_labels,test_labels=loadDataset(split)       
        pl=float(input("Enter petal length:"))
        pw=float(input("Enter petal width:"))
        data_in=([[pl,pw]])
        from sklearn.linear_model import LogisticRegression
        logisticRegr=LogisticRegression()
        logisticRegr.fit(train,train_labels)
        preds=logisticRegr.predict(data_in)
       # print(preds[0])
        return preds[0]
if __name__=='__main__':
    pplg(0.7)
    
