import warnings
warnings.filterwarnings(action="ignore")
import pandas as pd
from sklearn.model_selection import train_test_split  #uses only some part of data & is time saving
from sklearn.linear_model import  LogisticRegression
from matplotlib import pyplot as plt
import sys
def blah():
    filename= 'data.csv'
    hnames= ['deathtoll','mag','req_fund']
    dataframe=pd.read_csv(filename,names=hnames)
    array= dataframe.values
    dataframe.plot(x ='deathtoll', y='req_fund', kind = 'line')
    #plt.show()

    #separate array into input and output components
    x=array[:,0:2]  #input column
    y=array[:,2]     #output column

    test_data_size=0.1 #hides 33% data from machine so that it will be used for testing
    #seed=4
    x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=test_data_size) #,random_state=seed)

    model= LogisticRegression()
    model.fit(x_train,y_train)
    r=model.predict([[2089,8.9]])
        
    #ra.plot(x ='deathtoll', y='req_fund', kind = 'dotted-line',marker='d')
    # plt.plot(int(sys.argv[1]),int(sys.argv[2]),marker='o',markerfacecolor='red',markersize=7,
            # linestyle='dashed',color='blue')
    plt.plot(3500,45000,marker='o',markerfacecolor='red',markersize=7,
            linestyle='dashed',color='blue')
    plt.show()
    #result= model.score(x_test,y_test)  #checks accuracy of algorithm

    #print("Accuracy= %f %%"% (result*100))
blah()