import pygame, sys, time, random
from pygame.locals import *

pygame.init()
WIDTH  = 400
HEIGHT = 400
BOXSIZE = 40
BOARDWIDTH = WIDTH//BOXSIZE
BOARDHEIGHT = HEIGHT//BOXSIZE
board = []
boardColors = []
WHITE = (255,255,255)
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
ORANGE= (255,128,  0)
BLUE  = (  0,  0,255)
GRAY  = (100,100,100)
PURPLE= (255,  0,255)
colors = [RED,GREEN,ORANGE,BLUE,GRAY,PURPLE]
windowSurface = pygame.display.set_mode((WIDTH,HEIGHT), 0, 32)

class Box(object):

    def __init__(self, color, value, checked=False):
        self.color = color
        self.value = value
        self.checked = checked



def main():
    pygame.display.set_caption("Hello world!")

    initializeBoard()
    drawBoard()
    pygame.display.update()
    
    while True:
        for e in pygame.event.get():
            if e.type == QUIT:
                pygame.quit()
                sys.exit()
	    elif e.type == MOUSEBUTTONUP:
	        mousex, mousey = e.pos
	        boxy, boxx = getBox(mousex,mousey)
		updateColors(boxy,boxx)
                drawBoard()
                pygame.display.update()


def initializeBoard():
    for j in range(BOARDHEIGHT):
        row = []
        rowC = []
        for i in range(BOARDWIDTH):
            randCi = random.randint(0,len(colors)-1)
            row.append(Box(colors[randCi],False))
        board.append(row)

    board[0][0].value = True

def drawBoard():
    windowSurface.fill(WHITE)
    for j in range(BOARDHEIGHT):
        for i in range(BOARDWIDTH):
            rr = (i*BOXSIZE,j*BOXSIZE,BOXSIZE,BOXSIZE)
            pygame.draw.rect(windowSurface,board[j][i].color,rr)


def getBox(x,y):
    boxx = x//BOXSIZE
    boxy = y//BOXSIZE
    return boxy,boxx


def updateColors(boxy, boxx):
    if board[boxy][boxx].color == board[0][0].color:
        return
    newC = board[boxy][boxx].color




if __name__ == '__main__':
	main()
