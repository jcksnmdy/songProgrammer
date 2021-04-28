import pandas as pd
import pygame
import os
import time
import random
import subprocess
from constants import path
color = (255, 255, 255)
df = pd.read_excel(path + "/songSequence/songTemp.xlsx")
songSequenceRed = pd.DataFrame({
                    'red Inner':[df.loc[(0),'red Inner']],
                    'red Middle':[df.loc[(0),'red Middle']],
                    'red Outer':[df.loc[(0),'red Outer']],})
songSequenceOrange = pd.DataFrame({
                    'orange Inner':[df.loc[(0),'orange Inner']],
                    'orange Middle':[df.loc[(0),'orange Middle']],
                    'orange Outer':[df.loc[(0),'orange Outer']]})
songSequenceWhite = pd.DataFrame({
                    'white Inner':[df.loc[(0),'white Inner']],
                    'white Middle':[df.loc[(0),'white Middle']],
                    'white Outer':[df.loc[(0),'white Outer']]})
songSequenceYellow = pd.DataFrame({
                    'yellow Inner':[df.loc[(0),'yellow Inner']],
                    'yellow Middle':[df.loc[(0),'yellow Middle']],
                    'yellow Outer':[df.loc[(0),'yellow Outer']]})
songSequenceGreen = pd.DataFrame({
                    'green Inner':[df.loc[(0),'green Inner']],
                    'green Middle':[df.loc[(0),'green Middle']],
                    'green Outer':[df.loc[(0),'green Outer']]})
songSequenceBlue = pd.DataFrame({
                    'blue Inner':[df.loc[(0),'blue Inner']],
                    'blue Middle':[df.loc[(0),'blue Middle']],
                    'blue Outer':[df.loc[(0),'blue Outer']]})
                    
def compile(df):
    global color, songSequenceRed, songSequenceOrange, songSequenceWhite, songSequenceYellow, songSequenceGreen, songSequenceBlue
    i = 0
    while (i < len(df)):
        songSequenceRed = songSequenceRed.append({
                    'red Inner':df.loc[(i),'red Inner'],
                    'red Middle':df.loc[(i),'red Middle'],
                    'red Outer':df.loc[(i),'red Outer'],}, ignore_index=True)
        print(str(df.loc[(i),'red Inner']) + "  " + str(i) + "/" + str(len(df)))
        songSequenceOrange = songSequenceOrange.append({
                    'orange Inner':df.loc[(i),'orange Inner'],
                    'orange Middle':df.loc[(i),'orange Middle'],
                    'orange Outer':df.loc[(i),'orange Outer']}, ignore_index=True)
        songSequenceWhite = songSequenceWhite.append({
                    'white Inner':df.loc[(i),'white Inner'],
                    'white Middle':df.loc[(i),'white Middle'],
                    'white Outer':df.loc[(i),'white Outer']}, ignore_index=True)
        songSequenceYellow = songSequenceYellow.append({
                    'yellow Inner':df.loc[(i),'yellow Inner'],
                    'yellow Middle':df.loc[(i),'yellow Middle'],
                    'yellow Outer':df.loc[(i),'yellow Outer']}, ignore_index=True)
        songSequenceGreen = songSequenceGreen.append({
                    'green Inner':df.loc[(i),'green Inner'],
                    'green Middle':df.loc[(i),'green Middle'],
                    'green Outer':df.loc[(i),'green Outer']}, ignore_index=True)
        songSequenceBlue = songSequenceBlue.append({
                    'blue Inner':df.loc[(i),'blue Inner'],
                    'blue Middle':df.loc[(i),'blue Middle'],
                    'blue Outer':df.loc[(i),'blue Outer']}, ignore_index=True)
        i+=1

def finish(songNum):
    global color, songSequenceRed, songSequenceOrange, songSequenceWhite, songSequenceYellow, songSequenceGreen, songSequenceBlue
    songSequenceRed.to_excel(path + "/songs/song" + str(songNum) + "Red.xlsx")
    songSequenceOrange.to_excel(path + "/songs/song" + str(songNum) + "Orange.xlsx")
    songSequenceYellow.to_excel(path + "/songs/song" + str(songNum) + "Yellow.xlsx")
    songSequenceWhite.to_excel(path + "/songs/song" + str(songNum) + "White.xlsx")
    songSequenceGreen.to_excel(path + "/songs/song" + str(songNum) + "Green.xlsx")
    songSequenceBlue.to_excel(path + "/songs/song" + str(songNum) + "Blue.xlsx")


def toTuple(before):
    print(before)
    firstNum = int(before[before.find("'")+2:before.find(",")])
    secNum = int(before[before.find(",")+2:before.find(",", 9)])
    thirdNum = int(before[before.find(",", 9)+2:before.find("'", 9)])
    returning = (firstNum, secNum, thirdNum)
    print(returning)
    return returning