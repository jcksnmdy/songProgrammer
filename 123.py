import pandas as pd
import os
import time
import random
import subprocess
import sys
#sys.path.append('/home/pi/Desktop/globals/')
sys.path.append('/Users/s1034274/Desktop/globals/')
from constants import path

num = int(input("Song number: "))

color = (255, 255, 255)
dfToAdd = pd.read_excel("songs/song" + str(num) + ".xlsx")

songSequence = pd.DataFrame()

def toTupleCheck(before):
    before = str(before)
    firstNum = round(float(before[before.find("(")+1:before.find(",")]), 0)
    secNum = round(float(before[before.find(",")+2:before.find(",", 9)]), 0)
    thirdNum = round(float(before[before.find(",", 9)+2:before.find(")")]), 0)
    if (firstNum < 50.0 and secNum < 50.0 and thirdNum < 50.0):
        returning = (0.0, 0.0, 0.0)
    else:
        returning = (firstNum, secNum, thirdNum)
    return returning

def compile():
    global color, songSequence, df, num
    i = 5
    while (i < len(dfToAdd)):

        reds = dfToAdd.loc[(i),'Red 1']

        oranges = dfToAdd.loc[(i),'Orange 2']

        whites = dfToAdd.loc[(i),'White 3']

        yellows = dfToAdd.loc[(i),'Yellow 4']

        greens = dfToAdd.loc[(i),'Green 5']

        blues = dfToAdd.loc[(i),'Blue 6']

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
        i+=2
        

def finish(songNum):
    global color, songSequence
    songSequence.to_excel("songTemp123.xlsx")


def toTuple(before):
    print(before)
    firstNum = int(before[before.find("'")+2:before.find(",")])
    secNum = int(before[before.find(",")+2:before.find(",", 9)])
    thirdNum = int(before[before.find(",", 9)+2:before.find("'", 9)])
    returning = (firstNum, secNum, thirdNum)
    print(returning)
    return returning

compile()
finish(num)