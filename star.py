'''
title: PyGame Template
author: garrett
date created: 2019-04-08
'''
from myclass import box
import pygame, random
pygame.init() # loads pygame module commands in the program

# Display Variables
TITLE = 'star' # Appears in the window title
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
screen.fill(BLACK) # Fills the entire surface with the color. Think of fill as erase

clock = pygame.time.Clock() # Starts a clock to measure time
stars = []
for i in range(200):
    width = random.randrange(1,4)
    stars.append(box(width, width, random.randrange(0, WIDTH), random.randrange(0, HEIGHT)))
    stars[i].setColor(WHITE)

# --- CODE STARTS HERE --- #
running = True
while running:
    for event in pygame.event.get(): # returns all inputs and triggers into an array
        if event.type == pygame.QUIT: # If the red X was clicked.
            running = False
        pressedKeys = pygame.key.get_pressed()
    screen.fill(BLACK)
    for i in range(len(stars)):
        if stars[i].width == 1:
            stars[i].autoMove(-2,0)
        elif stars[i].width == 2:
            stars[i].autoMove(-4,0)
        elif stars[i].width == 3:
            stars[i].autoMove(-6,0)
        else:
            stars[i].autoMove(-3,0)
        stars[i].playerMove(pressedKeys)
        if stars[i].x < 0:
            stars[i].x = WIDTH
            stars[i].y = random.randrange(0, HEIGHT)
        elif stars[i].x > WIDTH:
            stars[i].x = 0
            stars[i].y = random.randrange(0, HEIGHT)
        if stars[i].y > HEIGHT:
            stars[i].y = 0
            stars[i].x = random.randrange(0, WIDTH)
        elif stars[i].y < 0:
            stars[i].y = HEIGHT
            stars[i].x = random.randrange(0, WIDTH)

        screen.blit(stars[i].getSurface(), stars[i].getPOS())


    clock.tick(FPS) # pause the game until the FPS time is reached
    pygame.display.flip() # update the screen with changes.
pygame.quit()