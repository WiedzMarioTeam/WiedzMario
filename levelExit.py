import globvar, pygame, envsurface

class LevelExit(object):
	def __init__(self, pos_x, pos_y):
		self.exit = pygame.sprite.GroupSingle()
		
		surface = envsurface.EnvSurface(pos_x, pos_y, globvar.EXIT_WIDTH, globvar.EXIT_HEIGHT, globvar.COLOR_BLUE)
		self.exit.add(surface)
		
	def update(self):
		self.exit.update()
 
	def draw(self, screen): 
		self.exit.draw(screen)
		
