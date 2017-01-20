import pygame, entityModule
from pygame import *


class NextLevelEntrance(object):
    def __init__(self, pos_x, pos_y):
        self.doors = pygame.sprite.GroupSingle()

        doors = Doors(pos_x, pos_y)
        self.doors.add(doors)

    def update(self):
        self.doors.update()

    def draw(self, screen):
        self.doors.draw(screen)


class Doors(entityModule.Entity):
    def __init__(self, x, y):
        entityModule.Entity.__init__(self)
        doors = pygame.image.load('Images/drzwi.png').convert_alpha()
        self.image = doors
        self.rect = doors.get_rect().move(x, y)