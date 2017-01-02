# use pygame
import pygame, player, globvar, gamePlay 
 
def main():
	# initialize pygame
	pygame.init()
	
	# initialize main game & menu loop logic
	currentGamePlay = gamePlay.GamePlay(pygame.font.SysFont("comicsansms", 40), "Mario", player.Player(100, 1300, globvar.PLAYER_SIZE, globvar.PLAYER_FILL), pygame.time.Clock(), 1)
	
	currentGamePlay.initGame()
	currentGamePlay.gameLoop()
 
	pygame.quit()
 
if __name__ == "__main__":
    main()
