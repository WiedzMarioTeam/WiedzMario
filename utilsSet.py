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
		pygame.display.update()
		pygame.time.delay(1500)
		
	def gameOver(self, currentLevel, screen, character):
		font = pygame.font.SysFont("comicsansms",40)
		self.printTextCenter("GAME OVER")
		text_width, text_height = font.size("Score:"+str(character.score))
		scoreText=font.render("Score:"+str(character.score), 1,(255,255,0))
		screen.blit(scoreText, ((globvar.SCREEN_WIDTH - text_width)/2, (globvar.SCREEN_HEIGHT + text_height + 20)/2))		
		pygame.display.update()
		pygame.time.delay(3000)
		#pygame.quit()

def rot_center(image, rect, angle):
    """rotate an image while keeping its center"""
    rot_image = pygame.transform.rotate(image, angle)
    rot_rect = rot_image.get_rect(center=rect.center)
    return rot_image,rot_rect