'''
title: Brick Breaker
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
        self.height = height
        self.width = width
        self.x = x
        self.y = y
        self.color = WHITE
        self.dim = (self.width, self.height)
        self.pos = (self.x, self.y)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)
        self.xDir = 1
        self.yDir = 1

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

    def setDim(self, width, height):
        self.height = height
        self.width = width
        self.dim = (self.width, self.height)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def __repr__(self): # For debugging
        return ('x:%s y:%s'%(self.x, self.y))

class paddle(blocks):

    def __init__(self, x, y, width, height):
        blocks.__init__(self, x, y, width, height)

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
paddle = paddle(WIDTH/2 - 75, HEIGHT - 100, 1500, 10)
ball = ball(WIDTH/2 - 75,HEIGHT - 200, 20, 20)
blockList = []
y = 5
for i in range(5):
    x = 65
    for j in range(15):
        blockList.append(blocks(x, y, 40, 15))
        x += blockList[i].width + 5
    y += blockList[i].height + 10
print(blockList)
running = True
while running:
    for event in pygame.event.get(): # returns all inputs and triggers into an array
        if event.type == pygame.QUIT: # If the red X was clicked.
            running = False
        pressedKeys = pygame.key.get_pressed()
    ball.autoMove(20)
    paddle.playerMove(pressedKeys, 15)
    if getSpriteCollision(paddle, ball) == True: # Checks if paddle and ball collided
        if ball.xDir == 1 or ball.xDir == -1 and ball.yDir == 1: # Bounces ball back
            ball.yDir = -1
    for i in range(len(blockList)):
        if getSpriteCollision(ball, blockList[i]):
            blockList.pop(i)
            if ball.yDir == -1:
                ball.yDir = 1
            elif ball.yDir == 1:
                ball.yDir = -1


    screen.fill(GREY)
    screen.blit(paddle.getSurface(), paddle.getPOS())
    screen.blit(ball.getSurface(), ball.getPOS())
    for i in range(len(blockList)):
        screen.blit(blockList[i].getSurface(), blockList[i].getPOS())
    clock.tick(FPS) # pause the game until the FPS time is reached
    pygame.display.flip() # update the screen with changes.
pygame.quit()