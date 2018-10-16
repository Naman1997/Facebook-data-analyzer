import os
from bs4 import BeautifulSoup
from collections import Counter
import matplotlib.pyplot as plt
from textblob import TextBlob
import heapq


def p1():
    b=[]
    count=0
    mydict={}
    directory = '/root/Downloads/facebook-namanarora921/messages'
    for subdir, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('message.html'):
                fname = os.path.join(subdir,filename)
                with open(fname, 'r') as f:
                    soup = BeautifulSoup(f.read(),'html.parser')
                    x = soup.find_all("div",class_= "_3-96 _2let")
                    y = soup.find_all("div",class_= "_3b0d")
                    for g in x:
                        r=g.text
                        for e in y:
                            t=e.text
                            count=count+1
                    mydict[t]=count
                    count=0
    print(sorted(mydict.items(), key=lambda x: x[1]))
    print("\n\n")
    top = heapq.nlargest(5, mydict, key=mydict.get)
    for q in top:
        l = mydict[q]
        print(l," messages with ",q)






"""                    for g,e in zip(x,y):
                        a=e.text
                        count=count+1
                        b.append(a) 
                        cnt=Counter()
                        for word in b:
                            cnt[word] += 1
    print(a)
    print(count)
    print(cnt)   """






p1()