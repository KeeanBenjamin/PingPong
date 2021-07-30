import pygame, sys
from pygame.locals import *
import math, random
# Sets the colors that are used later for the triangles
RED = (255, 0, 0)
BLUE = (0,0,255)
DARKRED = (192,0,0)
GREEN = (0, 150, 0)
BLACK = (0, 0, 0)
YELLOW = (255, 215, 0)
WHITE = (255, 255, 255)
ORANGE = (255,165,0)
PURPLE = (128,0,128)
TEAL = (86,237,253)

hSize = 600
vSize = 400

# Initiates the window size for pygame
WINDOW = pygame.display.set_mode((hSize, vSize), 0, 32)
def myDrawing(x,y,dx5,dy5):
    # Change x and y to move but we need to pass them back out
    x += dx5
    y += dy5

    boundingRect = pygame.Rect(x, y, hSize // 25, vSize // 20)
    pygame.draw.rect(WINDOW,WHITE,boundingRect)
    return boundingRect,x,y
# Control Moving
rectSize = 20
myRect = pygame.Rect(hSize//1.08,vSize//2,rectSize,vSize//4) #RED
myRect2 = pygame.Rect(hSize//30,vSize//2,rectSize,vSize//4) #BLUE
dx,dy = 0,0
dx2,dy2 = 0,0
speed = 10

def main():
    # Sets the caption for the window
    pygame.display.set_caption("Our first moving shapes")
    # Initiates PyGame
    pygame.init()
    score1 = -1
    score2 = -1
    x = hSize//2
    y = vSize//3
    dx5 = 4
    dy5 = 2
    # Set up a clock
    timer = pygame.time.Clock()
    pygame.key.set_repeat(100, 50)
    while True:
        timer.tick(60)
        dx, dy, dx2, dy2 = 0, 0, 0, 0
        for event in pygame.event.get():
            keys = pygame.key.get_pressed()
            # if keys[pygame.K_LEFT]:
            #     dx = -speed
            # elif keys[pygame.K_RIGHT]:
            #     dx = speed
            if keys[pygame.K_UP]:
                dy = -speed
            elif keys[pygame.K_DOWN]:
                dy = speed
            if keys[pygame.K_w]:
                dy2 = -speed
            elif keys[pygame.K_s]:
                dy2 = speed
            # if keys[pygame.K_a]:
            #     dx2 = -speed
            # elif keys[pygame.K_d]:
            #     dx2 = speed
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if myRect.left < 0:
                myRect.left, dx = 0, 0
            elif myRect.right > hSize:
                myRect.right, dx = hSize, 0
            if myRect.top < 0:
                myRect.top, dy = 0, 0
            elif myRect.bottom > vSize:
                myRect.bottom, dy = vSize, 0
            if myRect2.left < 0:
                myRect2.left, dx2 = 0, 0
            elif myRect2.right > hSize:
                myRect2.right, dx2 = hSize, 0
            if myRect2.top < 0:
                myRect2.top, dy2 = 0, 0
            elif myRect2.bottom > vSize:
                myRect2.bottom, dy2 = vSize, 0

        myRect.move_ip(dx, dy)  # Move the rectangle
        myRect2.move_ip(dx2, dy2)  # Move the rectangle
        WINDOW.fill(RED)
        # Drawing rectangles
        backOne = pygame.Rect(hSize // 2, vSize//1000, hSize, vSize)
        pygame.draw.rect(WINDOW, BLUE, backOne)
        # Fill the screen with a color
        # Updates the screen
        boundingRect,x,y = myDrawing(x,y,dx5,dy5)
        if boundingRect.top<=0 or boundingRect.bottom>=vSize:
            dy5*=-1
        if boundingRect.left<=0:
            x= hSize//2
            y= vSize//2
            score1+=1
        if boundingRect.right>=hSize:
            x = hSize // 2
            y = vSize // 2
            score2+=1

        if myRect.colliderect(boundingRect):
            dx5*=-1
            dy5*=1
        elif myRect2.colliderect(boundingRect):
            dx5*=-1
            dy5*=1
        else:
            pygame.draw.rect(WINDOW, RED, myRect)  # Draw the rectangle
            pygame.draw.rect(WINDOW, BLUE, myRect2)  # Draw the rectangle

        # Text
        myfont = pygame.font.SysFont('Comic Sans MS', 30)
        textsurface = myfont.render(str(score1), False, (0, 0, 0))
        textsurface2 = myfont.render(str(score2), False, (0, 0, 0))
        WINDOW.blit(textsurface, (hSize//3.35, 0))
        WINDOW.blit(textsurface2, (hSize // 1.5, 0))

        # Rules and Instructions
        if score1 == -1:
            dx5, dy5 = 0, 0
            WINDOW.fill(BLUE)
            textsurface6 = myfont.render("Game: Classic Pong", False, BLACK)
            WINDOW.blit(textsurface6, (hSize // 3.5, vSize // 12))
            textsurface3 = myfont.render("RULES: Use your paddle to hit the ball to", False, TEAL)
            WINDOW.blit(textsurface3, (hSize // 50, vSize // 4))
            textsurface5 = myfont.render("the other players side of the screen.", False, TEAL)
            WINDOW.blit(textsurface5, (hSize // 50, vSize // 3))
            textsurface7 = myfont.render("Player 1: Use w and s to move up and down.", False, BLACK)
            WINDOW.blit(textsurface7, (hSize // 50, vSize // 2.2))
            textsurface8 = myfont.render("Player 2: Use arrows to move up and down.", False, BLACK)
            WINDOW.blit(textsurface8, (hSize // 50, vSize // 1.8))
            textsurface8 = myfont.render("FIRST PLAYER TO 10 POINTS WINS!!!", False, TEAL)
            WINDOW.blit(textsurface8, (hSize // 50, vSize // 1.4))
            textsurface4 = myfont.render("Press Backspace to play!!", False, RED)
            WINDOW.blit(textsurface4, (hSize // 5, vSize // 1.2))
            keys = pygame.key.get_pressed()
            if keys[pygame.K_BACKSPACE]:
                  score1, score2 = 0, 0
                  dx5, dy5 = 4, 2

        # Wins and loses
        if score1 == 10:
            dx5,dy5 =0,0
            WINDOW.fill(BLUE)
            textsurface3 = myfont.render("Player Two Wins", False, RED)
            WINDOW.blit(textsurface3, (hSize//3, vSize//4))
            textsurface4 = myfont.render("Press Backspace to play again", False, RED)
            WINDOW.blit(textsurface4, (hSize // 5, vSize // 2))
            if keys[pygame.K_BACKSPACE]:
                score1,score2=0,0
                dx5,dy5=4,2
        if score2 == 10:
            dx5,dy5=0,0
            WINDOW.fill(RED)
            textsurface3 = myfont.render("Player One Wins", False, BLUE)
            WINDOW.blit(textsurface3, (hSize//3, vSize//4))
            textsurface4 = myfont.render("Press Backspace to play again", False, BLUE)
            WINDOW.blit(textsurface4, (hSize // 5, vSize // 2))
            if keys[pygame.K_BACKSPACE]:
                score1,score2=0,0
                dx5,dy5=4,2
        pygame.display.update()

main()