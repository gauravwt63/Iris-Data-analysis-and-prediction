import sepal_knn,petal_knn,sepal_petal_knn,sepal_petal_nbs,sepal_nbs,petal_nbs
import sepal_dt,petal_dt,sepal_petal_dt
import sepal_lg,petal_lg,sepal_petal_lg
knnp=petal_knn.knnP(0.7)
nbp=petal_nbs.NBP(0.7)
dtp=petal_dt.pdt(0.7)
lgp=petal_lg.plg(0.7)
import matplotlib.pyplot as plt
import numpy as np
def bar_graph():
    algorithms=('KNN','Naive Bayes','Decision Tree','Logical Regression')
    x_pos=np.arange(len(algorithms))
    accuracy=[knnp,nbp,dtp,lgp]
    plt.bar(x_pos,accuracy,align='center')
    plt.xticks(x_pos,algorithms)
    plt.ylabel('Accuracy')
    plt.title('Accuracy of Algorithms with Petal')
    plt.show()
def pie_chart():
    labels=['Knn','Naive Bayes','Decision Tree','Logical Regression']
    sizes=[knnp,nbp,dtp,lgp]
    colors=['gold','yellowgreen','lightcoral','lightskyblue']
    explode=(0.1,0,0,0)
    plt.pie(sizes,explode=explode,labels=labels,
            colors=colors,
            autopct='%1.2f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title('Accuracy of Algorithms with Petal')
    plt.show()    
if __name__=="__main__":
    pie_chart()
    bar_graph()
    


