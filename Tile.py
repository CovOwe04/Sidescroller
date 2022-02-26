import pygame
from pygame.locals import *


class Tile():
    def __init__(self, type, image, x, y):
        self.type = type
        self.image = image
        if(self.image != None):
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y


