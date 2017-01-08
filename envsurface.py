import pygame

# class representing fixed position objects
class EnvSurface(pygame.sprite.Sprite):
	# constructor allowing to set positon, size and color of environment structures
	def __init__(self, pos_x, pos_y, width, height, fill_color):
		# call the parent constructor
		pygame.sprite.Sprite.__init__(self)
			
		# create a surface of a given size
		self.image = pygame.Surface([width, height])
		# fill it with given color
		self.image.fill(fill_color)
			
		# place the surface in desired position (defined by top left vertex)
		self.rect = self.image.get_rect()
		self.rect.x = pos_x
		self.rect.y = pos_y
