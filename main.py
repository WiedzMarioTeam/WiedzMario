# use pygame
import pygame, player, globvar, gamePlay  
 
def main():
	# initialize pygame
	pygame.init()
	
	# initialize main game & menu loop logic
	currentGamePlay = gamePlay.GamePlay()
 
	pygame.quit()
 
if __name__ == "__main__":
    main()

