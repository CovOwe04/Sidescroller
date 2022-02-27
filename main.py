import pygame
from pygame.locals import *
from Player import Player
from World import World
from Tile import Tile
import random

pygame.init()
#CREATE WINDOW
width,height = 1600, 1000
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('HumansFall')

#IMPORTS
bg_img = pygame.image.load('Assets/bg_castle.png').convert_alpha()
grass_img = pygame.transform.scale(pygame.image.load('Assets/grassMid.png'), (100,100)).convert_alpha()
lava_img = pygame.transform.scale(pygame.image.load('Assets/lavaMid.png'), (100,100)).convert_alpha()
tile_images_array = [None, grass_img, lava_img]

image_jump = pygame.transform.scale(pygame.image.load('Assets/p1_jump.png'),(100,160)).convert_alpha()
image_dead = pygame.image.load('Assets/p1_hurt.png').convert_alpha()
images_right= []

for num in range(1,7):
    img_right = pygame.image.load(f'Assets/p1_walk{num}.png').convert_alpha()
    img_right = pygame.transform.scale(img_right, (100,160))
    img_left = pygame.transform.flip(img_right, True, False)
    images_right.append(img_right)







#WINDOW DRAW
def redrawWindow(win):
    win.blit(bg_img, (bgX, 0))
    win.blit(bg_img, (bgX2,0))
    world.draw(win)
    player.update(game_over, world.data, win)

#WORLD DATA TO TILE CONVERTER
def convertToTile(data):
    rowCount = 0
    newData  =[
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
]
    for row in data:
        colCount = 0
        for tile in row:
            newData[rowCount][colCount] = Tile(tile, tile_images_array[tile], colCount * blockSize, rowCount * blockSize)
            colCount+=1
        rowCount+=1 

    return newData       

#GAME SETTINGS
clock = pygame.time.Clock()
fps = 60
blockSize = 100

bgX = 0
bgX2 = bg_img.get_width()
game_over = 0

world_data =[
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,0 ,0 ,1 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,1 ,1 ,0],
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,1 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0 ,0],
[1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1 ,1],
]

world = World(convertToTile(world_data))
player = Player(100, 500, images_right,image_jump, image_dead)



 #RUN GAME
run = True

while run:

    bgX -= 5
    bgX2 -= 5

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
    