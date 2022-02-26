import pygame
from pygame.locals import *
import random

pygame.init()

clock = pygame.time.Clock()
fps = 60
blockSize = 100

width,height = 1600, 1000

win = pygame.display.set_mode((width, height))
pygame.display.set_caption('HumansFall')

bg_img = pygame.image.load('Assets/bg_castle.png').convert_alpha()
grass_img = pygame.transform.scale(pygame.image.load('Assets/grassMid.png'), (100,100)).convert_alpha()
lava_img = pygame.transform.scale(pygame.image.load('Assets/lavaMid.png'), (100,100)).convert_alpha()

bgX = 0
bgX2 = bg_img.get_width()

def redrawWindow(win):
    win.blit(bg_img, (bgX, 0))
    win.blit(bg_img, (bgX2,0))
    world.draw()



class World():
    def __init__(self, data):
        self.data = data
    
    def getBlockImage(self, blockval):
        if blockval == 1:
            return grass_img
        elif blockval == 2:
            return lava_img

    def draw(self):
        row_count = 0
        for row in self.data:
            col_count = 0
            for tile in row:
                currentImg = self.getBlockImage(tile)
                if(currentImg != None):
                    win.blit(currentImg, (col_count*blockSize, row_count*blockSize))       
                col_count += 1

            row_count +=1

world_data =[
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,0 ,0 ,0 ,1 ,1 ,0 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,1 ,1 ,0 ,0 ,0 ,1 ,1 ,0 ,0 ,0 ,1 ,1 ,0 ,0],
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[1 ,1 ,2 ,2 ,1 ,1 ,1 ,2 ,2 ,1 ,1 ,1 ,2 ,2 ,1 ,1],
]
 


world = World(world_data)

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
    