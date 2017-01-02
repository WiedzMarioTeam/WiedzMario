# use pygame
import pygame, player, globvar, gamePlay  
 
def main():
	# initialize pygame
	pygame.init()
	
	# initialize main game & menu loop logic
	currentGamePlay = gamePlay.GamePlay()
	
	currentGamePlay.initMenu(pygame.time.Clock(), None, 40, globvar.MENU_DEFAULT)
	currentGamePlay.menuLoop()
 
	pygame.quit()
 
if __name__ == "__main__":
    main()

