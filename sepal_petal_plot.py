import sepal_knn,petal_knn,sepal_petal_knn,sepal_petal_nbs,sepal_nbs,petal_nbs
import sepal_dt,petal_dt,sepal_petal_dt
import sepal_lg,petal_lg,sepal_petal_lg
knnsp=sepal_petal_knn.knnSP(0.7)
nbsp=sepal_petal_nbs.NBSP(0.7)
dtsp=sepal_petal_dt.spdt(0.7)
lgsp=sepal_petal_lg.splg(0.7)
import matplotlib.pyplot as plt
import numpy as np
def bar_graph():
    algorithms=('KNN','Naive Bayes','Decision Tree','Logical Regression')
    x_pos=np.arange(len(algorithms))
    accuracy=[knnsp,nbsp,dtsp,lgsp]
    plt.bar(x_pos,accuracy,align='center')
    plt.xticks(x_pos,algorithms)
    plt.ylabel('Accuracy')
    plt.title('Accuracy of Algorithms')
    plt.show()

def pie_chart():
    labels=['Knn','Naive Bayes','Decision Tree','Logical Regression']
    sizes=[knnsp,nbsp,dtsp,lgsp]
    colors=['gold','yellowgreen','lightcoral','lightskyblue']
    explode=(0.1,0,0,0)
    plt.pie(sizes,explode=explode,labels=labels,
            colors=colors,
            autopct='%1.2f%%', shadow=True, startangle=140)
    plt.axis('equal')
    plt.title('Accuracy of Algorithms')
    plt.show()
##bar_graph()
##pie_chart()
