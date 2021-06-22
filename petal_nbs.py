import random
import sklearn
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
def NBP(a):
    split=a
    train,train_labels,test,test_labels=petal_split_data(split)
    #Building the model
    #Naive Bayes Algorithm
    from sklearn.naive_bayes import GaussianNB
    gnb=GaussianNB()
    model=gnb.fit(train,train_labels)
    #Evaluating the model & its accuracy
    preds=gnb.predict(test)
    #print(preds)
    from sklearn.metrics import accuracy_score
    accuracy=accuracy_score(test_labels,preds)*100
    #print(accuracy)
    return accuracy
if __name__=='__main__':
    print(NBP(0.8))
