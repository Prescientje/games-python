import pygame, sys, time, random
from pygame.locals import *

pygame.init()
WIDTH  = 400
HEIGHT = 400
BOXSIZE = 40
BOARDWIDTH = WIDTH//BOXSIZE
BOARDHEIGHT = HEIGHT//BOXSIZE
board = []
BLACK = (  0,  0,  0)
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
ORANGE= (255,128,  0)
BLUE  = (  0,  0,255)
GRAY  = (100,100,100)
PURPLE= (255,  0,255)

def main():
    windowSurface = pygame.display.set_mode((WIDTH,HEIGHT), 0, 32)
    pygame.display.set_caption("Hello world!")

    initializeBoard()
    pygame.display.update()
    
    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
	    elif e.type == MOUSEBUTTONUP:
	        mousex, mousey = event.pos
	        box = getBox(mousex,mousey)
		updateColors(box)
                pygame.display.update()


def initializeBoard():
    pass

def getBox(x,y):
    pass

def updateColors(box):
    pass


if __name__ == '__main__':
	main()
