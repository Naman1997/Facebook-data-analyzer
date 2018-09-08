import os
from bs4 import BeautifulSoup
from collections import Counter
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.pyplot as plt

 
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
                b.append(a[0:3])
                count=count+1
            print(count)

cnt=Counter()
for word in b:
    cnt[word] += 1

jan = cnt['Jan']
feb = cnt['Feb']
mar = cnt['Mar']
apr = cnt['Apr']
may = cnt['May']
jun = cnt['Jun']
jul = cnt['Jul']
aug = cnt['Aug']
sep = cnt['Sep']
octe = cnt['Oct']
nov = cnt['Nov']
dec = cnt['Dec']



left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

height = [jan,feb,mar,apr,may,jun,jul,aug,sep,octe,nov,dec]

tick_label = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

# plotting a bar chart
plt.bar(left, height, tick_label = tick_label,
        width = 0.8, color = ['red', 'green'])
 
# naming the x-axis
plt.xlabel('x - axis')
# naming the y-axis
plt.ylabel('y - axis')
# plot title
plt.title('My bar chart!')
 
# function to show the plot
plt.show()