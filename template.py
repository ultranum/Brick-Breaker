'''
title: Brick Breaker
author: garrett
date created: 2019-04-08
'''

import pygame
pygame.init() # loads pygame module commands in the program

# Display Variables
TITLE = 'Hello World' # Appears in the window title
FPS = 100 # fps
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

class text:
    def __init__(self, text = 'text', pos = (0,0)):
        self.text = text
        self.color = (255,255,255)
        self.size = 28
        self.x = pos[0]
        self.y = pos[1]
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

    def getSurface(self): # Encapsulation
        return self.surface

    def getPOS(self): # Encapsulation
        return self.pos

    def setPos(self, x, y): # Encapsulation
        self.x = x
        self.y = y
        self.pos = (self.x, self.y)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)

    def setDim(self, width, height): # Encapsulation
        self.height = height
        self.width = width
        self.dim = (self.width, self.height)
        self.surface = pygame.Surface(self.dim, pygame.SRCALPHA, 32)
        self.surface.fill(self.color)

    def getX(self): # Encapsulation
        return self.x

    def getY(self): # Encapsulation
        return self.y

    def getWidth(self): # Encapsulation
        return self.width

    def getHeight(self): # Encapsulation
        return self.height

    def __repr__(self): # For debugging
        return ('x:%s y:%s'%(self.x, self.y))

class paddle(blocks): # Inheritance
    def __init__(self, x, y, width, height):
        blocks.__init__(self, x, y, width, height)

    def playerMove(self, pressedKey, spd=5):
        if pressedKey[pygame.K_a]:
            self.x -= spd
        if pressedKey[pygame.K_d]:
            self.x += spd
        self.pos = (self.x, self.y)

class ball(blocks): # Inheritance
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

def collision(rect1, rect2):
    right1 = rect1.getX() + rect1.getWidth()
    bot1 = rect1.getY() + rect1.getHeight()
    left1 = rect1.getX()
    top1 = rect1.getY()
    right2 = rect2.getX() + rect2.getWidth()
    bot2 = rect2.getY() + rect2.getHeight()
    left2 = rect2.getX()
    top2 = rect2.getY()
    if right1 > left2 and left1 < right2 and bot1 > top2 and top1 < bot2:
        return True


def setup():
    if level == 1:
        paddle.setPos(WIDTH / 2 - 75, HEIGHT - 100)
        ball.setPos(WIDTH / 2 - 75, HEIGHT - 200)
        ball.xDir = 1
        ball.yDir = 1

        y = 30
        for i in range(4):
            x = 35
            for j in range(16):
                blockList.append(blocks(x, y, 40, 20)) # Aggregation
                x += blockList[i].width + 5
            y += blockList[i].height + 20
    elif level == 2:
        paddle.setPos(WIDTH / 2 - 75, HEIGHT - 100)
        ball.setPos(WIDTH / 2 - 75, HEIGHT - 200)
        ball.xDir = 1
        ball.yDir = 1
        x = 0
        y = 5
        for j in range(8):
            blockList2.append(blocks(x, y, 40, 15)) # Aggregation
            x += blockList2[j].width + 10
            y += blockList2[j].height + 20

        x = WIDTH - 60
        y = 5
        for k in range(8):
            blockList2.append(blocks(x, y, 40, 15)) # Aggregation
            x -= blockList2[k].width + 10
            y += blockList2[k].height + 20


# --- CODE STARTS HERE --- #
score = 0
menu = 1
level = 1
setuplevel2 = 0
gameovercheck = 0
paddle = paddle(WIDTH/2 - 75, HEIGHT - 100, 1500, 10)
ball = ball(WIDTH/2 - 75,HEIGHT - 200, 10, 10)
title = text('Brick Breaker', (WIDTH/2, 50))
starttext = text('Press space', (WIDTH/2, HEIGHT - 90))
gameover = text('GAME OVER', (WIDTH/2,50))
retrytext = text('Press enter', (WIDTH/2, HEIGHT - 90))
scoretext = text('SCORE: %s'%(score), (0,0))
title.setPOS(999,999)
blockList = [] # Aggregation
blockList2 = [] # Aggregation
setup()
print(level)
print(blockList)
running = True
while running:
    for event in pygame.event.get(): # returns all inputs and triggers into an array
        if event.type == pygame.QUIT: # If the red X was clicked.
            running = False
        pressedKeys = pygame.key.get_pressed()
    if menu == 1:
        title.setPOS(WIDTH / 2 - 2*title.size, HEIGHT/2 - 30)
        starttext.setPOS(WIDTH / 2 - 2*starttext.size - 70 / 2, HEIGHT - 90)
        ball.autoMove(0, 0)
        paddle.playerMove(pressedKeys, 0)

        if pressedKeys[pygame.K_SPACE]:
            menu = 0
    else:

        if collision(paddle, ball): # Checks if paddle and ball collided
            ball.yDir = -1

        if level == 1:
            ball.autoMove(5)
            paddle.playerMove(pressedKeys, 15)
            if len(blockList) == 0 or score == 640:
                    print('this is a test')
                    level = 2
                    pass

            for i in range(len(blockList)):
                if collision(ball, blockList[i]):
                    blockList.pop(i)
                    ball.yDir = -ball.yDir
                    score += 10
                    print(score)
                    scoretext.getText()
                    scoretext = text('SCORE: %s' % (score), (0, 0))
                    print(len(blockList))
                    break


        elif level == 2:
            if setuplevel2 == 0:
                setup()
                setuplevel2 = 1
            ball.autoMove(5)
            paddle.playerMove(pressedKeys, 15)
            if len(blockList2) == 0:
                    print('diowauiod897398w98789w3987w98799f8wefwe')
                    gameovercheck = 1
                    pass

            for i in range(len(blockList2)):
                if collision(ball, blockList2[i]):
                    blockList2.pop(i)
                    ball.yDir = -ball.yDir
                    score += 10
                    scoretext.getText()
                    scoretext = text('SCORE: %s' % (score), (0, 0))
                    print(score)
                    break

        if ball.y > HEIGHT:
            gameovercheck = 1
            gameover.setPOS(WIDTH / 2 - 2 * gameover.size, HEIGHT / 2 - 30)
            retrytext.setPOS(WIDTH / 2 - 2 * retrytext.size - 70 / 2, HEIGHT - 90)
            ball.autoMove(0,0)
            paddle.playerMove(pressedKeys, 0)
            if pressedKeys[pygame.K_RETURN]:
                score = 0
                menu = 1
                level = 1
                setuplevel2 = 0
                gameovercheck = 0
                blockList = []
                blockList2 = []
                setup()




    screen.fill(GREY)
    screen.blit(paddle.getSurface(), paddle.getPOS())
    screen.blit(ball.getSurface(), ball.getPOS())
    screen.blit(scoretext.getText(), scoretext.getPOS())
    if menu == 1:
        screen.blit(title.getText(), title.getPOS())
        screen.blit(starttext.getText(), starttext.getPOS())

    if level == 1:
        for i in range(len(blockList)):
            screen.blit(blockList[i].getSurface(), blockList[i].getPOS())
    elif level == 2:
        for i in range(len(blockList2)):
            screen.blit(blockList2[i].getSurface(), blockList2[i].getPOS())
    if gameovercheck == 1:
        screen.blit(gameover.getText(), gameover.getPOS())
        screen.blit(retrytext.getText(), retrytext.getPOS())
    clock.tick(FPS) # pause the game until the FPS time is reached
    pygame.display.flip() # update the screen with changes.
pygame.quit()
