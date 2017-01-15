import pygame, baseEnemy

class enemy2Animation(object):

	def __init__(self):
		sheet = pygame.image.load('sprite/enemy2.png').convert_alpha()
		self.imageEnemyWalk = []
		self.imageEnemyDeath = []
		self.imageEnemyWalk.append( pygame.transform.scale(sheet.subsurface(11,89,180,140), (80,102)))
		self.imageEnemyWalk.append( pygame.transform.scale(sheet.subsurface(225,65,184,163), (80,102)))
		self.imageEnemyWalk.append( pygame.transform.scale(sheet.subsurface(431,40,173,188), (80,102)))
		self.imageEnemyWalk.append( pygame.transform.scale(sheet.subsurface(641,35,181,193), (80,102)))
		self.imageEnemyWalk.append( pygame.transform.scale(sheet.subsurface(855,30,183,198), (80,102)))
		self.imageEnemyWalk.append( pygame.transform.scale(sheet.subsurface(1056,31,189,199), (80,102)))
	