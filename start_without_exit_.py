import sepal_knn,petal_knn,sepal_petal_knn,sepal_petal_nbs,sepal_nbs,petal_nbs
import sepal_knnpredict,petal_knnpredict,sepal_petal_knnpredict
import sepal_nbspredict,petal_nbspredict,sepal_petal_nbspredict
import sepal_dt,petal_dt,sepal_petal_dt
import sepal_dtpredict,petal_dtpredict,sepal_petal_dtpredict
import sepal_lg,petal_lg,sepal_petal_lg
import sepal_lgpredict,petal_lgpredict,sepal_petal_lgpredict
import sepal_petal_plot
def main():
    ina=None
    inp=None
    print("Welcome to iris data Analysis & Prediction Project")
    while True:
        print("1:Analyze DataSet.")
        print("2:Predict from data.")
        print("3:To Exit")
        inp_choice=int(input(("Enter a value:")))
        if inp_choice==1:
            print("1:Analyze DataSet on Sepal Length & Sepal Width")
            print("2:Analyze DataSet on Petal Length & Petal Width")
            print("3:Analyze DataSet on Sepal & petal( Length   Width)")
            print("4:To Exit")
            ina=int(input("Enter a value:"))
            if ina==1:
                accuracy_knn=sepal_knn.knnS(0.7)
                print("Knn accuracy:",accuracy_knn)
                accuracy_NB=sepal_nbs.NBS(0.7)
                print("Naive Bays accuracy:",accuracy_NB)
                accuracy_DT=sepal_dt.sdt(0.7)
                print("Decision Tree accuracy:",accuracy_DT)
                accuracy_DT=sepal_lg.slg(0.7)
                print("Logical Regression accuracy:",accuracy_DT)
            elif ina==2:
                accuracy_knn=petal_knn.knnP(0.7)
                print("Knn accuracy:",accuracy_knn)
                accuracy_NB=petal_nbs.NBP(0.7)
                print("Naive Bays accuracy:",accuracy_NB)
                accuracy_DT=petal_dt.pdt(0.7)
                print("Decision Tree accuracy:",accuracy_DT)
                accuracy_DT=petal_lg.plg(0.7)
                print("Logical Regression accuracy:",accuracy_DT)
            elif ina==3:
                accuracy_knn=sepal_petal_knn.knnSP(0.7)
                print("Knn accuracy:",accuracy_knn)
                accuracy_NB=sepal_petal_nbs.NBSP(0.7)
                print("Naive Bays accuracy:",accuracy_NB)
                accuracy_DT=sepal_petal_dt.spdt(0.7)
                print("Decision Tree accuracy:",accuracy_DT)
                accuracy_DT=sepal_petal_lg.splg(0.7)
                print("Logical Regression accuracy:",accuracy_DT)
                print("Which graph you want to see for the Accuracy")
                while True:
                    print("1.Bar Graph")
                    print("2.Pie Chart")
                    inc=int(input("Enter a value:"))
                    if inc==1:
                        sepal_petal_plot.bar_graph()
                        break
                    elif inc==2:
                        sepal_petal_plot.pie_chart()
                        break
            elif ina==4:
                break
        elif inp_choice==2:
                print("1:Predict DataSet on Sepal Length & Sepal Width")
                print("2:Predict DataSet on Petal Length & Petal Width")
                print("3:Predict DataSet on Sepal & petal( Length   Width)")
                print("4:To Exit")
                inp=int(input(("Enter a value:")))
                if inp==1:
                    print("Enter Sepal Length & Width:")
##                  sl=float(input("Enter sepal length:"))
##                    sw=float(input("Enter sepal width:"))
                    res_knn=sepal_knnpredict.psknn(0.7)
                    print("knn prediction for Sepal:",res_knn)
                    res_NB=sepal_nbspredict.spNB(0.7)
                    print("NBS prediction for Sepal:",res_NB)
                    res_DT=sepal_dtpredict.spdt(0.7)
                    print("Decision Tree prediction:",res_DT)
                    res_LG=sepal_lgpredict.splg(0.7)
                    print("Logical Regression accuracy:",res_LG)
                elif inp==2:
                    print("Enter Petal Length & Width:")
##                    pl=float(input("Enter petal length:"))
##                    pw=float(input("Enter petal width:"))
                    res_knn=petal_knnpredict.ppknn(0.7)
                    print("knn prediction for Petal:",res_knn)
                    res_NB=petal_nbspredict.ppNB(0.7)
                    print("NBS prediction for Petal:",res_NB)
                    res_DT=petal_dtpredict.ppdt(0.7)
                    print("Decision Tree prediction:",res_DT)
                    res_LG=petal_lgpredict.pplg(0.7)
                    print("Logical Regression accuracy:",res_LG)
                elif inp==3:
                    print("Enter Sepal,Petal Length & Width:")
##                    sl=float(input("Enter sepal length:"))
##                    sw=float(input("Enter sepal width:"))
##                    pl=float(input("Enter petal length:"))
##                    pw=float(input("Enter petal width:"))
                    res_knn=sepal_petal_knnpredict.pknn(0.7)
                    print("knn prediction for Sepal & petal:",res_knn)
                    res_NB=sepal_petal_nbspredict.pNB(0.7)
                    print("NBS prediction for Sepal & petal:",res_NB)
                    res_DT=sepal_petal_dtpredict.pdt(0.7)
                    print("Decision Tree prediction",res_DT)
                    res_LG=sepal_petal_lgpredict.spplg(0.7)
                    print("Logical Regression accuracy:",res_LG)
                elif inp==4:
                    break
        elif inp_choice==3:
            break

                

      
main()        
        

        
