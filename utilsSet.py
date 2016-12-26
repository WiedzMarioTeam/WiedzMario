import pygame, globvar

class Utils(object):
	def __init__(self, screen):
	
		#czcionka do pol tekstowych
		self.font = pygame.font.SysFont("comicsansms",40)
		self.screen = screen

	def printTextCenter(self, textToPrint):
		
		text= self.font.render(textToPrint, 1,(255,255,0))
		text_width, text_height = self.font.size(textToPrint)
		self.screen.blit(text, ((globvar.SCREEN_WIDTH - text_width)/2, (globvar.SCREEN_HEIGHT - text_height)/2))
		
	def printLevelNumber(self, number):
		self.screen.fill(globvar.COLOR_BLACK)
		self.printTextCenter("LEVEL " + str(number))
		pygame.display.flip()
		pygame.time.delay(1500)