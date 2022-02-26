import pygame
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60

width,height = 1600, 1000

win = pygame.display.set_mode((width, height))
pygame.display.set_caption('HumansFall')

bg_img = pygame.image.load('Assets/bg_castle.png').convert_alpha()
grass_img = pygame.transform.scale(pygame.image.load('Assets/grassMid.png'), (100,100)).convert_alpha()

bgX = 0
bgX2 = bg_img.get_width()

def redrawWindow(win):
    win.blit(bg_img, (bgX, 0))
    win.blit(bg_img, (bgX2,0))
    win.blit(grass_img, (800,500))


 
run = True

while run:

    bgX -= 1
    bgX2 -= 1

    if bgX < bg_img.get_width() * -1:
        bgX = bg_img.get_width()
    if bgX2 < bg_img.get_width() * -1:
        bgX2 = bg_img.get_width()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            run = False

    redrawWindow(win)
    pygame.display.update()
    clock.tick(fps)
    