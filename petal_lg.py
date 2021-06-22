from sklearn.datasets import load_iris
import numpy as np
import matplotlib.pyplot as plt
def plg(a):
    split=a
    digits=load_iris()
    x=digits.data[:,2:4]
    y=digits.target
    from sklearn.model_selection import train_test_split
    x_train,x_test,y_train,y_test=train_test_split(
        x,y,test_size=split,random_state=0)

    from sklearn.linear_model import LogisticRegression
    logisticRegr=LogisticRegression()

    logisticRegr.fit(x_train,y_train)
    ##logisticRegr.predict(x_test[0])
    ##logisticRegr.predict(x_test[0:10])

    predictions=logisticRegr.predict(x_test)
    score=logisticRegr.score(x_test,y_test)*100

    #print(score)
    return score
#slg(0.7)
    
