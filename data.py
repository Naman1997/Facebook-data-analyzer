import os
from bs4 import BeautifulSoup
from collections import Counter
import matplotlib.pyplot as plt
from textblob import TextBlob



count =0
polarity = 0
blob_sentiment = 0
subjectivity = 0
sen_polarity = 0
directory = '/root/Downloads/facebook-namanarora921/messages'
for subdir, dirs, files in os.walk(directory):
    for filename in files:
        if filename.endswith('message.html'):
            fname = os.path.join(subdir,filename)
            with open(fname, 'r') as f:
                soup = BeautifulSoup(f.read(),'html.parser')
                x = soup.find_all("div",class_= "_3-96 _2let")
                for e in x:
                    a=e.text
                    blob = TextBlob(a)
                    count=count+1
                    for sentence in blob.sentences:
                        print(sentence.sentiment.polarity)
                        polarity = polarity+sentence.sentiment.polarity
                        print(blob.tags)
                        print(blob.sentiment)
                        subjectivity = subjectivity+blob.sentiment.subjectivity
                        sen_polarity = sen_polarity+blob.sentiment.polarity
                        print(blob.sentiment.polarity)
                        blob_sentiment = blob_sentiment+blob.sentiment.polarity
                        print(a)
                        print("\n")



print("Average Sentence Sentiment Polarity = ",polarity/count)
print("Average Blob Sentiment Polarity = ",blob_sentiment/count)
print("Average sentiment subjectivity =",subjectivity/count)
print("Average sentiment polarity",sen_polarity/count)
print("Count =",count)


