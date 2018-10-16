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
                        print(blob.sentiment.polarity)
                        blob_sentiment = blob_sentiment+blob.sentiment.polarity
                        print(a)
                        print("\n")


aa=polarity/count
bb=blob_sentiment/count
cc=subjectivity/count

print("Average Sentence Sentiment Polarity = ",aa)
print("Average Blob Sentiment Polarity = ",bb)
print("Average sentiment subjectivity =",cc)
print("Count =",count)

left = [1, 2, 3]


height = [aa, bb, cc]

tick_label = ['Average Sentence Sentiment Polarity', 'Average Blob Sentiment Polarity', 'Average sentiment subjectivity']

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
