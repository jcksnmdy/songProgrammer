import pandas as pd
import pygame
import os
import time
import random
import subprocess
import signal
import threading
from lightSequencer import program
from constants import monHipHop, tuesRock, wedWayBack, thursThrowback, fridayHits, satDisco, sunCountry, numSongs, numStations, holiday, michealJ, yacht

lights = pygame.Rect(115, 10, 99, 39)

red = (255,0,0)
orange = (255,128,0)
blue = (0,0,255)
yellow = (255,255,0)
green = (0,255,0)
white = (255,255,255)
grey = (128,128,128)
black = (0,0,0)
pygame.init()
pygame.font.init()
font = pygame.font.Font('freesansbold.ttf', 28)
screen = pygame.display.set_mode((750, 500))
clock = pygame.time.Clock()
pygame.display.set_caption("Main Menu")
state = 0
# Load the main Menu
def main():
    lightsText = font.render('Lights', True, black)

    while True:
        
        screen.fill([0,0,0])
        
        for event in pygame.event.get():
            
            # determin if X was clicked, or Ctrl+W or Alt+F4 was used
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos  # gets mouse position
                checkEventMain(mouse_pos)

        if (state == 1):
            lightsOptions(mouse_pos)

        pygame.draw.rect(screen, white, lights)  # draw button
        screen.blit(lightsText, lights)
        

        pygame.display.flip()
        
        clock.tick(60)

loadButton = pygame.Rect(115, 50, 144, 39)
loadButtonText = font.render('Load', True, black)

songName = font.render('Hit Me', True, white)
song = 1

pastSong = pygame.Rect(115, 130, 69, 39)
pastSongText = font.render('Last', True, black)
nextSong = pygame.Rect(190, 130, 69, 39)
nextSongText = font.render('Next', True, black)

def lightsOptions(mouse_pos):
    global songName, song
    if (song == 1):
        songName = font.render('Serious', True, white)
    elif (song == 2):
        songName = font.render('Thunderstruck', True, white)
    elif (song == 3):
        songName = font.render('Eye of the Tiger', True, white)
    elif (song == 4):
        songName = font.render('Hit Me', True, white)
    elif (song == 5):
        songName = font.render('Despacito', True, white)
    elif (song == 6):
        songName = font.render('Beat It', True, white)
    elif (song == 7):
        songName = font.render('Thriller', True, white)
    
    pygame.draw.rect(screen, white, loadButton)  # draw button
    pygame.draw.rect(screen, white, pastSong)  # draw button
    pygame.draw.rect(screen, white, nextSong)  # draw button
    screen.blit(loadButtonText, loadButton)
    screen.blit(songName, (115, 90))
    screen.blit(pastSongText, pastSong)
    screen.blit(nextSongText, nextSong)

def checkEventMain(mouse_pos):
    global state, song              
    if lights.collidepoint(mouse_pos):
        if (state!=1):
            state = 1
        else:
            state = 0

    if loadButton.collidepoint(mouse_pos):
        program(song)

    if nextSong.collidepoint(mouse_pos):
        if (song < numSongs):
            song+=1

    if pastSong.collidepoint(mouse_pos):
        if (song > 1):
            song-=1

main()