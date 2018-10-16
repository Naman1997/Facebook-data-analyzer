import webbrowser
import os
from bs4 import BeautifulSoup
import requests
import matplotlib.pyplot as plt

count =0
a=[]
b=[]
height = []
tick_label = []

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


text = '+'.join([str(v) for v in b])
print("\n")
print("INPUT IS GIVEN IN THE FOLLOWING FORMAT")
print("\n")
print(text)
print("\n")
print("\n")
classifier = 'Ageanalyzer'
readkey = 'aweO454Kgswc'

url = 'https://api.uclassify.com/v1/uClassify/'+classifier+'/classify/?readKey='+readkey+'&text=This+is+the+text+to+classify'

# Open URL in a new tab, if a browser window is already open.
#webbrowser.open_new_tab(url)

test = requests.get(url)

output = test.text

#CONVERTING THE INPUT STRING TO A DICTIONARY

string = output

#Now removing { and }
s = string.replace("{" ,"");
finalstring = s.replace("}" , "");

#Splitting the string based on , we get key value pairs
list = finalstring.split(",")

dict ={}
for i in list:
    #Get Key Value pairs separately to store in dictionary
    keyvalue = i.split(":")

    #Replacing the single quotes in the leading.
    m= keyvalue[0].strip('\'')
    m = m.replace("\"", "")
    dict[m] = keyvalue[1].strip('"\'')

print("Age distribution percentage")

for i in dict:
    height.append(float(dict[i])*100)
    tick_label.append(i)
    print(i,"::",float(dict[i])*100,"%")


#print(height)
#print(tick_label)
left = [1, 2, 3, 4, 5, 6]


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



