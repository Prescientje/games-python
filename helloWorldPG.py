import pygame, sys, time
from pygame.locals import *

pygame.init()
WIDTH  = 500
HEIGHT = 400

windowSurface = pygame.display.set_mode((WIDTH,HEIGHT), 0, 32)
pygame.display.set_caption("Hello world!")

BLACK = (  0,  0,  0)
WHITE = (255,255,255)
RED   = (255,  0,  0)
GREEN = (  0,255,  0)
BLUE  = (  0,  0,255)

UP = 0
DOWN = 1

basicFont = pygame.font.SysFont(None, 48)

text = basicFont.render('Hello world!', True, WHITE, BLUE)
textRect = text.get_rect()
textRect.centerx = windowSurface.get_rect().centerx
textRect.centery = windowSurface.get_rect().centery

b = {'rect':pygame.Rect(100,80,50,50),'color':RED,'dir':UP}
SPEED = 1

pygame.draw.polygon(windowSurface, GREEN, ((146,0), (291,106), (236,277), (56,277), (0,106)))

windowSurface.blit(text,textRect)
pygame.display.update()

while True:
    for e in pygame.event.get():
        if e.type == QUIT:
            pygame.quit()
            sys.exit()

    windowSurface.fill(WHITE)
    if b['dir'] == UP:
        b['rect'].top -= SPEED
    elif b['dir'] == DOWN:
        b['rect'].top += SPEED

    if b['rect'].top < 0:
        b['dir'] = DOWN
    elif b['rect'].bottom > HEIGHT:
        b['dir'] = UP

    pygame.draw.rect(windowSurface, b['color'], b['rect'])
    windowSurface.blit(text,textRect)

    pygame.display.update()
    time.sleep(0.02)
