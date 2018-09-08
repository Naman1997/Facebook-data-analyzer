#This one is for prediction of comments for net year if outliar is not removed


import os
from bs4 import BeautifulSoup
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np


 
def estimate_coef(x, y):
    # number of observations/points
    n = np.size(x)
 
    # mean of x and y vector
    m_x, m_y = np.mean(x), np.mean(y)
 
    # calculating cross-deviation and deviation about x
    SS_xy = np.sum(y*x - n*m_y*m_x)
    SS_xx = np.sum(x*x - n*m_x*m_x)
 
    # calculating regression coefficients
    b_1 = SS_xy / SS_xx
    b_0 = m_y - b_1*m_x
 
    return(b_0, b_1)
 
def plot_regression_line(x, y, b):
    # plotting the actual points as scatter plot
    plt.scatter(x, y, color = "m",
               marker = "o", s = 30)
    # predicted response vector
    y_pred = b[0] + b[1]*x
    # plotting the regression line
    plt.plot(x, y_pred, color = "g")
    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')
    # function to show plot
    plt.show()

count =0
y=0
a=[]
b=[]
directory ='/root/Downloads/facebook-namanarora921/comments'
for filename in os.listdir(directory):
    if filename.endswith('.html'):
        fname = os.path.join(directory,filename)
        with open(fname, 'r') as f:
            soup = BeautifulSoup(f.read(),'html.parser')
            x = soup.find_all("div",class_= "_3-94 _2lem")
            for e in x:
                a=e.text
                b.append(a[8:12])
                count=count+1
            print(b)

cnt=Counter()
for word in b:
    cnt[word] += 1


y12 = cnt['2012']
y13 = cnt['2013']
y14 = cnt['2014']
y15 = cnt['2015']
y16 = cnt['2016']
y17 = cnt['2017']
y18 = cnt['2018']

left = [1, 2, 3, 4, 5, 6, 7]

height = [y12, y13, y14, y15, y16, y17, y18]

y = np.asarray(height)

x = np.asarray(left)



# estimating coefficients
b = estimate_coef(x, y)
print("Estimated coefficients:\nb_0 = {}  \
      \nb_1 = {}".format(b[0], b[1]))
val = b[0]+b[1]*8
print("Prediction for next month =",val)
y= np.append(y,val)
x= np.append(x,8)

# plotting regression line
plot_regression_line(x, y, b)