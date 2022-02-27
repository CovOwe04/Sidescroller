import pygame
from pygame.locals import *


class Tile():
    def __init__(self, type, image, x, y):
        self.type = type
        self.image = image
        self.x = x
        self.y = y
        self.rect = None
        if self.type != 0:
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y

    def convertTile(self, newTile):
        self.type = newTile.type
        self.image = newTile.image
        if newTile.rect != None:
            self.rect = newTile.rect 
            self.rect.x -= 1
            self.rect.y = newTile.rect.y



