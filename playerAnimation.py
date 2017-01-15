import pygame


class playerAnimation(object):
	def __init__(self):
		sheet = pygame.image.load('sprite/mario-graphics.png').convert_alpha()
		self.imageRun = []
		self.imageJump = []
		
		for x in range(3):
			self.imageJump.append( pygame.transform.scale(sheet.subsurface(100*x,296,100,120), (68,90)))
		self.imageRun.append(pygame.transform.scale (sheet.subsurface(497,30,90,132), (68,90)))
		self.imageRun.append( pygame.transform.scale (sheet.subsurface(11,30,93,132), (68,90)))
		self.imageRun.append( pygame.transform.scale (sheet.subsurface(114,30,80,132), (68,90)))
		self.imageRun.append( pygame.transform.scale (sheet.subsurface(207,30,80,132), (68,90)))	


