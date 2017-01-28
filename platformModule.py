import pygame, entityModule
from pygame import *

class Platform(entityModule.Entity):
    def __init__(self, x, y, width, height, fill_color):
        entityModule.Entity.__init__(self)
        self.image = Surface((width, height))
        self.image.convert()
        self.image.blit(pygame.image.load('Images/podloga.png'),(0,0))
       # self.image.fill(fill_color)
        self.rect = Rect(x, y, width, height)