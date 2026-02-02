import numpy as np

class LinearRegressionClosed:

    def __init__(self):
        self.coef_=None 
        self.intercept_=0.0 

    def fit(self,X,y):
        X=np.array(X)
        y=np.array(y)

        Xb=np.c_[np.ones((X.shape[0],1)),X] # column cancetantion done by c_..... np.ones X.shape[0],1 means it will give one column full of 1's...and then it is concatenated to the column of actual X's

        A=np.linalg.inv(Xb.T @ Xb) @ Xb.T @ y #X.T means X transposed....@ means dot product...linalg is linear algebra

        self.intercept_=A[0] #first row is intercept value 
        self.coef_=A[1:] #rest are actual coeffs

    def predict(self,X):
        pass
