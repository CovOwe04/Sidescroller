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
game_over = 0

def redrawWindow(win):
    win.blit(bg_img, (bgX, 0))
    win.blit(bg_img, (bgX2,0))
    world.draw()
    player.update(game_over)

def getBlockImage(blockval):
    if blockval == 1:
        return grass_img
    elif blockval == 2:
        return lava_img

#PLAYER
class Player():
    def __init__(self, x, y):
        self.images_right = []
        self.images_left = []
        self.index = 0
        self.counter = 0
        self.jumped = False

        img_jump = pygame.image.load('Assets/p1_jump.png').convert_alpha()
        self.jump_img = pygame.transform.scale(img_jump, (100,160))

        for num in range(1,7):
            img_right = pygame.image.load(f'Assets/p1_walk{num}.png').convert_alpha()
            img_right = pygame.transform.scale(img_right, (100,160))
            img_left = pygame.transform.flip(img_right, True, False)
            self.images_right.append(img_right)
            self.images_left.append(img_left)
        self.dead_image = pygame.image.load('Assets/p1_hurt.png').convert_alpha()
        self.image = self.images_right[self.index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True
        self.sliding = False
    
    def update(self, game_over):
        dx = 0
        dy = 0
        walk_cooldown = 3
        if game_over == 0:
            #get key presses
            key = pygame.key.get_pressed()
            if key[pygame.K_SPACE] and self.jumped == False and self.in_air == False:
                self.vel_y = -40
                self.jumped = True
            if key[pygame.K_SPACE] == False:
                self.jumped = False
            if key[pygame.K_a]:
                dx -= 10
                self.counter +=1
                self.direction = -1
            if key[pygame.K_d]:
                dx += 10
                self.counter +=1
                self.direction = 1
            if key[pygame.K_a] == False and key[pygame.K_d] == False:
                self.counter = 0
                self.index = 0
                if self.direction == 1:
                    self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_left[self.index]


            #handle animation
            if self.counter > walk_cooldown:
                self.counter = 0
                self.index += 1
            if self.index >= len(self.images_right):
                self.index = 0
            if self.direction == 1:
                self.image = self.images_right[self.index]
                if self.direction == -1:
                    self.image = self.images_right[self.index]
            if self.in_air == True:
                if self.direction == 1:
                    self.image = self.jump_img
                if self.direction == -1:
                    self.image = self.jump_img 

            #add gravity
            self.vel_y += 2
            if self.vel_y > 25:
                self.vel_y = 25
            dy += self.vel_y
            
            #check for collision
            self.in_air = True
            for tile in world.tile_list:
                #check for collision in x direction
                if tile[1].colliderect(self.rect.x + dx, self.rect.y, self.width, self.height):
                    dx =0
                #check for collision in y direction
                if tile[1].colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                    #check if below the ground i.e. jumping
                    if self.vel_y < 0:
                        dy = tile[1].bottom - self.rect.top
                        self.vel_y = 0
                    #check if above the ground i.e. falling
                    elif self.vel_y >= 0:
                        dy = tile[1].top - self.rect.bottom
                        self.vel_y = 0
                        self.in_air = False

            self.rect.x +=dx
            self.rect.y +=dy
        
        elif game_over == -1:
            if self.direction == 1:
                self.image = pygame.transform.scale(self.dead_image, (100, 160))
            if self.direction == -1:
                self.image = pygame.transform.flip (pygame.transform.scale(self.dead_image, (100, 160)), True, False)
        
        win.blit(self.image, self.rect)
        
        return game_over

class Tile():
    def __init__(self, type, x, y):
        self.type = type
        self.image = getBlockImage(type)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y



class World():
    def __init__(self, data):
        self.data = data
    

    def draw(self):
        row_count = 0
        for row in self.data:
            col_count = 0
            for tile in row:
                currentTile = Tile(tile,col_count*blockSize, row_count*blockSize)
                if(currentTile.image != None):
                    win.blit(currentTile.image, currentTile.rect)       
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
player = Player(100, 500)

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
    