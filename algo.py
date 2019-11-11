import warnings
warnings.filterwarnings(action="ignore")
import pandas as pd
from sklearn.model_selection import train_test_split  #uses only some part of data & is time saving
from sklearn.linear_model import  LogisticRegression
from matplotlib import pyplot as plt
import sys
filename= 'nn.csv'
hnames= ['amount','item','donor_id','redonate']
dataframe=pd.read_csv(filename,names=hnames)
array= dataframe.values
#dataframe.hist(x='donor_id',y='redonate')
dataframe.plot(x ='donor_id', y='redonate', kind = 'bar')
#separate array into input and output components
x=array[:,0:3]  #input column
y=array[:,3]     #output column
test_data_size=0.1 #hides 33% data from machine so that it will be used for testing
#seed=4
x_train,x_test,y_train,y_test= train_test_split(x,y,test_size=test_data_size) #,random_state=seed)

model= LogisticRegression()
model.fit(x_train,y_train)
r=model.predict([[1000,2,6.9]])
print(r)
ra1=[2]
plt.plot(ra1,r,marker='o',markerfacecolor='red',markersize=7,
          linestyle='dashed',color='blue')

ab=model.predict([[200,8,3]])
print(ab)
ra2=[8]
plt.plot(ra2,ab,marker='o',markerfacecolor='green',markersize=7,
          linestyle='dashed',color='blue')

bc=model.predict([[6000,6,7]])
print(bc)
ra3=[6]
plt.plot(ra3,bc,marker='o',markerfacecolor='pink',markersize=7,
          linestyle='dashed',color='blue')
plt.show()
