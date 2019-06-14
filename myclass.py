'''
title: 
author: garrett
date created: 2019-04-15
'''

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

class myClass:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.surface = pygame.Surface((0,0), pygame.SRCALPHA, 32)
        self.red = 0
        self.blue = 0
        self.green = 0
        self.color = (self.red, self.green, self.blue)
        self.xDir = 1
        self.yDir = 1

    def getSurface(self):
        return self.surface

    def getPOS(self):
        return self.pos

    def setColor(self, color = (0,0,0)):
        self.red = color[0]
        self.green = color[1]
        self.blue = color[2]
        self.color = (self.red, self.green, self.blue)

    def autoMove(self, spex = 10, spey = 10):

        self.x += self.xDir * spex
        self.y += self.yDir * spey
        self.pos = (self.x, self.y)
        # if self.x > WIDTH - self.surface.get_width():
        #     self.x = WIDTH - self.surface.get_width()
        #     self.xDir = -1
        # if self.x < 0:
        #     self.x = 0
        #     self.xDir = 1
        # if self.y > HEIGHT - self.surface.get_height():
        #     self.y = HEIGHT - self.surface.get_height()
        #     self.yDir = -1
        # if self.y < 0:
        #     self.y = 0
        #     self.yDir = 1
        # self.pos = (self.x, self.y)

    def playerMove(self):
        pass

    def getX(self):
        return self.x
    def getY(self):
        return self.y

    def getWidth(self):
        return self.width

    def getHeight(self):
        return self.height

    def setPos(self, x, y):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)
class text(myClass):
    def __init__(self, content, font = 'Arial', fontSize = 24):
        myClass.__init__(self)
        self.fontSize = fontSize
        self.fontFam = font
        self.font = pygame.font.SysFont(font, fontSize)
        self.content = content
        self.surface = self.font.render(self.content, 1, self.color)

    def setColor(self, color = (0,0,0)):
        myClass.setColor(self, color)
        self.surface = self.font.render(self.content, 1, self.color)

    def getText(self):
        return myClass.getSurface(self)

class box(myClass):
    def __init__(self, width, height, x = 0, y = 0):
        myClass.__init__(self, x, y)
        self.width = width
        self.height = height
        self.dim = (self.width, self.height)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)

    def setColor(self, color):
        myClass.setColor(self, color)
        self.surface.fill(self.color)

    def getBox(self):
        return myClass.getSurface(self)

    def playerMove(self, pressedKey, spd=5):
        if pressedKey[pygame.K_w]:
            self.y -= spd
        if pressedKey[pygame.K_s]:
            self.y += spd
        if pressedKey[pygame.K_a]:
            self.x -= spd
        if pressedKey[pygame.K_d]:
            self.x += spd
        #
        # if self.x > WIDTH - self.surface.get_width():
        #     self.x = WIDTH - self.surface.get_width()
        # if self.x < 0:
        #     self.x = 0
        # if self.y > HEIGHT - self.surface.get_height():
        #     self.y = HEIGHT - self.surface.get_height()
        # if self.y < 0:
        #     self.y = 0
        # self.pos = (self.x, self.y)
class mySprite(myClass):
    def __init__(self, fileName):
        myClass.__init__(self)
        self.surface = pygame.image.load(fileName).convert_alpha()

    #TODO: Incorporate Automatic move and keyboard into this file
    #TODO: Incorporate specific methods into text and box
    #TODO: Incorporate 1 specific method into text or box that overrides a parent method. Can still include parent method ie set color
def getSpriteCollision(sprite1, sprite2):
    if sprite2.getX() <= sprite1.getX() + sprite1.getWidth() <= sprite2.getX() + sprite2.getWidth() + sprite1.getWidth() and sprite2.getY() <= sprite1.getY() + sprite1.getHeight() <= sprite2.getY() + sprite2.getHeight() + sprite1.getHeight():
        return True
    else:
        return False