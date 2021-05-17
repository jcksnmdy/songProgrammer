import pandas as pd
import os
import time
import random
import subprocess
import sys
sys.path.append('/home/pi/Desktop/globals/')
#sys.path.append('/Users/s1034274/Desktop/globals/')
from constants import path

color = (255, 255, 255)
df = pd.read_excel(path + "/songProgrammer/songTemp.xlsx")
songSequence = pd.DataFrame()

def compile():
    global color, songSequence, df
    i = 0
    while (i < len(df)):
        print(str(df.loc[(i),'red Left']) + "  " + str(i) + "/" + str(len(df)))
        songSequence = songSequence.append({
                    'red Left':df.loc[(i),'red Left'],
                    'red Middle':df.loc[(i),'red Middle'],
                    'red Right':df.loc[(i),'red Right'],
                    'orange Left':df.loc[(i),'orange Left'],
                    'orange Middle':df.loc[(i),'orange Middle'],
                    'orange Right':df.loc[(i),'orange Right'],
                    'white Left':df.loc[(i),'white Left'],
                    'white Middle':df.loc[(i),'white Middle'],
                    'white Right':df.loc[(i),'white Right'],
                    'yellow Left':df.loc[(i),'yellow Left'],
                    'yellow Middle':df.loc[(i),'yellow Middle'],
                    'yellow Right':df.loc[(i),'yellow Right'],
                    'green Left':df.loc[(i),'green Left'],
                    'green Middle':df.loc[(i),'green Middle'],
                    'green Right':df.loc[(i),'green Right'],
                    'blue Left':df.loc[(i),'blue Left'],
                    'blue Middle':df.loc[(i),'blue Middle'],
                    'blue Right':df.loc[(i),'blue Right']}, ignore_index=True)
        i+=1

def finish(songNum):
    global color, songSequence
    songSequence.to_excel(path + "/flagCode/song" + str(songNum) + ".xlsx")


def toTuple(before):
    print(before)
    firstNum = int(before[before.find("'")+2:before.find(",")])
    secNum = int(before[before.find(",")+2:before.find(",", 9)])
    thirdNum = int(before[before.find(",", 9)+2:before.find("'", 9)])
    returning = (firstNum, secNum, thirdNum)
    print(returning)
    return returning

num = int(input("Song number: "))
compile()
finish(num)