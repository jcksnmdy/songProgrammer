import pandas as pd
import pygame
import os
import time
import random
import subprocess
import signal
import threading
import pygame_widgets
import sys
sys.path.append('/home/pi/Desktop/globals/')
from constants import path
#from compiler import compile, finish

red = (255.0,0.0,0.0)
orange = (255.0,35.0,0.0)
blue = (0.0,0.0,255.0)
yellow = (255.0,128.0,0.0)
green = (0.0,255.0,0.0)
darkRed = (255/2.0,0.0,0.0)
darkOrange = (255/2.0,20.0,0.0)
darkBlue = (0.0,0.0,255/2.0)
darkYellow = (255/2.0,128/2.0,0.0)
darkGreen = (0.0,255/2.0,0.0)
white = (255.0,255.0,255.0)
grey = (128.0,128.0,128.0)
darkGrey = (64.0,64.0,64.0)
black = (0.0,0.0,0.0)

group1 = []
g1Action = ["off", str(white), 7500, 255]
addingToGroup1 = False
group2 = []
g2Action = ["off", str(white), 7500, 255]
addingToGroup2 = False
group3 = []
g3Action = ["off", str(white), 7500, 255]
addingToGroup3 = False
group4 = []
g4Action = ["off", str(white), 7500, 255]
addingToGroup4 = False
group5 = []
g5Action = ["off", str(white), 7500, 255]
addingToGroup5 = False
group6 = []
g6Action = ["off", str(white), 7500, 255]
addingToGroup6 = False
selected = 0
i = 0


## left
redFlagColorleft = red
orangeFlagColorleft = orange
whiteFlagColorleft = white
yellowFlagColorleft = yellow
greenFlagColorleft = green
blueFlagColorleft = blue
## MIDDLE
redFlagColorMiddle = red
orangeFlagColorMiddle = orange
whiteFlagColorMiddle = white
yellowFlagColorMiddle = yellow
greenFlagColorMiddle = green
blueFlagColorMiddle = blue
## Right
redFlagColorRight = red
orangeFlagColorRight = orange
whiteFlagColorRight = white
yellowFlagColorRight = yellow
greenFlagColorRight = green
blueFlagColorRight = blue

songSequence = pd.DataFrame({
                    'red Left':redFlagColorleft,
                    'red Middle':redFlagColorMiddle,
                    'red Right':redFlagColorRight,
                    'orange Left':orangeFlagColorleft,
                    'orange Middle':orangeFlagColorMiddle,
                    'orange Right':orangeFlagColorRight,
                    'yellow Left':yellowFlagColorleft,
                    'yellow Middle':yellowFlagColorMiddle,
                    'yellow Right':yellowFlagColorRight,
                    'white Left':whiteFlagColorleft,
                    'white Middle':whiteFlagColorMiddle,
                    'white Right':whiteFlagColorRight,
                    'green Left':greenFlagColorleft,
                    'green Middle':greenFlagColorMiddle,
                    'green Right':greenFlagColorRight,
                    'blue Left':blueFlagColorleft,
                    'blue Middle':blueFlagColorMiddle,
                    'blue Right':blueFlagColorRight})

g1Action[1] = white
g2Action[1] = white
g3Action[1] = white
g4Action[1] = white
g5Action[1] = white
g6Action[1] = white

songSequence = songSequence.append({
                    'red Left':redFlagColorleft,
                    'red Middle':redFlagColorMiddle,
                    'red Right':redFlagColorRight,
                    'orange Left':orangeFlagColorleft,
                    'orange Middle':orangeFlagColorMiddle,
                    'orange Right':orangeFlagColorRight,
                    'yellow Left':yellowFlagColorleft,
                    'yellow Middle':yellowFlagColorMiddle,
                    'yellow Right':yellowFlagColorRight,
                    'white Left':whiteFlagColorleft,
                    'white Middle':whiteFlagColorMiddle,
                    'white Right':whiteFlagColorRight,
                    'green Left':greenFlagColorleft,
                    'green Middle':greenFlagColorMiddle,
                    'green Right':greenFlagColorRight,
                    'blue Left':blueFlagColorleft,
                    'blue Middle':blueFlagColorMiddle,
                    'blue Right':blueFlagColorRight}, ignore_index=True)
g1Color = grey
g2Color = grey
g3Color = grey
g4Color = grey
g5Color = grey
g6Color = grey

pygame.init()
screen = pygame.display.set_mode((750, 500))
clock = pygame.time.Clock()
pygame.display.set_caption("Programmer")

## left
redFlagleftOrig = (270, 330, 39, 39)
orangeFlagleftOrig = (600, 270, 39, 39)
whiteFlagleftOrig = (490, 190, 39, 39)
yellowFlagleftOrig = (300, 220, 39, 39)
greenFlagleftOrig = (390, 160, 39, 39)
blueFlagleftOrig = (620, 100, 39, 39)

redFlagleft = pygame.Rect(redFlagleftOrig)
orangeFlagleft = pygame.Rect(orangeFlagleftOrig)
whiteFlagleft = pygame.Rect(whiteFlagleftOrig)
yellowFlagleft = pygame.Rect(yellowFlagleftOrig)
greenFlagleft = pygame.Rect(greenFlagleftOrig)
blueFlagleft = pygame.Rect(blueFlagleftOrig)
##MIDDLE
redFlagMiddleOrig = (260, 320, 59, 59)
orangeFlagMiddleOrig = (580, 270, 59, 59)
whiteFlagMiddleOrig = (480, 180, 59, 59)
yellowFlagMiddleOrig = (290, 210, 59, 59)
greenFlagMiddleOrig = (380, 150, 59, 59)
blueFlagMiddleOrig = (610, 90, 59, 59)

redFlagMiddle = pygame.Rect(redFlagMiddleOrig)
orangeFlagMiddle = pygame.Rect(orangeFlagMiddleOrig)
whiteFlagMiddle = pygame.Rect(whiteFlagMiddleOrig)
yellowFlagMiddle = pygame.Rect(yellowFlagMiddleOrig)
greenFlagMiddle = pygame.Rect(greenFlagMiddleOrig)
blueFlagMiddle = pygame.Rect(blueFlagMiddleOrig)
##Right
redFlagRightOrig = (250, 310, 79, 79)
orangeFlagRightOrig = (580, 260, 79, 79)
whiteFlagRightOrig = (470, 170, 79, 79)
yellowFlagRightOrig = (280, 200, 79, 79)
greenFlagRightOrig = (370, 140, 79, 79)
blueFlagRightOrig = (600, 80, 79, 79)

redFlagRight = pygame.Rect(redFlagRightOrig)
orangeFlagRight = pygame.Rect(orangeFlagRightOrig)
whiteFlagRight = pygame.Rect(whiteFlagRightOrig)
yellowFlagRight = pygame.Rect(yellowFlagRightOrig)
greenFlagRight = pygame.Rect(greenFlagRightOrig)
blueFlagRight = pygame.Rect(blueFlagRightOrig)
timer = time.time()
pausePoint = 0
playing = False
# Load the programmer
songNumG = 1
def program(songNum):
    global timer, songSequence, i, songNumG
    songNumG = songNum
    red = (255,0,0)
    orange = (255,128,0)
    blue = (0,0,255)
    yellow = (255,255,0)
    green = (0,255,0)
    white = (255,255,255)
    grey = (128,128,128)
    black = (0,0,0)
    state = 0
    pygame.mixer.music.load(path + "/songs/song" + str(songNum) + ".mp3")
    #pygame.mixer.music.load("/home/pi/Desktop/coreLightShow/songs/song" + str(songNum) + ".mp3")

    while True:
        
        screen.fill([0,0,0])
        keys = pygame.key.get_pressed()
        # determine if a letter key was pressed 
        # if keys[pygame.K_1]:
        #     redFlagColorleft = (255, 0, 0)
        #     redFlagColorMiddle = (255, 0, 0)
        #     redFlagColorRight = (255, 0, 0)
        #     #print("Red")
        # else:
        #     redFlagColorleft = (128, 128, 128)
        #     redFlagColorMiddle = (128, 128, 128)
        #     redFlagColorRight = (128, 128, 128)
        
        for event in pygame.event.get():
        
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                pygame.quit()
                return

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                if save.collidepoint(mouse_pos):
                    print("Saved")
                    songSequence.to_excel("songTemp.xlsx")

                
                checkEvent(mouse_pos)
        if (playing):
            i+=1
            if (i%2==0):
                songSequence = songSequence.append({
                    'red Left':redFlagColorleft,
                    'red Middle':redFlagColorMiddle,
                    'red Right':redFlagColorRight,
                    'orange Left':orangeFlagColorleft,
                    'orange Middle':orangeFlagColorMiddle,
                    'orange Right':orangeFlagColorRight,
                    'yellow Left':yellowFlagColorleft,
                    'yellow Middle':yellowFlagColorMiddle,
                    'yellow Right':yellowFlagColorRight,
                    'white Left':whiteFlagColorleft,
                    'white Middle':whiteFlagColorMiddle,
                    'white Right':whiteFlagColorRight,
                    'green Left':greenFlagColorleft,
                    'green Middle':greenFlagColorMiddle,
                    'green Right':greenFlagColorRight,
                    'blue Left':blueFlagColorleft,
                    'blue Middle':blueFlagColorMiddle,
                    'blue Right':blueFlagColorRight}, ignore_index=True)

        lightsOptions(songNum)
        drawRings()   
        pygame.display.flip()
        
        clock.tick(60)


pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 28)

songName = font.render('Hit Me', True, white)
timeElapsed = font.render('0:00', True, black)

indicateY = font.render('Y', True, white)
indicateO = font.render('O', True, white)

song = 1

upperAstetic = pygame.Rect(0, 0, 750, 70)
middleAstetic = pygame.Rect(0, 0, 230, 500)
lowerAstetic = pygame.Rect(0, 400, 750, 100)

save = pygame.Rect(515, 40, 99, 25)
saveText = font.render('Save', True, black)

pulseButton = pygame.Rect(10, 10, 79, 79)
sparkleButton = pygame.Rect(90, 10, 79, 79)
fadeButton = pygame.Rect(170, 10, 79, 79)
blinkButton = pygame.Rect(10, 90, 79, 79)
onButton = pygame.Rect(90, 90, 79, 79)
offButton = pygame.Rect(170, 90, 79, 79)


pulseButtonText = font.render('Pulse', True, black)
sparkleButtonText = font.render('Spar.', True, black)
fadeButtonText = font.render('Fade', True, black)
blinkButtonText = font.render('Blink', True, black)
onButtonText = font.render('On', True, black)
offButtonText = font.render('Off', True, black)

speedText = font.render('Speed', True, black)

whiteColor = pygame.Rect(10, 175, 39, 39)
greenColor = pygame.Rect(55, 175, 39, 39)
yellowColor = pygame.Rect(100, 175, 39, 39)
blueColor = pygame.Rect(145, 175, 39, 39)
orangeColor = pygame.Rect(10, 220, 39, 39)
redColor = pygame.Rect(55, 220, 39, 39)

slider = pygame_widgets.Slider(screen, 10, 300, 200, 20, min=1, max=15000, step=1)
output = font.render("1900", True, black)
sliderIntensity = pygame_widgets.Slider(screen, 10, 380, 200, 20, min=25, max=255, step=1)
outputIntensity = font.render("255", True, black)

intensityText = font.render("Brightness: " + str(255), True, black)

playHeadText = font.render("Playhead: " + str(0), True, black)
left = pygame.Rect(250, 430, 39, 39)
leftText = font.render("<", True, black)
right = pygame.Rect(500, 430, 39, 39)
rightText = font.render(">", True, black)
place = 0

pause = pygame.Rect(650, 430, 39, 39)
pauseText = font.render("||", True, black)
play = pygame.Rect(600, 430, 39, 39)
playText = font.render("|>", True, black)

g1 = pygame.Rect(255, 75, 39, 39)
g1Text = font.render("G1", True, black)
g2 = pygame.Rect(300, 75, 39, 39)
g2Text = font.render("G2", True, black)
g3 = pygame.Rect(345, 75, 39, 39)
g3Text = font.render("G3", True, black)
g4 = pygame.Rect(390, 75, 39, 39)
g4Text = font.render("G4", True, black)
g5 = pygame.Rect(435, 75, 39, 39)
g5Text = font.render("G5", True, black)
g6 = pygame.Rect(480, 75, 39, 39)
g6Text = font.render("G6", True, black)

def fadeHelper(before, power):
    returning = ((before[0]*power)/255, (before[1]*power)/255, (before[2]*power)/255)
    return returning

def lightsOptions(songNum):
    pygame.draw.rect(screen, darkGrey, upperAstetic)  # draw button
    pygame.draw.rect(screen, darkGrey, middleAstetic)  # draw button
    pygame.draw.rect(screen, darkGrey, lowerAstetic)  # draw button
    pygame.draw.rect(screen, g1Color, g1)  # draw button
    screen.blit(g1Text, g1)
    pygame.draw.rect(screen, g2Color, g2)  # draw button
    screen.blit(g2Text, g2)
    pygame.draw.rect(screen, g3Color, g3)  # draw button
    screen.blit(g3Text, g3)
    pygame.draw.rect(screen, g4Color, g4)  # draw button
    screen.blit(g4Text, g4)
    pygame.draw.rect(screen, g5Color, g5)  # draw button
    screen.blit(g5Text, g5)
    pygame.draw.rect(screen, g6Color, g6)  # draw button
    screen.blit(g6Text, g6)
    global songName, place, timer, pausePoint
    playHeadText = font.render(str(place+int(pygame.mixer.music.get_pos()/1000)), True, white)
    timeElapsed = font.render(str(place+int(pygame.mixer.music.get_pos()/1000)), True, black)
    if (songNum == 1):
        songName = font.render('Serious', True, white)
    elif (songNum == 2):
        songName = font.render('Thunderstruck', True, white)
    elif (songNum == 3):
        songName = font.render('Eye of the Tiger', True, white)
    elif (songNum == 4):
        songName = font.render('Hit Me', True, white)
    elif (songNum == 5):
        songName = font.render('Despacito', True, white)
    elif (songNum == 6):
        songName = font.render('Beat It', True, white)
    elif (songNum == 7):
        songName = font.render('Thriller', True, white)


    screen.blit(songName, (260, 10))
    screen.blit(timeElapsed, (270, 40))

    pygame.draw.rect(screen, white, save)  # draw button
    screen.blit(saveText, save)

    screen.blit(speedText, (10, 265))
    slider.listen(pygame.event.get())
    slider.draw()
    sliderIntensity.listen(pygame.event.get())
    sliderIntensity.draw()

    if addingToGroup1:
        g1Action[2] = slider.getValue()
        output = font.render(str(slider.getValue()), True, black)
        screen.blit(output, (10, 325))
        g1Action[3] = sliderIntensity.getValue()
        outputIntensity = font.render("Brightness: " + str(g1Action[3]), True, black)
        screen.blit(outputIntensity, (10, 420))
        g1Action[1] = fadeHelper(colorSelected, g1Action[3])
        if g1Action[0]=="pulse":
            pygame.draw.rect(screen, white, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g1Action[0]=="blink":
            pygame.draw.rect(screen, white, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g1Action[0]=="fade":
            pygame.draw.rect(screen, white, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g1Action[0]=="sparkle":
            pygame.draw.rect(screen, white, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g1Action[0]=="on":
            pygame.draw.rect(screen, white, onButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g1Action[0]=="off":
            pygame.draw.rect(screen, white, offButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            g1Action[1] = (128,128,128)
        else:
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        
        if g1Action[1]==fadeHelper(white, g1Action[3]):
            pygame.draw.rect(screen, white, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g1Action[1]==fadeHelper(red, g1Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, red, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g1Action[1]==fadeHelper(blue, g1Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, blue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g1Action[1]==fadeHelper(green, g1Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, green, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g1Action[1]==fadeHelper(yellow, g1Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, yellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g1Action[1]==fadeHelper(orange, g1Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, orange, orangeColor)  # draw button
        else:
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button

    elif addingToGroup2:
        g2Action[2] = slider.getValue()
        output = font.render(str(slider.getValue()), True, black)
        screen.blit(output, (10, 325))
        g2Action[3] = sliderIntensity.getValue()
        outputIntensity = font.render("Brightness: " + str(g2Action[3]), True, black)
        g2Action[1] = fadeHelper(colorSelected, g2Action[3])
        outputIntensity = font.render(str(g2Action[3]), True, black)
        screen.blit(outputIntensity, (10, 420))
        if g2Action[0]=="pulse":
            pygame.draw.rect(screen, white, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g2Action[0]=="blink":
            pygame.draw.rect(screen, white, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g2Action[0]=="fade":
            pygame.draw.rect(screen, white, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g2Action[0]=="sparkle":
            pygame.draw.rect(screen, white, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g2Action[0]=="on":
            pygame.draw.rect(screen, white, onButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g2Action[0]=="off":
            pygame.draw.rect(screen, white, offButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            g2Action[1] = (128,128,128)
        else:
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button

        if g2Action[1]==fadeHelper(white, g2Action[3]):
            pygame.draw.rect(screen, white, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g2Action[1]==fadeHelper(red, g2Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, red, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g2Action[1]==fadeHelper(blue, g2Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, blue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g2Action[1]==fadeHelper(green, g2Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, green, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g2Action[1]==fadeHelper(yellow, g2Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, yellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g2Action[1]==fadeHelper(orange, g2Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, orange, orangeColor)  # draw button
        else:
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
    
    elif addingToGroup3:
        g3Action[2] = slider.getValue()
        output = font.render(str(slider.getValue()), True, black)
        screen.blit(output, (10, 325))
        g3Action[3] = sliderIntensity.getValue()
        outputIntensity = font.render("Brightness: " + str(g3Action[3]), True, black)
        g3Action[1] = fadeHelper(colorSelected, g1Action[3])
        outputIntensity = font.render(str(g3Action[3]), True, black)
        screen.blit(outputIntensity, (10, 420))
        if g3Action[0]=="pulse":
            pygame.draw.rect(screen, white, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g3Action[0]=="blink":
            pygame.draw.rect(screen, white, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g3Action[0]=="fade":
            pygame.draw.rect(screen, white, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g3Action[0]=="sparkle":
            pygame.draw.rect(screen, white, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g3Action[0]=="on":
            pygame.draw.rect(screen, white, onButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g3Action[0]=="off":
            pygame.draw.rect(screen, white, offButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            g3Action[1] = (128,128,128)
        else:
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
            
        if g3Action[1]==fadeHelper(white, g3Action[3]):
            pygame.draw.rect(screen, white, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g3Action[1]==fadeHelper(red, g3Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, red, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g3Action[1]==fadeHelper(blue, g3Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, blue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g3Action[1]==fadeHelper(green, g3Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, green, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g3Action[1]==fadeHelper(yellow, g3Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, yellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g3Action[1]==fadeHelper(orange, g3Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, orange, orangeColor)  # draw button
        else:
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
    
    elif addingToGroup4:
        g4Action[2] = slider.getValue()
        output = font.render(str(slider.getValue()), True, black)
        screen.blit(output, (10, 325))
        g4Action[3] = sliderIntensity.getValue()
        outputIntensity = font.render("Brightness: " + str(g4Action[3]), True, black)
        g4Action[1] = fadeHelper(colorSelected, g1Action[3])
        outputIntensity = font.render(str(g4Action[3]), True, black)
        screen.blit(outputIntensity, (10, 420))
        if g4Action[0]=="pulse":
            pygame.draw.rect(screen, white, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g4Action[0]=="blink":
            pygame.draw.rect(screen, white, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g4Action[0]=="fade":
            pygame.draw.rect(screen, white, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g4Action[0]=="sparkle":
            pygame.draw.rect(screen, white, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g4Action[0]=="on":
            pygame.draw.rect(screen, white, onButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g4Action[0]=="off":
            pygame.draw.rect(screen, white, offButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            g4Action[1] = (128,128,128)
        else:
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
            
        if g4Action[1]==fadeHelper(white, g4Action[3]):
            pygame.draw.rect(screen, white, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g4Action[1]==fadeHelper(red, g4Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, red, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g4Action[1]==fadeHelper(blue, g4Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, blue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g4Action[1]==fadeHelper(green, g4Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, green, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g4Action[1]==fadeHelper(yellow, g4Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, yellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g4Action[1]==fadeHelper(orange, g4Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, orange, orangeColor)  # draw button
        else:
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
    
    elif addingToGroup5:
        g5Action[2] = slider.getValue()
        output = font.render(str(slider.getValue()), True, black)
        screen.blit(output, (10, 325))
        g5Action[3] = sliderIntensity.getValue()
        outputIntensity = font.render("Brightness: " + str(g5Action[3]), True, black)
        g5Action[1] = fadeHelper(colorSelected, g1Action[3])
        outputIntensity = font.render(str(g5Action[3]), True, black)
        screen.blit(outputIntensity, (10, 420))

        if g5Action[0]=="pulse":
            pygame.draw.rect(screen, white, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g5Action[0]=="blink":
            pygame.draw.rect(screen, white, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g5Action[0]=="fade":
            pygame.draw.rect(screen, white, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g5Action[0]=="sparkle":
            pygame.draw.rect(screen, white, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g5Action[0]=="on":
            pygame.draw.rect(screen, white, onButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g5Action[0]=="off":
            pygame.draw.rect(screen, white, offButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            g5Action[1] = (128,128,128)
        else:
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
            
        if g5Action[1]==fadeHelper(white, g5Action[3]):
            pygame.draw.rect(screen, white, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g5Action[1]==fadeHelper(red, g5Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, red, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g5Action[1]==fadeHelper(blue, g5Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, blue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g5Action[1]==fadeHelper(green, g5Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, green, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g5Action[1]==fadeHelper(yellow, g5Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, yellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g5Action[1]==fadeHelper(orange, g5Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, orange, orangeColor)  # draw button
        else:
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
    
    elif addingToGroup6:
        g6Action[2] = slider.getValue()
        output = font.render(str(slider.getValue()), True, black)
        screen.blit(output, (10, 325))
        g6Action[3] = sliderIntensity.getValue()
        outputIntensity = font.render("Brightness: " + str(g6Action[3]), True, black)
        g6Action[1] = fadeHelper(colorSelected, g1Action[3])
        outputIntensity = font.render(str(g6Action[3]), True, black)
        screen.blit(outputIntensity, (10, 420))
        if g6Action[0]=="pulse":
            pygame.draw.rect(screen, white, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g6Action[0]=="blink":
            pygame.draw.rect(screen, white, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g6Action[0]=="fade":
            pygame.draw.rect(screen, white, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g6Action[0]=="sparkle":
            pygame.draw.rect(screen, white, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g6Action[0]=="on":
            pygame.draw.rect(screen, white, onButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
        elif g6Action[0]=="off":
            pygame.draw.rect(screen, white, offButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, onButton)  # draw button
            g6Action[1] = (128,128,128)
        else:
            pygame.draw.rect(screen, grey, onButton)  # draw button
            pygame.draw.rect(screen, grey, pulseButton)  # draw button
            pygame.draw.rect(screen, grey, blinkButton)  # draw button
            pygame.draw.rect(screen, grey, fadeButton)  # draw button
            pygame.draw.rect(screen, grey, sparkleButton)  # draw button
            pygame.draw.rect(screen, grey, offButton)  # draw button
            
        if g6Action[1]==fadeHelper(white, g6Action[3]):
            pygame.draw.rect(screen, white, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g6Action[1]==fadeHelper(red, g6Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, red, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g6Action[1]==fadeHelper(blue, g6Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, blue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g6Action[1]==fadeHelper(green, g6Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, green, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g6Action[1]==fadeHelper(yellow, g6Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, yellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
        elif g6Action[1]==fadeHelper(orange, g6Action[3]):
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, orange, orangeColor)  # draw button
        else:
            pygame.draw.rect(screen, grey, whiteColor)  # draw button
            pygame.draw.rect(screen, darkRed, redColor)  # draw button
            pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
            pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
            pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
            pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button

    else:
        pygame.draw.rect(screen, grey, pulseButton)  # draw button
        pygame.draw.rect(screen, grey, offButton)  # draw button
        pygame.draw.rect(screen, grey, blinkButton)  # draw button
        pygame.draw.rect(screen, grey, fadeButton)  # draw button
        pygame.draw.rect(screen, grey, sparkleButton)  # draw button
        pygame.draw.rect(screen, grey, onButton)  # draw button
        
        pygame.draw.rect(screen, grey, whiteColor)  # draw button
        pygame.draw.rect(screen, darkRed, redColor)  # draw button
        pygame.draw.rect(screen, darkGreen, greenColor)  # draw button
        pygame.draw.rect(screen, darkYellow, yellowColor)  # draw button
        pygame.draw.rect(screen, darkBlue, blueColor)  # draw button
        pygame.draw.rect(screen, darkOrange, orangeColor)  # draw button
    
    screen.blit(pulseButtonText, pulseButton)
    screen.blit(indicateY, yellowColor)
    screen.blit(indicateO, orangeColor)
    screen.blit(offButtonText, offButton)
    screen.blit(blinkButtonText, blinkButton)
    screen.blit(fadeButtonText, fadeButton)
    screen.blit(sparkleButtonText, sparkleButton)
    screen.blit(onButtonText, onButton)
    pygame.draw.rect(screen, white, left)  # draw button
    pygame.draw.rect(screen, white, right)  # draw button
    playHeadText = font.render("Playhead: " + str(place), True, black)
    screen.blit(playHeadText, (300, 430))
    screen.blit(leftText, left)
    screen.blit(rightText, right)
    pygame.draw.rect(screen, white, pause)  # draw button
    pygame.draw.rect(screen, white, play)  # draw button
    screen.blit(pauseText, pause)
    screen.blit(playText, play)

def toTuple(before):
    print(before)
    firstNum = int(before[before.find("'")+2:before.find(",")])
    secNum = int(before[before.find(",")+2:before.find(",", 9)])
    thirdNum = int(before[before.find(",", 9)+2:before.find("'", 9)])
    returning = (firstNum, secNum, thirdNum)
    print(returning)
    return returning

a = 100
def blinkHelperG1(delay):
    global a
    a+=1
    if ((a/75)>=(delay/1000)):
        if ((a/75)>=((delay+300)/1000)):
            a=100
        return True
    else:
        return False
b = 100
def blinkHelperG2(delay):
    global b
    b+=1
    if ((b/75)>=(delay/1000)):
        if ((b/75)>=((delay+300)/1000)):
            b=100
        return True
    else:
        return False
c = 100
def blinkHelperG3(delay):
    global c
    c+=1
    if ((c/75)>=(delay/1000)):
        if ((c/75)>=((delay+300)/1000)):
            c=100
        return True
    else:
        return False
d = 100
def blinkHelperG4(delay):
    global d
    d+=1
    if ((d/75)>=(delay/1000)):
        if ((d/75)>=((delay+300)/1000)):
            d=100
        return True
    else:
        return False
e = 100
def blinkHelperG5(delay):
    global e
    e+=1
    if ((e/75)>=(delay/1000)):
        if ((e/75)>=((delay+300)/1000)):
            e=100
        return True
    else:
        return False
f = 100
def blinkHelperG6(delay):
    global f
    f+=1
    if ((f/75)>=(delay/1000)):
        if ((f/75)>=((delay+300)/1000)):
            f=100
        return True
    else:
        return False

def drawRings():
    global g1Action, colorSelected, group1, i, redFlagColorleft, redFlagColorMiddle, redFlagColorRight, orangeFlagColorleft, orangeFlagColorMiddle, orangeFlagColorRight, yellowFlagColorleft, yellowFlagColorMiddle, yellowFlagColorRight, greenFlagColorleft, greenFlagColorMiddle, greenFlagColorRight, whiteFlagColorleft, whiteFlagColorMiddle, whiteFlagColorRight, blueFlagColorleft, blueFlagColorMiddle, blueFlagColorRight
    color = (0.0, 0.0, 0.0)
    if (1 in group1) and (addingToGroup1 or playing):
        working = g1Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG1(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]
        redFlagColorRight = color
        redFlagColorMiddle = color
        redFlagColorleft = color
        pygame.draw.rect(screen, redFlagColorRight, redFlagRight)  # draw button
        pygame.draw.rect(screen, redFlagColorMiddle, redFlagMiddle)  # draw button
        pygame.draw.rect(screen, redFlagColorleft, redFlagleft)  # draw button
    elif (1 in group2) and (addingToGroup2 or playing):
        working = g2Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG2(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        redFlagColorRight = color
        redFlagColorMiddle = color
        redFlagColorleft = color
        pygame.draw.rect(screen, redFlagColorRight, redFlagRight)  # draw button
        pygame.draw.rect(screen, redFlagColorMiddle, redFlagMiddle)  # draw button
        pygame.draw.rect(screen, redFlagColorleft, redFlagleft)  # draw button
    elif (1 in group3) and (addingToGroup3 or playing):
        working = g3Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG3(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        redFlagColorRight = color
        redFlagColorMiddle = color
        redFlagColorleft = color
        pygame.draw.rect(screen, redFlagColorRight, redFlagRight)  # draw button
        pygame.draw.rect(screen, redFlagColorMiddle, redFlagMiddle)  # draw button
        pygame.draw.rect(screen, redFlagColorleft, redFlagleft)  # draw button
    elif (1 in group4) and (addingToGroup4 or playing):
        working = g4Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG4(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        redFlagColorRight = color
        redFlagColorMiddle = color
        redFlagColorleft = color
        pygame.draw.rect(screen, redFlagColorRight, redFlagRight)  # draw button
        pygame.draw.rect(screen, redFlagColorMiddle, redFlagMiddle)  # draw button
        pygame.draw.rect(screen, redFlagColorleft, redFlagleft)  # draw button
    elif (1 in group5) and (addingToGroup5 or playing):
        working = g5Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG5(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]
        if (working[0]=="on"):
            color = working[1]

        redFlagColorRight = color
        redFlagColorMiddle = color
        redFlagColorleft = color
        pygame.draw.rect(screen, redFlagColorRight, redFlagRight)  # draw button
        pygame.draw.rect(screen, redFlagColorMiddle, redFlagMiddle)  # draw button
        pygame.draw.rect(screen, redFlagColorleft, redFlagleft)  # draw button
    elif (1 in group6) and (addingToGroup6 or playing):
        working = g6Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG6(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        redFlagColorRight = color
        redFlagColorMiddle = color
        redFlagColorleft = color
        pygame.draw.rect(screen, redFlagColorRight, redFlagRight)  # draw button
        pygame.draw.rect(screen, redFlagColorMiddle, redFlagMiddle)  # draw button
        pygame.draw.rect(screen, redFlagColorleft, redFlagleft)  # draw button
    else:
        pygame.draw.rect(screen, darkGrey, redFlagRight)  # draw button
        pygame.draw.rect(screen, darkGrey, redFlagMiddle)  # draw button
        pygame.draw.rect(screen, darkGrey, redFlagleft)  # draw button
    color = (0.0, 0.0, 0.0)
    if (2 in group1) and (addingToGroup1 or playing):
        working = g1Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG1(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        orangeFlagColorRight = color
        orangeFlagColorMiddle = color
        orangeFlagColorleft = color
        pygame.draw.rect(screen, orangeFlagColorRight, orangeFlagRight)  # draw button
        pygame.draw.rect(screen, orangeFlagColorMiddle, orangeFlagMiddle)  # draw button
        pygame.draw.rect(screen, orangeFlagColorleft, orangeFlagleft)  # draw button
    elif (2 in group2) and (addingToGroup2 or playing):
        working = g2Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG2(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        orangeFlagColorRight = color
        orangeFlagColorMiddle = color
        orangeFlagColorleft = color
        pygame.draw.rect(screen, orangeFlagColorRight, orangeFlagRight)  # draw button
        pygame.draw.rect(screen, orangeFlagColorMiddle, orangeFlagMiddle)  # draw button
        pygame.draw.rect(screen, orangeFlagColorleft, orangeFlagleft)  # draw button
    elif (2 in group3) and (addingToGroup3 or playing):
        working = g3Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG3(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        orangeFlagColorRight = color
        orangeFlagColorMiddle = color
        orangeFlagColorleft = color
        pygame.draw.rect(screen, orangeFlagColorRight, orangeFlagRight)  # draw button
        pygame.draw.rect(screen, orangeFlagColorMiddle, orangeFlagMiddle)  # draw button
        pygame.draw.rect(screen, orangeFlagColorleft, orangeFlagleft)  # draw button
    elif (2 in group4) and (addingToGroup4 or playing):
        working = g4Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG4(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        orangeFlagColorRight = color
        orangeFlagColorMiddle = color
        orangeFlagColorleft = color
        pygame.draw.rect(screen, orangeFlagColorRight, orangeFlagRight)  # draw button
        pygame.draw.rect(screen, orangeFlagColorMiddle, orangeFlagMiddle)  # draw button
        pygame.draw.rect(screen, orangeFlagColorleft, orangeFlagleft)  # draw button
    elif (2 in group5) and (addingToGroup5 or playing):
        working = g5Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG5(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        orangeFlagColorRight = color
        orangeFlagColorMiddle = color
        orangeFlagColorleft = color
        pygame.draw.rect(screen, orangeFlagColorRight, orangeFlagRight)  # draw button
        pygame.draw.rect(screen, orangeFlagColorMiddle, orangeFlagMiddle)  # draw button
        pygame.draw.rect(screen, orangeFlagColorleft, orangeFlagleft)  # draw button
    elif (2 in group6) and (addingToGroup6 or playing):
        working = g6Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG6(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        orangeFlagColorRight = color
        orangeFlagColorMiddle = color
        orangeFlagColorleft = color
        pygame.draw.rect(screen, orangeFlagColorRight, orangeFlagRight)  # draw button
        pygame.draw.rect(screen, orangeFlagColorMiddle, orangeFlagMiddle)  # draw button
        pygame.draw.rect(screen, orangeFlagColorleft, orangeFlagleft)  # draw button
    else:
        pygame.draw.rect(screen, darkGrey, orangeFlagRight)  # draw button
        pygame.draw.rect(screen, darkGrey, orangeFlagMiddle)  # draw button
        pygame.draw.rect(screen, darkGrey, orangeFlagleft)  # draw button
    color = (0.0, 0.0, 0.0)
    if (3 in group1) and (addingToGroup1 or playing):
        working = g1Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG1(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], g3Action[3])
        if (working[0]=="on"):
            color = working[1]

        yellowFlagColorRight = color
        yellowFlagColorMiddle = color
        yellowFlagColorleft = color
        pygame.draw.rect(screen, yellowFlagColorRight, yellowFlagRight)  # draw button
        pygame.draw.rect(screen, yellowFlagColorMiddle, yellowFlagMiddle)  # draw button
        pygame.draw.rect(screen, yellowFlagColorleft, yellowFlagleft)  # draw button
    elif (3 in group2) and (addingToGroup2 or playing):
        working = g2Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG2(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], g3Action[3])
        if (working[0]=="on"):
            color = working[1]

        yellowFlagColorRight = color
        yellowFlagColorMiddle = color
        yellowFlagColorleft = color
        pygame.draw.rect(screen, yellowFlagColorRight, yellowFlagRight)  # draw button
        pygame.draw.rect(screen, yellowFlagColorMiddle, yellowFlagMiddle)  # draw button
        pygame.draw.rect(screen, yellowFlagColorleft, yellowFlagleft)  # draw button
    elif (3 in group3) and (addingToGroup3 or playing):
        working = g3Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG3(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], g3Action[3])
        if (working[0]=="on"):
            color = working[1]

        yellowFlagColorRight = color
        yellowFlagColorMiddle = color
        yellowFlagColorleft = color
        pygame.draw.rect(screen, yellowFlagColorRight, yellowFlagRight)  # draw button
        pygame.draw.rect(screen, yellowFlagColorMiddle, yellowFlagMiddle)  # draw button
        pygame.draw.rect(screen, yellowFlagColorleft, yellowFlagleft)  # draw button
    elif (3 in group4) and (addingToGroup4 or playing):
        working = g4Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG4(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], g3Action[3])
        if (working[0]=="on"):
            color = working[1]

        yellowFlagColorRight = color
        yellowFlagColorMiddle = color
        yellowFlagColorleft = color
        pygame.draw.rect(screen, yellowFlagColorRight, yellowFlagRight)  # draw button
        pygame.draw.rect(screen, yellowFlagColorMiddle, yellowFlagMiddle)  # draw button
        pygame.draw.rect(screen, yellowFlagColorleft, yellowFlagleft)  # draw button
    elif (3 in group5) and (addingToGroup5 or playing):
        working = g5Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG5(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], g3Action[3])
        if (working[0]=="on"):
            color = working[1]

        yellowFlagColorRight = color
        yellowFlagColorMiddle = color
        yellowFlagColorleft = color
        pygame.draw.rect(screen, yellowFlagColorRight, yellowFlagRight)  # draw button
        pygame.draw.rect(screen, yellowFlagColorMiddle, yellowFlagMiddle)  # draw button
        pygame.draw.rect(screen, yellowFlagColorleft, yellowFlagleft)  # draw button
    elif (3 in group6) and (addingToGroup6 or playing):
        working = g6Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG6(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], g3Action[3])
        if (working[0]=="on"):
            color = working[1]

        yellowFlagColorRight = color
        yellowFlagColorMiddle = color
        yellowFlagColorleft = color
        pygame.draw.rect(screen, yellowFlagColorRight, yellowFlagRight)  # draw button
        pygame.draw.rect(screen, yellowFlagColorMiddle, yellowFlagMiddle)  # draw button
        pygame.draw.rect(screen, yellowFlagColorleft, yellowFlagleft)  # draw button
    else:
        pygame.draw.rect(screen, darkGrey, yellowFlagRight)  # draw button
        pygame.draw.rect(screen, darkGrey, yellowFlagMiddle)  # draw button
        pygame.draw.rect(screen, darkGrey, yellowFlagleft)  # draw button
    color = (0.0, 0.0, 0.0)
    if (4 in group1) and (addingToGroup1 or playing):
        working = g1Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG1(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        whiteFlagColorRight = color
        whiteFlagColorMiddle = color
        whiteFlagColorleft = color
        pygame.draw.rect(screen, whiteFlagColorRight, whiteFlagRight)  # draw button
        pygame.draw.rect(screen, whiteFlagColorMiddle, whiteFlagMiddle)  # draw button
        pygame.draw.rect(screen, whiteFlagColorleft, whiteFlagleft)  # draw button
    elif (4 in group2) and (addingToGroup2 or playing):
        working = g2Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG2(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        whiteFlagColorRight = color
        whiteFlagColorMiddle = color
        whiteFlagColorleft = color
        pygame.draw.rect(screen, whiteFlagColorRight, whiteFlagRight)  # draw button
        pygame.draw.rect(screen, whiteFlagColorMiddle, whiteFlagMiddle)  # draw button
        pygame.draw.rect(screen, whiteFlagColorleft, whiteFlagleft)  # draw button
    elif (4 in group3) and (addingToGroup3 or playing):
        working = g3Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG3(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        whiteFlagColorRight = color
        whiteFlagColorMiddle = color
        whiteFlagColorleft = color
        pygame.draw.rect(screen, whiteFlagColorRight, whiteFlagRight)  # draw button
        pygame.draw.rect(screen, whiteFlagColorMiddle, whiteFlagMiddle)  # draw button
        pygame.draw.rect(screen, whiteFlagColorleft, whiteFlagleft)  # draw button
    elif (4 in group4) and (addingToGroup4 or playing):
        working = g4Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG4(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        whiteFlagColorRight = color
        whiteFlagColorMiddle = color
        whiteFlagColorleft = color
        pygame.draw.rect(screen, whiteFlagColorRight, whiteFlagRight)  # draw button
        pygame.draw.rect(screen, whiteFlagColorMiddle, whiteFlagMiddle)  # draw button
        pygame.draw.rect(screen, whiteFlagColorleft, whiteFlagleft)  # draw button
    elif (4 in group5) and (addingToGroup5 or playing):
        working = g5Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG5(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        whiteFlagColorRight = color
        whiteFlagColorMiddle = color
        whiteFlagColorleft = color
        pygame.draw.rect(screen, whiteFlagColorRight, whiteFlagRight)  # draw button
        pygame.draw.rect(screen, whiteFlagColorMiddle, whiteFlagMiddle)  # draw button
        pygame.draw.rect(screen, whiteFlagColorleft, whiteFlagleft)  # draw button
    elif (4 in group6) and (addingToGroup6 or playing):
        working = g6Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG6(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        whiteFlagColorRight = color
        whiteFlagColorMiddle = color
        whiteFlagColorleft = color
        pygame.draw.rect(screen, whiteFlagColorRight, whiteFlagRight)  # draw button
        pygame.draw.rect(screen, whiteFlagColorMiddle, whiteFlagMiddle)  # draw button
        pygame.draw.rect(screen, whiteFlagColorleft, whiteFlagleft)  # draw button
    else:
        pygame.draw.rect(screen, darkGrey, whiteFlagRight)  # draw button
        pygame.draw.rect(screen, darkGrey, whiteFlagMiddle)  # draw button
        pygame.draw.rect(screen, darkGrey, whiteFlagleft)  # draw button
    color = (0.0, 0.0, 0.0)
    if (5 in group1) and (addingToGroup1 or playing):
        working = g1Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG1(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        greenFlagColorRight = color
        greenFlagColorMiddle = color
        greenFlagColorleft = color
        pygame.draw.rect(screen, greenFlagColorRight, greenFlagRight)  # draw button
        pygame.draw.rect(screen, greenFlagColorMiddle, greenFlagMiddle)  # draw button
        pygame.draw.rect(screen, greenFlagColorleft, greenFlagleft)  # draw button
    elif (5 in group2) and (addingToGroup2 or playing):
        working = g2Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG2(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        greenFlagColorRight = color
        greenFlagColorMiddle = color
        greenFlagColorleft = color
        pygame.draw.rect(screen, greenFlagColorRight, greenFlagRight)  # draw button
        pygame.draw.rect(screen, greenFlagColorMiddle, greenFlagMiddle)  # draw button
        pygame.draw.rect(screen, greenFlagColorleft, greenFlagleft)  # draw button
    elif (5 in group3) and (addingToGroup3 or playing):
        working = g3Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG3(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        greenFlagColorRight = color
        greenFlagColorMiddle = color
        greenFlagColorleft = color
        pygame.draw.rect(screen, greenFlagColorRight, greenFlagRight)  # draw button
        pygame.draw.rect(screen, greenFlagColorMiddle, greenFlagMiddle)  # draw button
        pygame.draw.rect(screen, greenFlagColorleft, greenFlagleft)  # draw button
    elif (5 in group4) and (addingToGroup4 or playing):
        working = g4Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG4(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        greenFlagColorRight = color
        greenFlagColorMiddle = color
        greenFlagColorleft = color
        pygame.draw.rect(screen, greenFlagColorRight, greenFlagRight)  # draw button
        pygame.draw.rect(screen, greenFlagColorMiddle, greenFlagMiddle)  # draw button
        pygame.draw.rect(screen, greenFlagColorleft, greenFlagleft)  # draw button
    elif (5 in group5) and (addingToGroup5 or playing):
        working = g5Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG5(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        greenFlagColorRight = color
        greenFlagColorMiddle = color
        greenFlagColorleft = color
        pygame.draw.rect(screen, greenFlagColorRight, greenFlagRight)  # draw button
        pygame.draw.rect(screen, greenFlagColorMiddle, greenFlagMiddle)  # draw button
        pygame.draw.rect(screen, greenFlagColorleft, greenFlagleft)  # draw button
    elif (5 in group6) and (addingToGroup6 or playing):
        working = g6Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG6(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        greenFlagColorRight = color
        greenFlagColorMiddle = color
        greenFlagColorleft = color
        pygame.draw.rect(screen, greenFlagColorRight, greenFlagRight)  # draw button
        pygame.draw.rect(screen, greenFlagColorMiddle, greenFlagMiddle)  # draw button
        pygame.draw.rect(screen, greenFlagColorleft, greenFlagleft)  # draw button
    else:
        pygame.draw.rect(screen, darkGrey, greenFlagRight)  # draw button
        pygame.draw.rect(screen, darkGrey, greenFlagMiddle)  # draw button
        pygame.draw.rect(screen, darkGrey, greenFlagleft)  # draw button
    color = (0.0, 0.0, 0.0)
    if (6 in group1) and (addingToGroup1 or playing):
        working = g1Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG1(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        blueFlagColorRight = color
        blueFlagColorMiddle = color
        blueFlagColorleft = color
        pygame.draw.rect(screen, blueFlagColorRight, blueFlagRight)  # draw button
        pygame.draw.rect(screen, blueFlagColorMiddle, blueFlagMiddle)  # draw button
        pygame.draw.rect(screen, blueFlagColorleft, blueFlagleft)  # draw button
    elif (6 in group2) and (addingToGroup2 or playing):
        working = g2Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG2(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        blueFlagColorRight = color
        blueFlagColorMiddle = color
        blueFlagColorleft = color
        pygame.draw.rect(screen, blueFlagColorRight, blueFlagRight)  # draw button
        pygame.draw.rect(screen, blueFlagColorMiddle, blueFlagMiddle)  # draw button
        pygame.draw.rect(screen, blueFlagColorleft, blueFlagleft)  # draw button
    elif (6 in group3) and (addingToGroup3 or playing):
        working = g3Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG3(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        blueFlagColorRight = color
        blueFlagColorMiddle = color
        blueFlagColorleft = color
        pygame.draw.rect(screen, blueFlagColorRight, blueFlagRight)  # draw button
        pygame.draw.rect(screen, blueFlagColorMiddle, blueFlagMiddle)  # draw button
        pygame.draw.rect(screen, blueFlagColorleft, blueFlagleft)  # draw button
    elif (6 in group4) and (addingToGroup4 or playing):
        working = g4Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG4(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        blueFlagColorRight = color
        blueFlagColorMiddle = color
        blueFlagColorleft = color
        pygame.draw.rect(screen, blueFlagColorRight, blueFlagRight)  # draw button
        pygame.draw.rect(screen, blueFlagColorMiddle, blueFlagMiddle)  # draw button
        pygame.draw.rect(screen, blueFlagColorleft, blueFlagleft)  # draw button
    elif (6 in group5) and (addingToGroup5 or playing):
        working = g5Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG5(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        blueFlagColorRight = color
        blueFlagColorMiddle = color
        blueFlagColorleft = color
        pygame.draw.rect(screen, blueFlagColorRight, blueFlagRight)  # draw button
        pygame.draw.rect(screen, blueFlagColorMiddle, blueFlagMiddle)  # draw button
        pygame.draw.rect(screen, blueFlagColorleft, blueFlagleft)  # draw button
    elif (6 in group6) and (addingToGroup6 or playing):
        working = g6Action
        if (working[0]=="blink" or working[0]=="sparkle" or working[0]=="pulse"):
            wait = working[2]
            if (not blinkHelperG6(float(wait))):
                color = (0.0, 0.0, 0.0)
            else:
                color = fadeHelper(working[1], working[3])
        if (working[0]=="on"):
            color = working[1]

        blueFlagColorRight = color
        blueFlagColorMiddle = color
        blueFlagColorleft = color
        pygame.draw.rect(screen, blueFlagColorRight, blueFlagRight)  # draw button
        pygame.draw.rect(screen, blueFlagColorMiddle, blueFlagMiddle)  # draw button
        pygame.draw.rect(screen, blueFlagColorleft, blueFlagleft)  # draw button
    else:
        pygame.draw.rect(screen, darkGrey, blueFlagRight)  # draw button
        pygame.draw.rect(screen, darkGrey, blueFlagMiddle)  # draw button
        pygame.draw.rect(screen, darkGrey, blueFlagleft)  # draw button
    
    #print(str(g1Action) + " " + str(group1) + " " + str(g2Action) + " " + str(group2) + " " + str(g3Action) + " " + str(group3) + " " + str(g4Action) + " " + str(group4) + " " + str(g5Action) + " " + str(group5) + " " + str(g6Action) + " " + str(group6))
    
actingGroup = 0
colorSelected = white

def checkEvent(mouse_pos):
    global place, timer, pausePoint, addingToGroup1, selected, playing, songSequence, actingGroup, colorSelected, g1Action, g1Color, g2Color, g3Color, g4Color, g5Color, g6Color, addingToGroup2, addingToGroup3, addingToGroup4, addingToGroup5, addingToGroup6

    if g1.collidepoint(mouse_pos):
        if (addingToGroup1):
            addingToGroup1 = False
            g1Color = grey
        else:
            addingToGroup1 = True
            g1Color = white
            slider.setValue(g1Action[2])
            sliderIntensity.setValue(g1Action[3])
            colorSelected = g1Action[1]

    if g2.collidepoint(mouse_pos):
        if (addingToGroup2):
            addingToGroup2 = False
            g2Color = grey
        else:
            addingToGroup2 = True
            g2Color = white
            slider.setValue(g2Action[2])
            sliderIntensity.setValue(g1Action[3])
            colorSelected = g2Action[1]

    if g3.collidepoint(mouse_pos):
        if (addingToGroup3):
            addingToGroup3 = False
            g3Color = grey
        else:
            addingToGroup3 = True
            g3Color = white
            slider.setValue(g3Action[2])
            sliderIntensity.setValue(g1Action[3])
            colorSelected = g3Action[1]
            
    if g4.collidepoint(mouse_pos):
        if (addingToGroup4):
            addingToGroup4 = False
            g4Color = grey
        else:
            addingToGroup4 = True
            g4Color = white
            slider.setValue(g4Action[2])
            sliderIntensity.setValue(g1Action[3])
            colorSelected = g4Action[1]
            
    if g5.collidepoint(mouse_pos):
        if (addingToGroup5):
            addingToGroup5 = False
            g5Color = grey
        else:
            addingToGroup5 = True
            g5Color = white
            slider.setValue(g5Action[2])
            sliderIntensity.setValue(g1Action[3])
            colorSelected = g5Action[1]
            
    if g6.collidepoint(mouse_pos):
        if (addingToGroup6):
            addingToGroup6 = False
            g6Color = grey
        else:
            addingToGroup6 = True
            g6Color = white
            slider.setValue(g6Action[2])
            sliderIntensity.setValue(g1Action[3])
            colorSelected = g6Action[1]

    if redFlagRight.collidepoint(mouse_pos):
        selected = 1
        if addingToGroup1:
            if selected in group1:
                group1.remove(selected)
            else:
                group1.append(selected)
        if addingToGroup2:
            if selected in group2:
                group2.remove(selected)
            else:
                group2.append(selected)
        if addingToGroup3:
            if selected in group3:
                group3.remove(selected)
            else:
                group3.append(selected)
        if addingToGroup4:
            if selected in group4:
                group4.remove(selected)
            else:
                group4.append(selected)
        if addingToGroup5:
            if selected in group5:
                group5.remove(selected)
            else:
                group5.append(selected)
        if addingToGroup6:
            if selected in group6:
                group6.remove(selected)
            else:
                group6.append(selected)
        
        
    if orangeFlagRight.collidepoint(mouse_pos):
        selected = 2
        if addingToGroup1:
            if selected in group1:
                group1.remove(selected)
            else:
                group1.append(selected)
        if addingToGroup2:
            if selected in group2:
                group2.remove(selected)
            else:
                group2.append(selected)
        if addingToGroup3:
            if selected in group3:
                group3.remove(selected)
            else:
                group3.append(selected)
        if addingToGroup4:
            if selected in group4:
                group4.remove(selected)
            else:
                group4.append(selected)
        if addingToGroup5:
            if selected in group5:
                group5.remove(selected)
            else:
                group5.append(selected)
        if addingToGroup6:
            if selected in group6:
                group6.remove(selected)
            else:
                group6.append(selected)

    if yellowFlagRight.collidepoint(mouse_pos):
        selected = 3
        if addingToGroup1:
            if selected in group1:
                group1.remove(selected)
            else:
                group1.append(selected)
        if addingToGroup2:
            if selected in group2:
                group2.remove(selected)
            else:
                group2.append(selected)
        if addingToGroup3:
            if selected in group3:
                group3.remove(selected)
            else:
                group3.append(selected)
        if addingToGroup4:
            if selected in group4:
                group4.remove(selected)
            else:
                group4.append(selected)
        if addingToGroup5:
            if selected in group5:
                group5.remove(selected)
            else:
                group5.append(selected)
        if addingToGroup6:
            if selected in group6:
                group6.remove(selected)
            else:
                group6.append(selected)

    if whiteFlagRight.collidepoint(mouse_pos):
        selected = 4
        if addingToGroup1:
            if selected in group1:
                group1.remove(selected)
            else:
                group1.append(selected)
        if addingToGroup2:
            if selected in group2:
                group2.remove(selected)
            else:
                group2.append(selected)
        if addingToGroup3:
            if selected in group3:
                group3.remove(selected)
            else:
                group3.append(selected)
        if addingToGroup4:
            if selected in group4:
                group4.remove(selected)
            else:
                group4.append(selected)
        if addingToGroup5:
            if selected in group5:
                group5.remove(selected)
            else:
                group5.append(selected)
        if addingToGroup6:
            if selected in group6:
                group6.remove(selected)
            else:
                group6.append(selected)

    if greenFlagRight.collidepoint(mouse_pos):
        selected = 5
        if addingToGroup1:
            if selected in group1:
                group1.remove(selected)
            else:
                group1.append(selected)
        if addingToGroup2:
            if selected in group2:
                group2.remove(selected)
            else:
                group2.append(selected)
        if addingToGroup3:
            if selected in group3:
                group3.remove(selected)
            else:
                group3.append(selected)
        if addingToGroup4:
            if selected in group4:
                group4.remove(selected)
            else:
                group4.append(selected)
        if addingToGroup5:
            if selected in group5:
                group5.remove(selected)
            else:
                group5.append(selected)
        if addingToGroup6:
            if selected in group6:
                group6.remove(selected)
            else:
                group6.append(selected)

    if blueFlagRight.collidepoint(mouse_pos):
        selected = 6
        if addingToGroup1:
            if selected in group1:
                group1.remove(selected)
            else:
                group1.append(selected)  
        if addingToGroup2:
            if selected in group2:
                group2.remove(selected)
            else:
                group2.append(selected)
        if addingToGroup3:
            if selected in group3:
                group3.remove(selected)
            else:
                group3.append(selected)
        if addingToGroup4:
            if selected in group4:
                group4.remove(selected)
            else:
                group4.append(selected)
        if addingToGroup5:
            if selected in group5:
                group5.remove(selected)
            else:
                group5.append(selected)
        if addingToGroup6:
            if selected in group6:
                group6.remove(selected)
            else:
                group6.append(selected)  

    if left.collidepoint(mouse_pos):
        if (place>0):
            place-=1
    if right.collidepoint(mouse_pos):
        place+=1

    if play.collidepoint(mouse_pos):
        print("Play")
        playing = True
        pygame.mixer.music.play(0, place)
        timer = time.time()
        print(timer)

    if pause.collidepoint(mouse_pos):
        print("Pause")
        playing = False
        place += int(pygame.mixer.music.get_pos()/1000)
        pygame.mixer.music.stop()
    
        

    if fadeButton.collidepoint(mouse_pos):
        if (addingToGroup1):
            g1Action[0] = "fade"
        if (addingToGroup2):
            g2Action[0] = "fade"
        if (addingToGroup3):
            g3Action[0] = "fade"
        if (addingToGroup4):
            g4Action[0] = "fade"
        if (addingToGroup5):
            g5Action[0] = "fade"
        if (addingToGroup6):
            g6Action[0] = "fade"
    
    if blinkButton.collidepoint(mouse_pos):
        if (addingToGroup1):
            g1Action[0] = "blink"
        if (addingToGroup2):
            g2Action[0] = "blink"
        if (addingToGroup3):
            g3Action[0] = "blink"
        if (addingToGroup4):
            g4Action[0] = "blink"
        if (addingToGroup5):
            g5Action[0] = "blink"
        if (addingToGroup6):
            g6Action[0] = "blink"
    
    if sparkleButton.collidepoint(mouse_pos):
        if (addingToGroup1):
            g1Action[0] = "sparkle"
        if (addingToGroup2):
            g2Action[0] = "sparkle"
        if (addingToGroup3):
            g3Action[0] = "sparkle"
        if (addingToGroup4):
            g4Action[0] = "sparkle"
        if (addingToGroup5):
            g5Action[0] = "sparkle"
        if (addingToGroup6):
            g6Action[0] = "sparkle"
    
    if pulseButton.collidepoint(mouse_pos):
        if (addingToGroup1):
            g1Action[0] = "pulse"
        if (addingToGroup2):
            g2Action[0] = "pulse"
        if (addingToGroup3):
            g3Action[0] = "pulse"
        if (addingToGroup4):
            g4Action[0] = "pulse"
        if (addingToGroup5):
            g5Action[0] = "pulse"
        if (addingToGroup6):
            g6Action[0] = "pulse"
    
    if onButton.collidepoint(mouse_pos):
        if (addingToGroup1):
            g1Action[0] = "on"
        if (addingToGroup2):
            g2Action[0] = "on"
        if (addingToGroup3):
            g3Action[0] = "on"
        if (addingToGroup4):
            g4Action[0] = "on"
        if (addingToGroup5):
            g5Action[0] = "on"
        if (addingToGroup6):
            g6Action[0] = "on"
    
    if offButton.collidepoint(mouse_pos):
        if (addingToGroup1):
            g1Action[0] = "off"
        if (addingToGroup2):
            g2Action[0] = "off"
        if (addingToGroup3):
            g3Action[0] = "off"
        if (addingToGroup4):
            g4Action[0] = "off"
        if (addingToGroup5):
            g5Action[0] = "off"
        if (addingToGroup6):
            g6Action[0] = "off"

    if redColor.collidepoint(mouse_pos):
        colorSelected = red
    if orangeColor.collidepoint(mouse_pos):
        colorSelected = orange
    if yellowColor.collidepoint(mouse_pos):
        colorSelected = yellow
    if blueColor.collidepoint(mouse_pos):
        colorSelected = blue
    if whiteColor.collidepoint(mouse_pos):
        colorSelected = white
    if greenColor.collidepoint(mouse_pos):
        colorSelected = green
