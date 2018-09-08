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
                b.append(a[-2:])
                count=count+1
            print(b)

cnt=Counter()
for word in b:
    cnt[word] += 1

am = cnt['am']
pm = cnt['pm']


left = [1, 2]

height = [am, pm]

tick_label = ['am', 'pm']


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