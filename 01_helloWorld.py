'''
title: Hello World
author: garrett
date created: 2019-04-08
'''

import pygame, random
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
YELLOW = (255,255,0)
# Create the Window

screen = pygame.display.set_mode(SCREENDIM) # Creates the main surface where all other assets are placed on top
pygame.display.set_caption(TITLE) # This update the window title with TITLE
screen.fill(GREY) # Fills the entire surface with the color. Think of fill as erase

clock = pygame.time.Clock() # Starts a clock to measure time

## Add text
class text:
    def __init__(self, text = 'hello world', pos = (0,0)):
        self.text = text
        self.color = (255,255,255)
        self.size = 28
        self.x = pos[0]
        self.y = pos[1]
        self.xDir = 1
        self.yDir = 1
        self.pos = (self.x, self.y)
        self.fontFam = 'Arial'
        self.font = pygame.font.SysFont(self.fontFam, self.size)
        self.surface = self.font.render(self.text, 1, self.color)

    def getText(self):
        return self.surface

    def getPOS(self):
        return self.pos

    def setColor(self, color):
        self.color = color
        self.surface = self.font.render(self.text, 1, self.color)

    def setSize(self, size):
        self.size = size
        self.font = pygame.font.SysFont(self.fontFam, self.size)
        self. surface = self.font.render(self.text, 1, self.color)

    def setPOS(self, x, y):
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.surface = self.font.render(self.text, 1, self.color)

    def setFont(self, font):
        self.fontFam = str(font)
        self.font = pygame.font.SysFont(self.fontFam, self.size)
        self.surface = self.font.render(self.text, 1, self.color)

    def setText(self, text):
        self.text = str(text)
        self.surface = self.font.render(self.text, 1, self.color)

    def moveText(self, spdx=1, spdy=1):

        self.x += (self.xDir*spdx)
        self.y += (self.yDir * spdy)
        self.pos = (self.x, self.y)
        if self.x > WIDTH - self.surface.get_width():
            self.xDir = -1
        elif self.x < 0:
            self.xDir = 1
        if self.y > HEIGHT - self.surface.get_height():
            self.yDir = -1
        elif self.y < 0:
            self.yDir = 1

    def playerMove(self, pressedKey, spd = 5):
        if pressedKey[pygame.K_w]:
            self.y -= spd
        if pressedKey[pygame.K_s]:
            self.y += spd
        if pressedKey[pygame.K_a]:
            self.x -= spd
        if pressedKey[pygame.K_d]:
            self.x += spd

        if self.x > WIDTH - self.surface.get_width():
            self.x = WIDTH - self.surface.get_width()
        if self.x < 0:
            self.x = 0
        if self.y > HEIGHT - self.surface.get_height():
            self.y = HEIGHT - self.surface.get_height()
        if self.y < 0:
            self.y = 0
        self.pos = (self.x, self.y)
# --- CODE STARTS HERE --- #
x = 0
myText = text('Hello', (100,100))
myText.setColor(YELLOW)
myText.setSize(100)
myText.setPOS(WIDTH/2 - myText.getText().get_width()/2, HEIGHT/2 - myText.getText().get_height()/2)
myText.setFont('Comic Sans')

newText = text('world')
newText1 = text('a',(30,20))
newText2 = text('b',(50,90))
newText3 = text('c', (200, 100))
running = True
while running:
    for event in pygame.event.get(): # returns all inputs and triggers into an array
        if event.type == pygame.QUIT: # If the red X was clicked.
            running = False
        pressedKeys = pygame.key.get_pressed()
        print(pressedKeys[pygame.K_a])
    myText.playerMove(pressedKeys)
    newText.moveText(12,20)
    newText.playerMove(pressedKeys)

    # newText.setText(x)
    # x += 1
    # newText1.moveText(2,9)
    # newText2.moveText(9,10)
    # newText3.moveText(30,10)
    screen.fill(GREY)
    screen.blit(myText.getText(), myText.getPOS())
    screen.blit(newText.getText(), newText.getPOS())
    screen.blit(newText1.getText(), newText1.getPOS())
    screen.blit(newText2.getText(), newText2.getPOS())
    screen.blit(newText3.getText(), newText3.getPOS())
    clock.tick(FPS) # pause the game until the FPS time is reached
    pygame.display.flip() # update the screen with changes.

pygame.quit()