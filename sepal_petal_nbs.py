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
def NBSP(a):
    split=a
    train,test,train_labels,test_labels=loadDataset(split)
    #Building the model
    #Naive Bayes Algorithm
    from sklearn.naive_bayes import GaussianNB
    gnb=GaussianNB()
    model=gnb.fit(train,train_labels)
    #Evaluating the model & its accuracy
    preds=gnb.predict(test)
    #print(preds)
    from sklearn.metrics  import accuracy_score
    accuracy=accuracy_score(test_labels,preds)*100
    #print("accuracy of nbs",accuracy)
    return accuracy
#NBSP()
