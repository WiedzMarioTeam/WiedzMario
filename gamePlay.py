import pygame, player, envsurface, platformsSets, globvar, baseEnemy, enemiesSets, starsSets, Level, time, levelExit, utilsSet, cameraModule 

class GamePlay():
	def __init__(self, font, caption, character, clock, current_level_no):
		#create the game screen
		self.screen = pygame.display.set_mode((globvar.SCREEN_WIDTH, globvar.SCREEN_HEIGHT), 0, 32)
		# set font
		self.font = font
		# set the window title
		pygame.display.set_caption(caption)	
		self.utils = utilsSet.Utils(self.screen)
		# set the player character
		self.character = character
		# set the clock
		self.clock = clock
		# set current level number
		self.currentLevelNumber = current_level_no
		self.levels = None
		self.exit_game = False
		
	
	def initGame(self):
		# tworzymy obiekty dla kolejnych poziomow
		level_1 = Level.Level(2000, 1600, 100, 1300)
		level_1.platformsSet = platformsSets.PlatformSet1(self.character)
		level_1.starsSet = starsSets.StarsSet1(self.character)	
		level_1.enemiesSet = enemiesSets.EnemiesSet1(self.character, level_1)
		level_1.levelExit = levelExit.LevelExit(950,598)
		
		level_2 = Level.Level(3000, 1000, 100, 650)
		level_2.platformsSet = platformsSets.PlatformSet2(self.character)
		level_2.starsSet = starsSets.StarsSet2(self.character)	
		level_2.enemiesSet = enemiesSets.EnemiesSet2(self.character, level_2)
		level_2.levelExit = levelExit.LevelExit(950,598)	
		
		self.levels = [level_1, level_2]
		
		self.currentLevel = level_1	
		self.character.level = level_1
		
		self.sprites = pygame.sprite.Group()
		self.sprites.add(self.character)
		
		self.camera = cameraModule.Camera(cameraModule.complex_camera, self.currentLevel.width, self.currentLevel.height)
		self.currentLevel.timeStart = time.time()
		
	
	def gameLoop(self):	
		# the event loop
		while not self.exit_game:
		
			#przetwarzamy ruchy przeciwnikow
			for enemy in self.currentLevel.enemiesSet.enemies:
				enemy.moveEnemy()
		
			# process game events
			for event in pygame.event.get():
				
				if event.type == pygame.QUIT:
					self.exit_game = True
				# on key press
				if event.type == pygame.KEYDOWN:
					if event.key == pygame.K_LEFT:
						self.character.move_left()
					elif event.key == pygame.K_RIGHT:
						self.character.move_right()
					elif event.key == pygame.K_UP or event.key == pygame.K_SPACE:
						self.character.jump()
				# on key release
				if event.type == pygame.KEYUP:
					if event.key == pygame.K_LEFT and self.character.change_x < 0:
						self.character.stop()
					elif event.key == pygame.K_RIGHT and self.character.change_x > 0:
						self.character.stop()	
	 
			# update the scene
			self.sprites.update()
			self.currentLevel.update()
			
			#Aktualizujemy kamere
			self.camera.update(self.character)
	 
			self.character.checkCollisionsWithEnemies()

			# Sprawdzamy, czy zebrano jakas gwiazdke		
			self.character.checkCollisionsWithStars()
			
			#Sprawdzamy, czy gracz dotarl do konca poziomu
			for ex in self.currentLevel.levelExit.exit:
				if self.character.rect.colliderect(ex.rect):
					if self.currentLevelNumber == len(self.levels):
						self.utils.printTextCenter("YOU WON THE GAME")
						text_width, text_height = self.font.size("Score:"+str(self.character.score))
						scoreText=self.font.render("Score:"+str(self.character.score), 1,(255,255,0))
						self.screen.blit(scoreText, ((globvar.SCREEN_WIDTH - text_width)/2, (globvar.SCREEN_HEIGHT + text_height + 20)/2))	
						pygame.display.update()
						pygame.time.delay(3000)
						self.exit_game = True
					else:
						self.currentLevel = self.levels[self.currentLevelNumber]
						self.currentLevelNumber += 1
						self.character.level = self.currentLevel
						self.character.resetPosition()
						self.camera = cameraModule.Camera(cameraModule.complex_camera, self.currentLevel.width, self.currentLevel.height)
						self.utils.printLevelNumber(self.currentLevelNumber)
						self.currentLevel.timeStart = time.time()
			
			# don't let the player leave the world
			if self.character.rect.right > self.currentLevel.width:
				self.character.rect.right = self.currentLevel.width
	 
			if self.character.rect.left < 0:
				self.character.rect.left = 0
			if self.character.rect.bottom > self.currentLevel.height:
				self.character.lifeLost()
				
			#Jesli zostalo 0 zyc, to funkcja informuje o koncu gry			
			if self.character.lives == 0:
				self.utils.gameOver(self.currentLevel, self.screen, self.character)
				break
			
			# in case of end-game
			if self.exit_game == True:
				break
				
			self.screen.fill(globvar.BACKGROUND_FILL)

			
			for e in self.currentLevel.platformsSet.platforms:
				self.screen.blit(e.image, self.camera.apply(e))
			for e in self.currentLevel.starsSet.stars:
				self.screen.blit(e.image, self.camera.apply(e))
			for e in self.currentLevel.enemiesSet.enemies:
				self.screen.blit(e.image, self.camera.apply(e))
			for e in self.currentLevel.levelExit.exit:
				self.screen.blit(e.image, self.camera.apply(e))

			self.screen.blit(self.character.image, self.camera.apply(self.character))
			
			# draw the scene
			#currentLevel.draw(screen)
			#sprites.draw(screen)
	 
			# display the defined number of FPS
			self.clock.tick(globvar.TICK)
			
			#inicjalizacja pol tekstowych z zyciami i suma punktow
			livesText=self.font.render("Lives:"+str(self.character.lives), 1,(255,255,0))
			self.screen.blit(livesText, (globvar.SCREEN_WIDTH - 250, 10))
			scoreText=self.font.render("Score:"+str(self.character.score), 1,(255,255,0))
			self.screen.blit(scoreText, (globvar.SCREEN_WIDTH - 250, 70))
			timeText=self.font.render("Time:"+str(round(time.time() - self.currentLevel.timeStart, 2)), 1,(255,255,0))
			self.screen.blit(timeText, (10, 10))
	 
			pygame.display.update()
			#pygame.display.flip()
				
			
