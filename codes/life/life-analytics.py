# Game Of Life Analytics Code
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from lazyt import Loader
from time import sleep
times=[]
players=[]
with open('lifeanalytics.txt','a') as txt:
    pass
import time as afdhhs
def tprint(srt,time=0.025):
    for char in srt:
        print(char,end="")
        afdhhs.sleep(time)
    print()
def tinput(srt,time=0.025,space=""):
    for char in srt:
        print(char,end="")
        afdhhs.sleep(time)
    entered=input(space)
    return entered
def readfile():
    with open('lifeanalytics.txt','r') as txt:
        txt=txt.readlines()
        txt[0]=txt[0][:-1]
        times=txt[0].split("|")
        players=txt[1].split("|")
        return times,players
if __name__=="__main__":
    l=Loader("Importing Analytics ","Analytics Import Complete ",0.05)
    sleep(1)
    l.stop()
l=Loader("Reading File ","File Read Complete",0.05).start()
timess,playerss=readfile()
l.stop()
l=Loader("Plotting Date ","Data Plotting Complete ",0.05).start()
df = pd.DataFrame({'y_axis':timess,'x_axis':playerss})
plt.plot('x_axis','y_axis',data=df,marker='o')
plt.ylabel("Time to Complete (Seconds)")
plt.xlabel("Number of Players (Numbers)")
l.stop()
plt.show()