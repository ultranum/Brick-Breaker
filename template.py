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
    def __init__(self, x=0, y=0, width=50, height=10):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.xDir = 1
        self.yDir = -1
        self.color = WHITE
        self.surface = pygame.Surface((0, 0), pygame.SRCALPHA, 32)
        self.surface.fill(self.color)

    def getSurface(self):
        return self.surface

    def getPOS(self):
        return self.pos

    def setPos(self, x, y):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)

    def collision(self):
        pass

    def __repr__(self):
        return ('%s, %s'%(self.x, self.y))
class paddle(blocks):

    def __init__(self, x, y, width, height):
        blocks.__init__(self, x, y, width, height)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)
    def playerMove(self, pressedKey, spd=5):

        if pressedKey[pygame.K_a]:
            self.x -= spd
        if pressedKey[pygame.K_d]:
            self.x += spd
        self.pos = (self.x, self.y)



class ball(blocks):
    def __init__(self, x, y, width, height):
        blocks.__init__(self, x, y, width, height)

    def autoMove(self, spex = 10, spey = 10):
        self.x += self.xDir * spex
        self.y += self.yDir * spey
        self.pos = (self.x, self.y)
        if self.x > WIDTH - self.surface.get_width():
            self.x = WIDTH - self.surface.get_width()
            self.xDir = -1
        if self.x < 0:
            self.x = 0
            self.xDir = 1
        if self.y < 0:
            self.y = 0
            self.yDir = 1
        self.pos = (self.x, self.y)

def getSpriteCollision(sprite1, sprite2):
    if sprite2.getX() <= sprite1.getX() + sprite1.getWidth() <= sprite2.getX() + sprite2.getWidth() + sprite1.getWidth() and sprite2.getY() <= sprite1.getY() + sprite1.getHeight() <= sprite2.getY() + sprite2.getHeight() + sprite1.getHeight():
        return True
    else:
        return False
# --- CODE STARTS HERE --- #
paddle = paddle(90, 90, 100, 20)
ball = ball(20, 20, 20, 20)
ball.setPos(30,30)
paddle.setPos(WIDTH/2,HEIGHT - 30)
blockList = []
blockList.append(blocks(0,0))
blockList[0].setPos(0,0)
for i in range(10):
    x = blockList[i-1].x + blockList[i-1].width + 10
    y = 0
    blockList.append(blocks(x, y))
    blockList[i].setPos(x, y)
    if (blockList[i].x + blockList[i].width) >= WIDTH:
        y = blockList[i].height + blockList[i].y + 2
print(blockList)
running = True
while running:
    for event in pygame.event.get(): # returns all inputs and triggers into an array
        if event.type == pygame.QUIT: # If the red X was clicked.
            running = False
        pressedKeys = pygame.key.get_pressed()
    ball.autoMove()
    paddle.playerMove(pressedKeys, 10)
    screen.fill(GREY)
    screen.blit(paddle.getSurface(), paddle.getPOS())
    screen.blit(ball.getSurface(), ball.getPOS())
    for i in range(len(blockList)):
        screen.blit(blockList[i].getSurface(), blockList[i].getPOS())
    clock.tick(FPS) # pause the game until the FPS time is reached
    pygame.display.flip() # update the screen with changes.
pygame.quit()