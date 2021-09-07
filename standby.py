import pandas as pd
import os
import time
import random
import subprocess
import sys
#sys.path.append('/home/pi/Desktop/globals/')
sys.path.append('/Users/s1034274/Desktop/globals/')
from constants import path


color = (255, 255, 255)

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
    global color, songSequence
    red = 0.0
    green = 0.0
    blue = 0.0
    count = 0
    factor = 51.0

    while count < 15:
        while (red < 255):
            red+=factor
            if (blue > 0): 
                blue-=factor

            songSequence = songSequence.append({
                        'red Left':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'red Middle':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'red Right':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'orange Left':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'orange Middle':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'orange Right':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'white Left':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'white Middle':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'white Right':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'yellow Left':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'yellow Middle':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'yellow Right':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'green Left':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'green Middle':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'green Right':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'blue Left':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'blue Middle':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'blue Right':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")"}, ignore_index=True)
            print("(" + str(red) + ", " + str(green) + ", " + str(blue) + ")" + " " + "(" + str(red) + ", " + str(green) + ", " + str(blue) + ")" + " " + "(" + str(red) + ", " + str(green) + ", " + str(blue) + ")")
        while (green < 255):
            green+=factor
            if (red > 0): 
                red-=factor

            songSequence = songSequence.append({
                        'red Left':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'red Middle':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'red Right':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'orange Left':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'orange Middle':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'orange Right':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'white Left':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'white Middle':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'white Right':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'yellow Left':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'yellow Middle':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'yellow Right':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'green Left':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'green Middle':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'green Right':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'blue Left':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'blue Middle':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'blue Right':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")"}, ignore_index=True)
            print("(" + str(red) + ", " + str(green) + ", " + str(blue) + ")" + " " + "(" + str(red) + ", " + str(green) + ", " + str(blue) + ")" + " " + "(" + str(red) + ", " + str(green) + ", " + str(blue) + ")")
        while (blue < 255):
            blue+=factor
            if (green > 0): 
                green-=factor

            songSequence = songSequence.append({
                        'red Left':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'red Middle':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'red Right':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'orange Left':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'orange Middle':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'orange Right':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'white Left':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'white Middle':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'white Right':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'yellow Left':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'yellow Middle':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'yellow Right':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'green Left':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'green Middle':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'green Right':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'blue Left':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'blue Middle':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")",
                        'blue Right':"(" + str(red) + ", " + str(green) + ", " + str(blue) + ")"}, ignore_index=True)
            print("(" + str(red) + ", " + str(green) + ", " + str(blue) + ")" + " " + "(" + str(red) + ", " + str(green) + ", " + str(blue) + ")" + " " + "(" + str(red) + ", " + str(green) + ", " + str(blue) + ")")
        count+=1
        print(count)
        

def finish():
    global color, songSequence
    songSequence.to_excel("standBy.xlsx")


def toTuple(before):
    print(before)
    firstNum = int(before[before.find("'")+2:before.find(",")])
    secNum = int(before[before.find(",")+2:before.find(",", 9)])
    thirdNum = int(before[before.find(",", 9)+2:before.find("'", 9)])
    returning = (firstNum, secNum, thirdNum)
    print(returning)
    return returning

compile()
finish()