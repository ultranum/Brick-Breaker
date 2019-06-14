'''
title: Inheritance example
author: garrett
date created: 2019-04-16
'''

from myclass import text, box, getSpriteCollision, mySprite
import pygame
pygame.init() # loads pygame module commands in the program

# Display Variables
TITLE = 'Inheritance' # Appears in the window title
FPS = 30 # fps
WIDTH = 800
HEIGHT = 600
SCREENDIM = (WIDTH, HEIGHT)

# Color Variables
WHITE = (255,255,255)
BLACK = (0,0,0)
GREY = (50,50,50)

# Create the Window

screen = pygame.display.set_mode(SCREENDIM) # Creates the main surface where all other assets are placed on top
pygame.display.set_caption(TITLE) # This update the window title with TITLE
screen.fill(GREY) # Fills the entire surface with the color. Think of fill as erase

clock = pygame.time.Clock() # Starts a clock to measure time

# --- CODE STARTS HERE --- #
myText = text('dawiop')
myBox = box(100,200,300,300)
myBox.setColor((255,0,0))
myBox2 = box(100,200)
myBox2.setColor((255,0,255))
myText.setColor((0,255,0))
buny = mySprite('Media/bunny.png')

running = True
while running:
    for event in pygame.event.get(): # returns all inputs and triggers into an array
        if event.type == pygame.QUIT: # If the red X was clicked.
            running = False
        pressedKeys = pygame.key.get_pressed()
    myBox2.autoMove()
    myBox.playerMove(pressedKeys)
    if getSpriteCollision(myBox, myBox2) == True:
        pass
    screen.fill(GREY)

    screen.blit(myText.getSurface(), myText.getPOS())
    screen.blit(myBox.getSurface(), myBox.getPOS())
    screen.blit(myBox2.getSurface(), myBox2.getPOS())
    screen.blit(buny.getSurface(), buny.getPOS())
    clock.tick(FPS) # pause the game until the FPS time is reached
    pygame.display.flip() # update the screen with changes.
pygame.quit()