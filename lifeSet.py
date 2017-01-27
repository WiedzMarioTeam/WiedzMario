import pygame, globvar, envsurface, baseLife

########################### LEVEL 2 ###################################
class LifeSet2(object):

    def __init__(self, player):
		self.lifeBottles = pygame.sprite.Group()
		self.player = player

        # position, width, height and color of the platform
		lifeBottles = [baseLife.BaseLife(2535, 330)]

		for life in lifeBottles:
			self.lifeBottles.add(life)

        # update the level
    def update(self):
        self.lifeBottles.update()

    def draw(self, screen):
        # draw the sprites
        self.lifeBottles.draw(screen)
