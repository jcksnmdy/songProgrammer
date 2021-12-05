import pandas as pd
import pygame
import os
import time
import random
import pathlib
import subprocess
import threading
import ctypes 
import signal
import os
import sys
import logging
import argparse
import datetime
sys.path.append('/Users/s1034274/Desktop/globals/')

from constants import path

numInPlaylist = 10


loadButton = pygame.Rect(50, 50, 99, 59)
playButton = pygame.Rect(200, 50, 99, 59)
mainMenu = pygame.Rect(400, 50, 69, 39)

playlist1 = pygame.Rect(50, 50, 129, 39)
playlist2 = pygame.Rect(190, 50, 129, 39)
playlist3 = pygame.Rect(330, 50, 129, 39)
playlist4 = pygame.Rect(470, 50, 129, 39)
playlist5 = pygame.Rect(50, 100, 129, 39)
playlist6 = pygame.Rect(190, 100, 129, 39)
playlist7 = pygame.Rect(330, 100, 129, 39)
playlist8 = pygame.Rect(470, 100, 129, 39)
playlist9 = pygame.Rect(50, 150, 129, 39)
playlist10 = pygame.Rect(190, 150, 129, 39)
playlist11 = pygame.Rect(330, 150, 129, 39)
playlist12 = pygame.Rect(470, 150, 129, 39)
playlist13 = pygame.Rect(50, 200, 129, 39)
playlist14 = pygame.Rect(190, 200, 129, 39)
playlist15 = pygame.Rect(330, 200, 129, 39)
playlist16 = pygame.Rect(470, 200, 129, 39)
playlist17 = pygame.Rect(50, 250, 129, 39)
playlist18 = pygame.Rect(190, 250, 129, 39)
playlist19 = pygame.Rect(330, 250, 129, 39)
playlist20 = pygame.Rect(470, 250, 129, 39)

pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 28)
playlist1Text = font.render('Sirius', True, [0,0,0])
playlist2Text = font.render('Thunder', True, [0,0,0])
playlist3Text = font.render('Eye', True, [0,0,0])
playlist4Text = font.render('Hit me', True, [0,0,0])
playlist5Text = font.render('Enter S', True, [0,0,0])
playlist6Text = font.render('Beat It', True, [0,0,0])
playlist7Text = font.render('Lil Bit', True, [0,0,0])
playlist8Text = font.render('Beggin', True, [0,0,0])
playlist9Text = font.render('Yeah!', True, [0,0,0])
playlist10Text = font.render('Uptown', True, [0,0,0])
playlist11Text = font.render('AOK', True, [0,0,0])
playlist12Text = font.render('Sing.Lad', True, [0,0,0])
playlist13Text = font.render('Thriller', True, [0,0,0])
playlist14Text = font.render('Edemame', True, [0,0,0])
playlist15Text = font.render('Squid', True, [0,0,0])
playlist16Text = font.render('immabe', True, [0,0,0])
playlist17Text = font.render('DeckT', True, [0,0,0])
playlist18Text = font.render('JinRoc', True, [0,0,0])
playlist19Text = font.render('Mili', True, [0,0,0])
playlist20Text = font.render('12days', True, [0,0,0])


redButton = pygame.Rect(137, 330, 7, 39)
orangeButton = pygame.Rect(417, 280, 7, 39)
whiteButton = pygame.Rect(307, 190, 7, 39)
yellowButton = pygame.Rect(167, 220, 7, 39)
greenButton = pygame.Rect(257, 160, 7, 39)
blueButton = pygame.Rect(437, 100, 7, 39)

loadColor = [255,255,255]
playColor = [255,255,255]

redButtonColor = (0.0, 0.0, 0.0)
orangeButtonColor = (0.0, 0.0, 0.0)
whiteButtonColor = (0.0, 0.0, 0.0)
yellowButtonColor = (0.0, 0.0, 0.0)
greenButtonColor = (0.0, 0.0, 0.0)
blueButtonColor = (0.0, 0.0, 0.0)

def main():
    global songSequence, loadColor, playColor
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    pygame.display.set_caption("Main Menu")
    
    loadText = font.render('Load', True, [0,0,0])
    playText = font.render('Play', True, [0,0,0])
    while True:
        
        screen.fill([0,0,0])
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                if loadButton.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    pickLoad()
                                    
                if playButton.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    pickPlay()
                
                if mainMenu.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    loadColor = [255,255,255]
                    playColor = [255,255,255]

        pygame.draw.rect(screen, loadColor, loadButton)  # draw button
        pygame.draw.rect(screen, playColor, playButton)  # draw button
        screen.blit(loadText, loadButton)
        screen.blit(playText, playButton)

        pygame.display.flip()
        
        clock.tick(60)

def pickLoad():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    while True:
        
        screen.fill([0,0,0])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                main()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                if playlist1.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(1)

                if playlist2.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(2)

                if playlist3.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(3)

                if playlist4.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(4)

                if playlist5.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(5)

                if playlist6.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(6)

                if playlist7.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(7)

                if playlist8.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(8)

                if playlist9.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(9)

                if playlist10.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(10)

                if playlist11.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(11)
                
                if playlist12.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(12)
                

                if playlist13.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(13)

                
                if playlist14.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(14)

                if playlist15.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(15)
                    
                if playlist16.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(16)
                if playlist17.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(17)

                
                if playlist18.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(18)

                if playlist19.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(19)
                    
                if playlist20.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(20)

        pygame.draw.rect(screen, [255,255,255], playlist1)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist2)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist3)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist4)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist5)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist6)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist7)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist8)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist9)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist10)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist11)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist12)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist13)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist14)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist15)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist16)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist17)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist18)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist19)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist20)  # draw button

        screen.blit(playlist1Text, playlist1)
        screen.blit(playlist2Text, playlist2)
        screen.blit(playlist3Text, playlist3)
        screen.blit(playlist4Text, playlist4)
        screen.blit(playlist5Text, playlist5)
        screen.blit(playlist6Text, playlist6)
        screen.blit(playlist7Text, playlist7)
        screen.blit(playlist8Text, playlist8)
        screen.blit(playlist9Text, playlist9)
        screen.blit(playlist10Text, playlist10)
        screen.blit(playlist11Text, playlist11)
        screen.blit(playlist12Text, playlist12)
        screen.blit(playlist13Text, playlist13)
        screen.blit(playlist14Text, playlist14)
        screen.blit(playlist15Text, playlist15)
        screen.blit(playlist16Text, playlist16)
        screen.blit(playlist17Text, playlist17)
        screen.blit(playlist18Text, playlist18)
        screen.blit(playlist19Text, playlist19)
        screen.blit(playlist20Text, playlist20)
        
        pygame.display.flip()
        clock.tick(60)

def pickPlay():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    while True:
        
        screen.fill([0,0,0])
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                main()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                if playlist1.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    play(1)
                if playlist2.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    play(2)
                if playlist3.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    play(3)
                if playlist4.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    play(4)
                if playlist5.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    play(5)
                if playlist6.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    play(6)
                if playlist7.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    play(7)
                if playlist8.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    play(8)
                if playlist9.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    play(9)
                if playlist10.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    play(10)
                if playlist11.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    play(11)
                
                if playlist12.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    play(12)
                

                if playlist13.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    play(13)

                
                if playlist14.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    play(14)
                

                if playlist15.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    play(15)

                if playlist16.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    play(16)
                if playlist17.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(17)

                
                if playlist18.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(18)

                if playlist19.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(19)
                    
                if playlist20.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
                    load(20)

        pygame.draw.rect(screen, [255,255,255], playlist1)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist2)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist3)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist4)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist5)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist6)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist7)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist8)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist9)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist10)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist11)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist12)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist13)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist14)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist15)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist16)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist17)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist18)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist19)  # draw button
        pygame.draw.rect(screen, [255,255,255], playlist20)  # draw button

        screen.blit(playlist1Text, playlist1)
        screen.blit(playlist2Text, playlist2)
        screen.blit(playlist3Text, playlist3)
        screen.blit(playlist4Text, playlist4)
        screen.blit(playlist5Text, playlist5)
        screen.blit(playlist6Text, playlist6)
        screen.blit(playlist7Text, playlist7)
        screen.blit(playlist8Text, playlist8)
        screen.blit(playlist9Text, playlist9)
        screen.blit(playlist10Text, playlist10)
        screen.blit(playlist11Text, playlist11)
        screen.blit(playlist12Text, playlist12)
        screen.blit(playlist13Text, playlist13)
        screen.blit(playlist14Text, playlist14)
        screen.blit(playlist15Text, playlist15)
        screen.blit(playlist16Text, playlist16)
        screen.blit(playlist17Text, playlist17)
        screen.blit(playlist18Text, playlist18)
        screen.blit(playlist19Text, playlist19)
        screen.blit(playlist20Text, playlist20)

        
        pygame.display.flip()
    
        clock.tick(60)

def load(songPlay):
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font('freesansbold.ttf', 28)
    global songSequence, redButtonColor, orangeButtonColor, whiteButtonColor, yellowButtonColor, greenButtonColor, blueButtonColor
    pygame.mixer.init()
    pygame.mixer.music.load("/Users/s1034274/Desktop/songs/song" + str(songPlay) + ".mp3")
    pygame.mixer.music.play(0)
    songSequence = pd.DataFrame({'Time Elapsed':[0],
                    'Red 1':[redButtonColor],
                    'Orange 2':[orangeButtonColor],
                    'White 3':[whiteButtonColor],
                    'Yellow 4':[yellowButtonColor],
                    'Green 5':[greenButtonColor],
                    'Blue 6':[blueButtonColor],})

    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    timer = time.time()
    i = 0
    while (pygame.mixer.music.get_busy() and time.time()-timer<180.0):
        screen.fill([0,0,0])
        i = i + 1
        keys = pygame.key.get_pressed()
        # determine if a letter key was pressed 
        if keys[pygame.K_1]:
            redButtonColor = (255.0, 0.0, 0.0)
        else:
            redButtonColor = (0.0, 0.0, 0.0)

        if keys[pygame.K_2]:
            orangeButtonColor = (255.0, 168, 0.0)
        else:
            orangeButtonColor = (0.0, 0.0, 0.0)

        if keys[pygame.K_3]:
            whiteButtonColor = (255.0, 255.0, 255.0)
        else:
            whiteButtonColor = (0.0, 0.0, 0.0)

        if keys[pygame.K_4]:
            yellowButtonColor = (255.0, 255.0, 0)
        else:
            yellowButtonColor = (0.0, 0.0, 0.0)

        if keys[pygame.K_5]:
            greenButtonColor = (0.0, 255.0, 0.0)
        else:
            greenButtonColor = (0.0, 0.0, 0.0)
        
        if keys[pygame.K_6]:
            blueButtonColor = (0.0, 0.0, 255.0)
        else:
            blueButtonColor = (0.0, 0.0, 0.0)

        if keys[pygame.K_q]:
            redButtonColor = (111.1, 111.1, 111.1)

        if keys[pygame.K_w]:
            orangeButtonColor = (111.1, 111.1, 111.1)

        if keys[pygame.K_e]:
            whiteButtonColor = (111.1, 111.1, 111.1)

        if keys[pygame.K_r]:
            yellowButtonColor = (111.1, 111.1, 111.1)

        if keys[pygame.K_t]:
            greenButtonColor = (111.1, 111.1, 111.1)

        if keys[pygame.K_y]:
            blueButtonColor = (111.1, 111.1, 111.1)

        if keys[pygame.K_9]:
            redButtonColor = (255.0, 0.0, 0.0)
            orangeButtonColor = (255.0, 128.0, 0.0)
            whiteButtonColor = (255.0, 255.0, 255.0)
            yellowButtonColor = (255.0, 255.0, 0.0)
            greenButtonColor = (0.0, 255.0, 0.0)
            blueButtonColor = (0.0, 0, 255.0)

        if keys[pygame.K_a]:
            redButtonColor = (255.0, 0.0, 0.0)
            orangeButtonColor = (255.0, 0.0, 0.0)
            whiteButtonColor = (255.0, 0.0, 0.0)
            yellowButtonColor = (255.0, 0.0, 0.0)
            greenButtonColor = (255.0, 0.0, 0.0)
            blueButtonColor = (255.0, 0.0, 0.0)
        if keys[pygame.K_s]:
            redButtonColor = (255.0, 128.0, 0.0)
            orangeButtonColor = (255.0, 128.0, 0.0)
            whiteButtonColor = (255.0, 128.0, 0.0)
            yellowButtonColor = (255.0, 128.0, 0.0)
            greenButtonColor = (255.0, 128.0, 0.0)
            blueButtonColor = (255.0, 128.0, 0.0)
        if keys[pygame.K_d]:
            redButtonColor = (255.0, 255.0, 255.0)
            orangeButtonColor = (255.0, 255.0, 255.0)
            whiteButtonColor = (255.0, 255.0, 255.0)
            yellowButtonColor = (255.0, 255.0, 255.0)
            greenButtonColor = (255.0, 255.0, 255.0)
            blueButtonColor = (255.0, 255.0, 255.0)
        if keys[pygame.K_f]:
            redButtonColor = (255.0, 255.0, 0.0)
            orangeButtonColor = (255.0, 255.0, 0.0)
            whiteButtonColor = (255.0, 255.0, 0.0)
            yellowButtonColor = (255.0, 255.0, 0.0)
            greenButtonColor = (255.0, 255.0, 0.0)
            blueButtonColor = (255.0, 255.0, 0.0)
        if keys[pygame.K_g]:
            redButtonColor = (0.0, 255.0, 0.0)
            orangeButtonColor = (0.0, 255.0, 0.0)
            whiteButtonColor = (0.0, 255.0, 0.0)
            yellowButtonColor = (0.0, 255.0, 0.0)
            greenButtonColor = (0.0, 255.0, 0.0)
            blueButtonColor = (0.0, 255.0, 0.0)
        if keys[pygame.K_h]:
            redButtonColor = (0.0, 0.0, 255.0)
            orangeButtonColor = (0.0, 0.0, 255.0)
            whiteButtonColor = (0.0, 0.0, 255.0)
            yellowButtonColor = (0.0, 0.0, 255.0)
            greenButtonColor = (0.0, 0.0, 255.0)
            blueButtonColor = (0.0, 0.0, 255.0)

#special
        special1 = (255.0, 128.0, 0.0)
        special2 = (255.0, 0.0, 255.0)
        special3 = (255.0, 255.0, 255.0)
        if keys[pygame.K_z]:
            redButtonColor = special1
            orangeButtonColor = special2
            whiteButtonColor = special3
            yellowButtonColor = special1
            greenButtonColor = special2
            blueButtonColor = special3
        if keys[pygame.K_x]:
            redButtonColor = special3
            orangeButtonColor = special1
            whiteButtonColor = special2
            yellowButtonColor = special3
            greenButtonColor = special1
            blueButtonColor = special2
        if keys[pygame.K_c]:
            redButtonColor = special2
            orangeButtonColor = special3
            whiteButtonColor = special1
            yellowButtonColor = special2
            greenButtonColor = special3
            blueButtonColor = special1
        if keys[pygame.K_v]:
            redButtonColor = (255.0, 255.0, 0.0)
            orangeButtonColor = (255.0, 255.0, 0.0)
            whiteButtonColor = (255.0, 255.0, 0.0)
            yellowButtonColor = (255.0, 255.0, 0.0)
            greenButtonColor = (255.0, 255.0, 0.0)
            blueButtonColor = (255.0, 255.0, 0.0)
        if keys[pygame.K_b]:
            redButtonColor = (0.0, 255.0, 0.0)
            orangeButtonColor = (0.0, 255.0, 0.0)
            whiteButtonColor = (0.0, 255.0, 0.0)
            yellowButtonColor = (0.0, 255.0, 0.0)
            greenButtonColor = (0.0, 255.0, 0.0)
            blueButtonColor = (0.0, 255.0, 0.0)
        if keys[pygame.K_n]:
            redButtonColor = (0.0, 0.0, 255.0)
            orangeButtonColor = (0.0, 0.0, 255.0)
            whiteButtonColor = (0.0, 0.0, 255.0)
            yellowButtonColor = (0.0, 0.0, 255.0)
            greenButtonColor = (0.0, 0.0, 255.0)
            blueButtonColor = (0.0, 0.0, 255.0)

        pygame.draw.rect(screen, redButtonColor, redButton)  # draw button
        pygame.draw.rect(screen, orangeButtonColor, orangeButton)  # draw button
        pygame.draw.rect(screen, whiteButtonColor, whiteButton)  # draw button
        pygame.draw.rect(screen, yellowButtonColor, yellowButton)  # draw button
        pygame.draw.rect(screen, greenButtonColor, greenButton)  # draw button
        pygame.draw.rect(screen, blueButtonColor, blueButton)  # draw button
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                songSequence.to_excel("/Users/s1034274/Desktop/songs/song" + str(songPlay) + ".xlsx")
                pygame.quit()
                main()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                if loadButton.collidepoint(mouse_pos):
                    # prints the location of mouse
                    print('button was pressed at {0}'.format(mouse_pos))
        
        if (i%2==0):
            songSequence = songSequence.append({'Time Elapsed':pygame.mixer.music.get_pos()/1000,
                        'Red 1':redButtonColor,
                        'Orange 2':orangeButtonColor,
                        'White 3':whiteButtonColor,
                        'Yellow 4':yellowButtonColor,
                        'Green 5':greenButtonColor,
                        'Blue 6':blueButtonColor,}, ignore_index=True)
        
        pygame.display.flip()
    
        clock.tick(60)
    pygame.mixer.music.stop()
    songSequence.to_excel("/Users/s1034274/Desktop/songs/song" + str(songPlay) + ".xlsx")
    pygame.quit()
    main()

def toTuple(before):
    print("Before: " + str(before))
    firstNum = float(before[before.find("(")+1:before.find(",")])
    secNum = float(before[before.find(",")+2:before.find(",", 9)])
    thirdNum = float(before[before.find(",", 9)+2:before.find(")")])
    returning = (firstNum, secNum, thirdNum)
    print("Returning:" + str(returning))
    return returning

def play(songNum):
    pygame.init()
    pygame.font.init()
    font = pygame.font.Font('freesansbold.ttf', 28)
    pygame.mixer.init()
    global songSequence
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()

    print("Programmed song playing. " + str(songNum))
    i = 5
    allInfo = pd.read_excel(path + "/flagCode/song" + str(songNum) + ".xlsx")
    time.sleep(5)
    pygame.mixer.music.load("/Users/s1034274/Desktop/songs/song" + str(songNum) + ".mp3")
    pygame.mixer.music.play(0)
    while (i < len(allInfo)):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.music.stop()
                pygame.quit()
                main()

        screen.fill([0,0,0])
        # redButton = pygame.Rect(120, 330, 39, 39)
        # orangeButton = pygame.Rect(400, 280, 39, 39)
        # whiteButton = pygame.Rect(290, 190, 39, 39)
        # yellowButton = pygame.Rect(150, 220, 39, 39)
        # greenButton = pygame.Rect(240, 160, 39, 39)
        # blueButton = pygame.Rect(420, 100, 39, 39)

        pygame.draw.line(screen, toTuple(allInfo.loc[(i),'red Left']), (120, 330), (160, 370), 8)  # draw button
        pygame.draw.rect(screen, toTuple(allInfo.loc[(i),'red Middle']), redButton)  # draw button
        pygame.draw.line(screen, toTuple(allInfo.loc[(i),'red Right']), (160, 330), (120, 370), 8)  # draw button
        
        pygame.draw.line(screen, toTuple(allInfo.loc[(i),'orange Left']), (400, 280), (440, 320), 8)  # draw button
        pygame.draw.rect(screen, toTuple(allInfo.loc[(i),'orange Middle']), orangeButton)  # draw button
        pygame.draw.line(screen, toTuple(allInfo.loc[(i),'orange Right']), (440, 280), (400, 320), 8)  # draw button

        pygame.draw.line(screen, toTuple(allInfo.loc[(i),'white Left']), (290, 190), (330, 230), 8)  # draw button
        pygame.draw.rect(screen, toTuple(allInfo.loc[(i),'white Middle']), whiteButton)  # draw button
        pygame.draw.line(screen, toTuple(allInfo.loc[(i),'white Right']), (330, 190), (290, 230), 8)  # draw button

        pygame.draw.line(screen, toTuple(allInfo.loc[(i),'yellow Left']), (150, 220), (190, 260), 8)  # draw button
        pygame.draw.rect(screen, toTuple(allInfo.loc[(i),'yellow Middle']), yellowButton)  # draw button
        pygame.draw.line(screen, toTuple(allInfo.loc[(i),'yellow Right']), (190, 220), (150, 260), 8)  # draw button

        pygame.draw.line(screen, toTuple(allInfo.loc[(i),'green Left']), (240, 160), (280, 200), 8)  # draw button
        pygame.draw.rect(screen, toTuple(allInfo.loc[(i),'green Middle']), greenButton)  # draw button
        pygame.draw.line(screen, toTuple(allInfo.loc[(i),'green Right']), (280, 160), (240, 200), 8)  # draw button

        pygame.draw.line(screen, toTuple(allInfo.loc[(i),'blue Left']), (420, 100), (460, 140), 8)  # draw button
        pygame.draw.rect(screen, toTuple(allInfo.loc[(i),'blue Middle']), blueButton)  # draw button
        pygame.draw.line(screen, toTuple(allInfo.loc[(i),'blue Right']), (460, 100), (420, 140), 8)  # draw button

        print(i)
        pygame.display.flip()   
        clock.tick(60)
        i+=1
        time.sleep(0.06362)

    pygame.mixer.music.stop()
    pygame.quit()
    main()

main()