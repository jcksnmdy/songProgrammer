import pandas as pd
import os
import time
import random
import subprocess
import sys
#sys.path.append('/home/pi/Desktop/globals/')
sys.path.append('/Users/s1034274/Desktop/globals/')
from constants import path


num = int(input("Song: "))
numStart = int(input("Start: "))
numEnd = int(input("End: "))
dimBy = float(input("Dim Num: "))


color = (255, 255, 255)
dfToAdd = pd.read_excel("/Users/s1034274/Desktop/flagCode/song" + str(num) + ".xlsx")

songSequence = pd.DataFrame()
i = 0

def toTupleCheck(before):
    global i, dimBy
    before = str(before)
    firstNum = round(float(before[before.find("(")+1:before.find(",")]), 0)
    secNum = round(float(before[before.find(",")+2:before.find(",", 9)]), 0)
    thirdNum = round(float(before[before.find(",", 9)+2:before.find(")")]), 0)
    if (i >= numStart and i <= numEnd):
        returning = (firstNum/dimBy, secNum/dimBy, thirdNum/dimBy)
    else:
        returning = (firstNum, secNum, thirdNum)
    return returning

def compile():
    global color, songSequence, df, num, numStart, numEnd, i
    while (i < len(dfToAdd)):

        reds = dfToAdd.loc[(i),'red Left']

        oranges = dfToAdd.loc[(i),'orange Left']

        whites = dfToAdd.loc[(i),'white Left']

        yellows = dfToAdd.loc[(i),'yellow Left']

        greens = dfToAdd.loc[(i),'green Left']

        blues = dfToAdd.loc[(i),'blue Left']

        songSequence = songSequence.append({
                    'red Left':toTupleCheck(reds),
                    'red Middle':toTupleCheck(reds),
                    'red Right':toTupleCheck(reds),
                    'orange Left':toTupleCheck(oranges),
                    'orange Middle':toTupleCheck(oranges),
                    'orange Right':toTupleCheck(oranges),
                    'white Left':toTupleCheck(whites),
                    'white Middle':toTupleCheck(whites),
                    'white Right':toTupleCheck(whites),
                    'yellow Left':toTupleCheck(yellows),
                    'yellow Middle':toTupleCheck(yellows),
                    'yellow Right':toTupleCheck(yellows),
                    'green Left':toTupleCheck(greens),
                    'green Middle':toTupleCheck(greens),
                    'green Right':toTupleCheck(greens),
                    'blue Left':toTupleCheck(blues),
                    'blue Middle':toTupleCheck(blues),
                    'blue Right':toTupleCheck(blues)}, ignore_index=True)
        print(str(i) + "/" + str(len(dfToAdd)) + " " + str(reds) + " " + str(oranges) + " " + str(whites) + " " + str(yellows) + " " + str(greens) + " " + str(blues))
        i+=1
        

def finish(songNum):
    global color, songSequence
    songSequence.to_excel("/Users/s1034274/Desktop/flagCode/song" + str(num) + ".xlsx")



compile()
finish(num)