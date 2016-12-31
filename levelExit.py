import globvar, pygame, envsurface, entityModule
from pygame import *

class LevelExit(object):
	def __init__(self, pos_x, pos_y):
		self.exit = pygame.sprite.GroupSingle()
		
		exit = Exit(pos_x, pos_y)
		self.exit.add(exit)
		
		
        
		
	def update(self):
		self.exit.update()
 
	def draw(self, screen): 
		self.exit.draw(screen)
		
class Exit(entityModule.Entity):
	def __init__(self, x, y):
		entityModule.Entity.__init__(self)
		self.image = Surface((globvar.EXIT_WIDTH, globvar.EXIT_HEIGHT))
		self.image.convert()
		self.image.fill(globvar.COLOR_BLUE)
		self.rect = Rect(x, y, globvar.EXIT_WIDTH, globvar.EXIT_HEIGHT)