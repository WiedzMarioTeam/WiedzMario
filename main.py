# use pygame
import pygame, player, envsurface, platformset1, globvar, baseEnemy, LevelEnemySet1
 
def main():
	# initialize pygame
	pygame.init()
 
	# create the game screen
	screen = pygame.display.set_mode([globvar.SCREEN_WIDTH, globvar.SCREEN_HEIGHT])
 
	# set the window title
	pygame.display.set_caption('Mario')

    # create the character
	character = player.Player(globvar.GROUND_LEVEL, globvar.SCREEN_HEIGHT - globvar.GROUND_LEVEL - globvar.PLAYER_SIZE, globvar.PLAYER_SIZE, globvar.PLAYER_FILL)
 
	# establish a link between player and level
	level = platformset1.PlatformSet1(character)
	character.level = level
 	
	enemiesSet = LevelEnemySet1.LevelEnemySet1(character, level)
	level.enemies = enemiesSet.enemies
	
 	sprites = pygame.sprite.Group()
 	sprites.add(character)
	
	for enemy in enemiesSet.enemies:
		sprites.add(enemy)
 
	exit_clicked = False
 
	clock = pygame.time.Clock()
	
	# the event loop
	while not exit_clicked:
	
		#przetwarzamy ruchy przeciwnikow
		for enemy in enemiesSet.enemies:
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
		level.update()
 
		character.checkCollisionsWithEnemies(sprites)
        # don't let the player leave the world
		if character.rect.right > globvar.SCREEN_WIDTH:
			character.rect.right = globvar.SCREEN_WIDTH
 
		if character.rect.left < 0:
			character.rect.left = 0
 
        # draw the scene
		level.draw(screen)
		sprites.draw(screen)
 
		# display the defined number of FPS
		clock.tick(globvar.TICK)
 
        # update the screen
		pygame.display.flip()
 
	# quit game upon clicking the (X) button
	pygame.quit()
 
if __name__ == "__main__":
    main()
