# use pygame
import pygame, player, envsurface, platformsSets, globvar, baseEnemy, enemiesSets, starsSets, Level, time, levelExit, utilsSet, cameraModule
 
def main():
	# initialize pygame
	pygame.init()

	# create the game screen
	#screen = pygame.display.set_mode([globvar.SCREEN_WIDTH, globvar.SCREEN_HEIGHT])
	screen = pygame.display.set_mode((globvar.SCREEN_WIDTH, globvar.SCREEN_HEIGHT), 0, 32)
	
 	#czcionka do pol tekstowych
	font = pygame.font.SysFont("comicsansms",40)
	# set the window title
	pygame.display.set_caption('Mario')	
	utils = utilsSet.Utils(screen)
    # create the character
	character = player.Player(100, 1300, globvar.PLAYER_SIZE, globvar.PLAYER_FILL)
	
	# tworzymy obiekty dla kolejnych poziomow
	level_1 = Level.Level(2000, 1600, 100, 1300)
	level_1.platformsSet = platformsSets.PlatformSet1(character)
	level_1.starsSet = starsSets.StarsSet1(character)	
	level_1.enemiesSet = enemiesSets.EnemiesSet1(character, level_1)
	level_1.levelExit = levelExit.LevelExit(950,598)
	
	level_2 = Level.Level(3000, 1000, 100, 650)
	level_2.platformsSet = platformsSets.PlatformSet2(character)
	level_2.starsSet = starsSets.StarsSet2(character)	
	level_2.enemiesSet = enemiesSets.EnemiesSet2(character, level_2)
	level_2.levelExit = levelExit.LevelExit(950,598)
	
	levels = [level_1, level_2]
	
	# laczymy bohatera z pierwszym poziomem
	character.level = level_1
	
 	sprites = pygame.sprite.Group()
 	sprites.add(character)
	
	exit_game = False
 
	clock = pygame.time.Clock()
	currentLevelNumber = 1
	#utils.printLevelNumber(currentLevelNumber)
	currentLevel = level_1
	camera = cameraModule.Camera(cameraModule.complex_camera, currentLevel.width, currentLevel.height)
	currentLevel.timeStart = time.time()
	
	# the event loop
	while not exit_game:
	
		#przetwarzamy ruchy przeciwnikow
		for enemy in currentLevel.enemiesSet.enemies:
			enemy.moveEnemy()
	
		# process game events
		for event in pygame.event.get():
            
			if event.type == pygame.QUIT:
				exit_game = True
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
		
		#Aktualizujemy kamere
		camera.update(character)
 
		character.checkCollisionsWithEnemies()

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
					pygame.display.update()
					pygame.time.delay(3000)
					exit_game = True
				else:
					currentLevel = levels[currentLevelNumber]
					currentLevelNumber += 1
					character.level = currentLevel
					character.resetPosition()
					camera = cameraModule.Camera(cameraModule.complex_camera, currentLevel.width, currentLevel.height)
					utils.printLevelNumber(currentLevelNumber)
					currentLevel.timeStart = time.time()
		
        # don't let the player leave the world
		if character.rect.right > currentLevel.width:
			character.rect.right = currentLevel.width
 
		if character.rect.left < 0:
			character.rect.left = 0
		if character.rect.bottom > currentLevel.height:
			character.lifeLost()
			
		#Jesli zostalo 0 zyc, to funkcja informuje o koncu gry			
		if character.lives == 0:
			utils.gameOver(currentLevel, screen, character)
			break
		
		# in case of end-game
		if exit_game == True:
			break
			
		screen.fill(globvar.BACKGROUND_FILL)

		
		for e in currentLevel.platformsSet.platforms:
			screen.blit(e.image, camera.apply(e))
		for e in currentLevel.starsSet.stars:
			screen.blit(e.image, camera.apply(e))
		for e in currentLevel.enemiesSet.enemies:
			screen.blit(e.image, camera.apply(e))
		for e in currentLevel.levelExit.exit:
			screen.blit(e.image, camera.apply(e))

		screen.blit(character.image, camera.apply(character))
		
        # draw the scene
		#currentLevel.draw(screen)
		#sprites.draw(screen)
 
		# display the defined number of FPS
		clock.tick(globvar.TICK)
		
		#inicjalizacja pol tekstowych z zyciami i suma punktow
		livesText=font.render("Lives:"+str(character.lives), 1,(255,255,0))
		screen.blit(livesText, (globvar.SCREEN_WIDTH - 250, 10))
		scoreText=font.render("Score:"+str(character.score), 1,(255,255,0))
		screen.blit(scoreText, (globvar.SCREEN_WIDTH - 250, 70))
		timeText=font.render("Time:"+str(round(time.time() - currentLevel.timeStart, 2)), 1,(255,255,0))
		screen.blit(timeText, (10, 10))
 
		pygame.display.update()
		#pygame.display.flip()
 
	# quit game upon clicking the (X) button
	pygame.quit()
 
if __name__ == "__main__":
    main()
