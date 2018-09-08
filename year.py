import os
from bs4 import BeautifulSoup
from collections import Counter
import matplotlib.pyplot as plt
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

tick_label = ['2012', '2013', '2014', '2015', '2016', '2017', '2018']

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