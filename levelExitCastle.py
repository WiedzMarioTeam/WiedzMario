import pygame, entityModule
from pygame import *


class LevelExitCastle(object):
    def __init__(self, pos_x, pos_y):
        self.castle = pygame.sprite.GroupSingle()

        castle = Castle(pos_x, pos_y)
        self.castle.add(castle)

    def update(self):
        self.castle.update()

    def draw(self, screen):
        self.castle.draw(screen)


class Castle(entityModule.Entity):
    def __init__(self, x, y):
        entityModule.Entity.__init__(self)
        castle = pygame.image.load('sprite/zamek.png').convert_alpha()
        self.image = castle
        self.rect = castle.get_rect().move(x, y)