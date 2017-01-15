import pygame, globvar, utilsSet


# Podstawowa klasa reprezentujaca przeciwnika
class BaseStar(pygame.sprite.Sprite):
    # constructor allowing to set positon, size and color of the player
	def __init__(self, pos_x, pos_y):
		# call the parent constructor
		pygame.sprite.Sprite.__init__(self)
		self.image = pygame.transform.scale(pygame.image.load('sprite/stars.png').convert_alpha(), (40,40))

		self.rect = self.image.get_rect()
		self.rect.x = pos_x
		self.rect.y = pos_y

	def rotate(self):
		self.image = pygame.transform.flip(self.image, True, False)