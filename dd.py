from tkinter import *
import subprocess

OPTIONS = [
"Month",
"Year",
"Time",
"Year_prediction_with_outliar",
"Year_prediction_without_outliar",
"Month_prediction",
"Top 5 friends using a heap",
"User Gender Prediction",
"User Age Prediction",
"Text tokeniztion with NLP",
"Overall Mood Analysis with NLP",
"User's topic interest using NLP"
] #etc

master = Tk()

variable = StringVar(master)
variable.set(OPTIONS[0]) # default value

w = OptionMenu(master, variable, *OPTIONS)
w.pack()

def ok():
    a = variable.get()
    print(a)
    if a=="Month":
        subprocess.call(" python3 month.py 1",shell=True)
    elif a=="Year":
        subprocess.call(" python3 year.py 1",shell=True)
    elif a=="Time":
        subprocess.call(" python3 time.py 1",shell=True)
    elif a=="Year_prediction_with_outliar":
        subprocess.call(" python3 jj.py 1",shell=True)
    elif a=="Year_prediction_without_outliar":
        subprocess.call(" python3 kk.py 1",shell=True)
    elif a=="Month_prediction":
        subprocess.call(" python3 nn.py 1",shell=True)
    elif a=="User Gender Prediction":
        subprocess.call(" python3 gender.py 1",shell=True)
    elif a=="User Age Prediction":
        subprocess.call(" python3 age.py 1",shell=True)
    elif a=="Text tokeniztion with NLP":
        subprocess.call(" python3 data.py 1",shell=True)
    elif a=="Top 5 friends using a heap":
        subprocess.call(" python3 message_rank.py 1",shell=True)
    elif a=="Overall Mood Analysis with NLP":
        subprocess.call(" python3 sentiment.py 1",shell=True)
    elif a=="User's topic interest using NLP":
        subprocess.call(" python3 topics.py 1",shell=True)

button = Button(master, text="OK", command=ok)
button.pack()

mainloop()