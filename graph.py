import warnings
warnings.filterwarnings(action="ignore")
import pandas as pd
from sklearn.model_selection import train_test_split  #uses only some part of data & is time saving
from sklearn.linear_model import  LogisticRegression
from matplotlib import pyplot as plt


#result= model.score(x_test,y_test)  #checks accuracy of algorithm

#print("Accuracy= %f %%"% (result*100))