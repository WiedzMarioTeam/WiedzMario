import pygame, baseEnemy, enemiesSets

class enemy1Animation(object):

	def __init__(self):
		sheet = pygame.image.load('sprite/enemy1.png').convert_alpha()
		self.imageEnemyWalk = []
		self.imageEnemyDeath = []
		self.imageEnemyWalk.append( pygame.transform.scale(sheet.subsurface(4,195,72,88), (74,86)))
		self.imageEnemyWalk.append( pygame.transform.scale(sheet.subsurface(80,195,72,88), (74,86)))
		self.imageEnemyWalk.append( pygame.transform.scale(sheet.subsurface(157,195,71,88), (74,86)))
		self.imageEnemyWalk.append( pygame.transform.scale(sheet.subsurface(231,195,67,88), (74,86)))
		self.imageEnemyWalk.append( pygame.transform.scale(sheet.subsurface(303,195,71,88), (74,86)))
		self.imageEnemyWalk.append( pygame.transform.scale(sheet.subsurface(378,195,81,88), (74,86)))
		self.imageEnemyWalk.append( pygame.transform.scale(sheet.subsurface(462,195,77,88), (74,86)))
		self.imageEnemyWalk.append( pygame.transform.scale(sheet.subsurface(541,195,76,88), (74,86)))
	