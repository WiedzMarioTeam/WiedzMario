import pygame, player, envsurface, platformsSets, globvar, baseEnemy, enemiesSets, starsSets, Level, time, levelExit, utilsSet, cameraModule, menuItem, sys

class GamePlay():
	def __init__(self):
		self.menu_loop = True
	
	# menu initialization
	def initMenu(self, clock, font, font_size, font_color, menu_items, start_menu):
		#create the game screen
		self.screen = pygame.display.set_mode((globvar.SCREEN_WIDTH, globvar.SCREEN_HEIGHT), 0, 32)
		self.scr_width = self.screen.get_rect().width
		self.scr_height = self.screen.get_rect().height
		self.font = font
		self.start_menu = start_menu
		self.menu_items = menu_items
		# to be implemented
		self.items_in_game = None
		self.clock = clock
		self.items = []
        
		for index, item in enumerate(self.menu_items):
			menu_item = menuItem.MenuItem(item, font, font_size, font_color, 0, 0)
 
            # height of text block
			block_height = len(self.menu_items) * menu_item.height
			pos_x = (self.scr_width / 2) - (menu_item.width / 2)
			pos_y = (self.scr_height / 2) - (block_height / 2) + ((index*2) + index * menu_item.height)
            
			menu_item.set_position(pos_x, pos_y)
			self.items.append(menu_item)
		
		self.current_item = None

        
    
    # handle option choice
	def setKeySelection(self, key):
		for item in self.items:
			# reset all items
			item.set_bold(False)
			item.set_font_color(globvar.MENU_DEFAULT)
 
		if self.current_item is None:
			self.current_item = 0
		else:	
			if key == pygame.K_UP and self.current_item > 0:
				self.current_item -= 1
			elif key == pygame.K_UP and self.current_item == 0:
				self.current_item = len(self.items) - 1
			elif key == pygame.K_DOWN and self.current_item < len(self.items) - 1:
				self.current_item += 1
			elif key == pygame.K_DOWN and self.current_item == len(self.items) - 1:
				self.current_item = 0
 
		# highlight the selected item
		self.items[self.current_item].set_bold(True)
		self.items[self.current_item].set_font_color(globvar.MENU_ACTIVE)
 
        # check if any menu button was "pressed"
		if key == pygame.K_SPACE or key == pygame.K_RETURN:
			text = self.items[self.current_item].text
			if text == 'Start':
				self.initGame(pygame.font.SysFont("comicsansms", 40), "Mario", player.Player(100, 1300, globvar.PLAYER_SIZE, globvar.PLAYER_FILL), pygame.time.Clock(), 1)
			elif text == 'Settings':
				self.settings()
			elif text == 'Choose level':
				self.chooseLevel()
			elif text == 'Quit':
				sys.exit()
    
    # display the start menu  
	def menuLoop(self):
		while self.menu_loop:
			self.clock.tick(globvar.TICK)
            
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					self.setKeySelection(event.key)

			if self.menu_loop:
				self.screen.fill(globvar.MENU_FILL)
 
				for item in self.items:
					self.screen.blit(item.label, item.position)
 
				pygame.display.flip()
        
        
	# initialization of the actual gameplay
	def initGame(self, font, caption, character, clock, current_level_no):
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
		
		self.currentLevel = self.levels[current_level_no - 1]	
		self.character.level = self.levels[current_level_no - 1]	
		
		self.sprites = pygame.sprite.Group()
		self.sprites.add(self.character)
		
		self.camera = cameraModule.Camera(cameraModule.complex_camera, self.currentLevel.width, self.currentLevel.height)
		self.currentLevel.timeStart = time.time()
		
		self.gameLoop()
		
	
	# gameplay loop
	def gameLoop(self):	
		# the event loop
		while self.menu_loop:
		
			#przetwarzamy ruchy przeciwnikow
			for enemy in self.currentLevel.enemiesSet.enemies:
				enemy.moveEnemy()
		
			# process game events
			for event in pygame.event.get():
				
				if event.type == pygame.QUIT:
					self.menu_loop = False
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
						self.menu_loop = False
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
				self.menu_loop = False
			
			# in case of end-game
			if self.menu_loop == False:
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
				
	
	def chooseLevel(self):
		pass
	
	def settings(self):		
		pass
