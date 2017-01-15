import pygame, globvar


# Podstawowa klasa reprezentujaca przeciwnika
class BaseStar(pygame.sprite.Sprite):
    # constructor allowing to set positon, size and color of the player
    def __init__(self, pos_x, pos_y, sizeWidth, sizeHeight, pointsForCollect, level):
        # call the parent constructor
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load('sprite/stars.png').convert_alpha()

        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
