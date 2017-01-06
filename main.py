# use pygame
import pygame, player, globvar, gamePlay  
 
def main():

	pygame.mixer.pre_init(44100, -16, 1, 512)
	# initialize pygame
	pygame.init()
	
	# initialize main game & menu loop logic
	currentGamePlay = gamePlay.GamePlay()
 
	pygame.quit()
 
if __name__ == "__main__":
    main()

