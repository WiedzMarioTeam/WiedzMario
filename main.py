# use pygame
import pygame, player, envsurface, platformsSets, globvar, baseEnemy, enemiesSets, starsSets, Level, time, levelExit, utilsSet
 
def main():
	# initialize pygame
	pygame.init()

	# create the game screen
	screen = pygame.display.set_mode([globvar.SCREEN_WIDTH, globvar.SCREEN_HEIGHT])
 
 	#czcionka do pol tekstowych
	font = pygame.font.SysFont("comicsansms",40)
	# set the window title
	pygame.display.set_caption('Mario')	
	utils = utilsSet.Utils(screen)
    # create the character
	character = player.Player(globvar.GROUND_LEVEL, globvar.SCREEN_HEIGHT - globvar.GROUND_LEVEL - globvar.PLAYER_SIZE, globvar.PLAYER_SIZE, globvar.PLAYER_FILL)
	
	# tworzymy obiekty dla kolejnych poziomow
	level_1 = Level.Level()
	level_1.platformsSet = platformsSets.PlatformSet1(character)
	level_1.starsSet = starsSets.StarsSet1(character)	
	level_1.enemiesSet = enemiesSets.EnemiesSet1(character, level_1)
	level_1.levelExit = levelExit.LevelExit(950,598)
	
	level_2 = Level.Level()
	level_2.platformsSet = platformsSets.PlatformSet2(character)
	level_2.starsSet = starsSets.StarsSet2(character)	
	level_2.enemiesSet = enemiesSets.EnemiesSet2(character, level_2)
	level_2.levelExit = levelExit.LevelExit(950,598)
	
	levels = [level_1, level_2]
	
	# laczymy bohatera z pierwszym poziomem
	character.level = level_1
	
 	sprites = pygame.sprite.Group()
 	sprites.add(character)
	
	exit_clicked = False
 
	clock = pygame.time.Clock()
	currentLevelNumber = 1
	utils.printLevelNumber(currentLevelNumber)
	currentLevel = level_1
	currentLevel.timeStart = time.time()
	
	# the event loop
	while not exit_clicked:
	
		#przetwarzamy ruchy przeciwnikow
		for enemy in currentLevel.enemiesSet.enemies:
			enemy.moveEnemy()
	
		# process game events
		for event in pygame.event.get():
            
			if event.type == pygame.QUIT:
				exit_clicked = True
			# on key press
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					character.move_left()
				elif event.key == pygame.K_RIGHT:
					character.move_right()
				elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
					character.jump()
			# on key release
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT and character.change_x < 0:
					character.stop()
				elif event.key == pygame.K_RIGHT and character.change_x > 0:
					character.stop()
					
			
 
		# update the scene
		sprites.update()
		currentLevel.update()
 
		#Jesli zostalo 0 zyc, to funkcja informuje o koncu gry		
		isGammeOver = character.checkCollisionsWithEnemies()
		if isGammeOver:
			currentLevel.draw(screen)
			sprites.draw(screen)
			utils.printTextCenter("GAME OVER")
			text_width, text_height = font.size("Score:"+str(character.score))
			scoreText=font.render("Score:"+str(character.score), 1,(255,255,0))
			screen.blit(scoreText, ((globvar.SCREEN_WIDTH - text_width)/2, (globvar.SCREEN_HEIGHT + text_height + 20)/2))		
			pygame.display.flip()
			pygame.time.delay(3000)
			pygame.quit()

		# Sprawdzamy, czy zebrano jakas gwiazdke		
		character.checkCollisionsWithStars()
		
		#Sprawdzamy, czy gracz dotarl do konca poziomu
		for ex in currentLevel.levelExit.exit:
			if character.rect.colliderect(ex.rect):
				if currentLevelNumber == len(levels):
					utils.printTextCenter("YOU WON THE GAME")
					text_width, text_height = font.size("Score:"+str(character.score))
					scoreText=font.render("Score:"+str(character.score), 1,(255,255,0))
					screen.blit(scoreText, ((globvar.SCREEN_WIDTH - text_width)/2, (globvar.SCREEN_HEIGHT + text_height + 20)/2))	
					pygame.display.flip()
					pygame.time.delay(3000)
					pygame.quit()
				else:
					currentLevel = levels[currentLevelNumber]
					currentLevelNumber += 1
					character.level = currentLevel
					character.resetPosition()
					utils.printLevelNumber(currentLevelNumber)
					currentLevel.timeStart = time.time()
		
        # don't let the player leave the world
		if character.rect.right > globvar.SCREEN_WIDTH:
			character.rect.right = globvar.SCREEN_WIDTH
 
		if character.rect.left < 0:
			character.rect.left = 0
 
        # draw the scene
		currentLevel.draw(screen)
		sprites.draw(screen)
 
		# display the defined number of FPS
		clock.tick(globvar.TICK)
		
		#inicjalizacja pol tekstowych z zyciami i suma punktow
		livesText=font.render("Lives:"+str(character.lives), 1,(255,255,0))
		screen.blit(livesText, (globvar.SCREEN_WIDTH - 250, 10))
		scoreText=font.render("Score:"+str(character.score), 1,(255,255,0))
		screen.blit(scoreText, (globvar.SCREEN_WIDTH - 250, 70))
		timeText=font.render("Time:"+str(round(time.time() - currentLevel.timeStart, 2)), 1,(255,255,0))
		screen.blit(timeText, (10, 10))
 
        # update the screen
		pygame.display.flip()
 
	# quit game upon clicking the (X) button
	pygame.quit()
 
if __name__ == "__main__":
    main()