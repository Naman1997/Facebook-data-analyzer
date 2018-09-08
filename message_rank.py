import os
from bs4 import BeautifulSoup
from collections import Counter
import matplotlib.pyplot as plt
from textblob import TextBlob


def p1():
    b=[]
    directory = '/root/Downloads/facebook-namanarora921/messages'
    for subdir, dirs, files in os.walk(directory):
        for filename in files:
            if filename.endswith('message.html'):
                fname = os.path.join(subdir,filename)
                with open(fname, 'r') as f:
                    soup = BeautifulSoup(f.read(),'html.parser')
                    y = soup.find_all("div",class_= "_3b0c")
                    for e in y:
                        a=e.text
                        b.append(a)
    print(b)
    b=[]





#blob = TextBlob(b[])
 #                   for sentence in blob.sentences:
  #                      print(sentence.sentiment.polarity)
   #                     print(blob.tags)
    #                    print(blob.sentiment)
     #                   print(blob.sentiment.polarity)
p1()