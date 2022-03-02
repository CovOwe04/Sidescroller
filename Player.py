import pygame 
from pygame.locals import *
class Player():
    def __init__(self, x, y, images, image_jump, image_dead):
        self.images = images
        self.index = 0
        self.counter = 0
        self.jumped = False
        self.image_jump = image_jump
        self.image_dead = image_dead
        self.rect = self.images[self.index].get_rect()
        self.rect.x = x
        self.rect.y = y
        self.width = self.images[self.index].get_width()
        self.height = self.images[self.index].get_height()
        self.vel_y = 0
        self.jumped = False
        self.direction = 0
        self.in_air = True
        self.sliding = False
    
    def update(self, game_over, data, win):
        dx = 0
        dy = 0
        walk_cooldown = 2
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
                if self.rect.x == 0:
                    self.counter +=1
                    walk_cooldown = 5
                else:
                    self.counter = 0
                self.direction = -1
            if key[pygame.K_d]:
                dx += 5
                self.counter +=1
                self.direction = 1
            if key[pygame.K_a] == False and key[pygame.K_d] == False:
                self.counter +=1
                self.direction = 1
                walk_cooldown = 5
                self.image = self.images[self.index]


            #handle animation
            if self.counter > walk_cooldown:
                self.counter = 0
                self.index += 1
            if self.index >= len(self.images):
                self.index = 1
            if self.direction == 1:
                self.image = self.images[self.index]
            if self.direction == -1:
                self.image = self.images[0]
                if self.rect.x == 0:
                    self.image = self.images[self.index]
            if self.in_air == True:
                if self.direction == 1:
                    self.image = self.image_jump
                if self.direction == -1:
                    self.image = self.image_jump

            #add gravity
            self.vel_y += 2
            if self.vel_y > 25:
                self.vel_y = 25
            dy += self.vel_y
            
            #check for collision
            self.in_air = True
            for row in data:
                for tile in row:
                
                    if (tile.type != 0):
                        #check for collision in x direction
                        if tile.rect.colliderect(self.rect.x + dx +20, self.rect.y, self.width, self.height):
                            dx = -10.5
                        #check for collision in y direction
                        if tile.rect.colliderect(self.rect.x, self.rect.y + dy, self.width, self.height):
                            #check if below the ground i.e. jumping
                            if self.vel_y < 0:
                                dy = tile.rect.bottom - self.rect.top
                                self.vel_y = 0
                            #check if above the ground i.e. falling
                            elif self.vel_y >= 0:
                                dy = tile.rect.top - self.rect.bottom
                                self.vel_y = 0
                                self.in_air = False
            if (self.rect.x + dx < 0):
                dx = 0
            self.rect.x +=dx
            self.rect.y +=dy
        
        elif game_over == -1:
                self.image = self.dead_image
        
        win.blit(self.image, self.rect)
        
        return game_over

