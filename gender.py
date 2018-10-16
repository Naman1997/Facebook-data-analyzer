import webbrowser
import os
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

def urlify(s):

     # Remove all non-word characters (everything except numbers and letters)
     #s = re.sub(r"[^\w\s]", '', s)

     # Replace all runs of whitespace with a single dash
     s = re.sub(r"\s+", '-', s)

     return s

count =0
a=[]
b=[]
next_lines = []

directory ='/root/Downloads/facebook-namanarora921/ads'
for filename in os.listdir(directory):
    if filename.endswith('interests.html'):
        fname = os.path.join(directory,filename)
        with open(fname, 'r') as f:
            soup = BeautifulSoup(f.read(),'html.parser')
            x = soup.find_all("div",class_= "_2lek")
            for e in x:
                a=e.text
                b.append(a)


text = ''.join([str(v) for v in b])
trr = "+".join(text.split())
print("\n")
print("INPUT IS GIVEN IN THE FOLLOWING FORMAT")
print("\n")
print(trr)
print("\n")
print("\n")
classifier = 'genderanalyzer_v5'
readkey = 'aweO454Kgswc'

url = 'https://api.uclassify.com/v1/uClassify/'+classifier+'/classify/?readKey='+readkey+'&text=This+is+the+text+to+classify'

test = requests.get(url)

#webbrowser.open(url_2, new=2)

output = test.text

male = output[26:34]
female = output[10:18]
print(output)
print("Percentage of male =",float(male)*100,"%")
print("Percentage of female =",float(female)*100,"%")

male_p = float(male)*100
female_p = float(female)*100


left = [1, 2]

height = [male_p, female_p]

tick_label = ['male', 'female']

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