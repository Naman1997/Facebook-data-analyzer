from tkinter import *
import subprocess

OPTIONS = [
"Month",
"Year",
"Time",
"Year_prediction_with_outliar",
"Year_prediction_without_outliar",
"Month_prediction"
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

button = Button(master, text="OK", command=ok)
button.pack()

mainloop()