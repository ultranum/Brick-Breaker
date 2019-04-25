'''
title: PyGame Template
author: garrett
date created: 2019-04-08
'''

import pygame
pygame.init() # loads pygame module commands in the program

# Display Variables
TITLE = 'Hello World' # Appears in the window title
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

class blocks:

class ball(blocks):

class player:
    pass

# --- CODE STARTS HERE --- #
running = True
while running:
    for event in pygame.event.get(): # returns all inputs and triggers into an array
        if event.type == pygame.QUIT: # If the red X was clicked.
            running = False

    clock.tick(FPS) # pause the game until the FPS time is reached
    pygame.display.flip() # update the screen with changes.
pygame.quit()