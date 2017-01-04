import pygame, player, envsurface, platformsSets, globvar, baseEnemy, enemiesSets, starsSets, Level, time, levelExit, utilsSet, cameraModule, menuItem, volMenuItem, gameMusic, sys

class GamePlay():
	def __init__(self):
		self.max_levels = 2
		self.player_positions = {'1': (100, 1300), '2': (100, 650)}
		# object handling class music
		self.game_music = gameMusic.GameMusic(2, {'jump': 'sfx/jump.wav'})
		self.pos_toggle = None
		self.pos_volume = None
		# control keys
		self.jump = pygame.K_SPACE
		self.left = pygame.K_LEFT
		self.right = pygame.K_RIGHT
		self.change_keys = False
	
	# menu initialization
	def initMenu(self, clock, font, font_size, font_color, menu_items, start_menu, menu_id, menu_label = None):
		#create the game screen
		self.menu_loop = True
		self.screen = pygame.display.set_mode((globvar.SCREEN_WIDTH, globvar.SCREEN_HEIGHT), 0, 32)
		self.scr_width = self.screen.get_rect().width
		self.scr_height = self.screen.get_rect().height
		self.font = font
		self.start_menu = start_menu
		self.menu_items = menu_items
		self.menu_id = menu_id
		self.clock = clock
		self.items = []
		self.menu_label = menu_label
        
		for index, item in enumerate(self.menu_items):
			# toggle sound logic
			if item == 'Toggle sound':
				item = 'Toggle sound' + ' ' + ('(Off)' if self.isSound() else '(On)')
				self.pos_toggle = index	
			menu_item = menuItem.MenuItem(item, font, font_size, font_color, 0, 0)
			
			# sound volume logic
			if item == 'Sound volume':
				self.pos_volume = index
				if not self.isSound():
					menu_item.set_active(False)
					menu_item.set_font_color(globvar.MENU_INACTIVE)
 
            # height of text block
			block_height = len(self.menu_items) * menu_item.height
			pos_x = (self.scr_width / 2) - (menu_item.width / 2)
			pos_y = (self.scr_height / 2) - (block_height / 2) + ((index * 2) + index * menu_item.height)
            
			menu_item.set_position(pos_x, pos_y)
			self.items.append(menu_item)
		
		self.current_item = None

	
	# volume adjustment menu initialization
	def initVolMenu(self, clock, start_menu, menu_id, menu_label):
		#create the game screen
		self.menu_loop = True
		self.screen = pygame.display.set_mode((globvar.SCREEN_WIDTH, globvar.SCREEN_HEIGHT), 0, 32)
		self.scr_width = self.screen.get_rect().width
		self.scr_height = self.screen.get_rect().height
		self.start_menu = start_menu
		self.menu_id = menu_id
		self.clock = clock
		self.items = []
		self.menu_label = menu_label
        
		initial_x = (self.scr_width - (globvar.MENU_VOL_NO * globvar.MENU_VOL_WIDTH) - ((globvar.MENU_VOL_NO - 1) *globvar.MENU_SPACE_BETWEEN)) / 2
		initial_y = self.scr_height - self.scr_height / 4
		
		for i in range(0, globvar.MENU_VOL_NO):
			width = globvar.MENU_VOL_WIDTH
			height = (i + 1) * globvar.MENU_VOL_HEIGHT

			menu_item = volMenuItem.VolMenuItem(width, height, (globvar.MENU_DEFAULT if i <= (self.game_music.sound_level) else globvar.MENU_INACTIVE), i, 0, 0)
 
			pos_x = initial_x + (i * globvar.MENU_VOL_WIDTH + i * globvar.MENU_SPACE_BETWEEN)
			pos_y = initial_y - (i * globvar.MENU_VOL_HEIGHT)
			menu_item.set_position(pos_x, pos_y)
			self.items.append(menu_item)
		
		self.current_item = None

			
    # handle option choice
	def setKeySelection(self, key):
		for item in self.items:
			item.set_bold(False)
			# reset all active items
			if item.is_active():
				item.set_font_color(globvar.MENU_DEFAULT)
			else:
				item.set_font_color(globvar.MENU_INACTIVE)
		if self.current_item is None:
			self.current_item = 0
			self.items[self.current_item].set_font_color(globvar.MENU_ACTIVE)
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
		if self.change_keys:
			self.items[self.current_item].set_font_color(globvar.MENU_CHANGE)
		elif self.items[self.current_item].is_active():
			self.items[self.current_item].set_font_color(globvar.MENU_ACTIVE)
		else:
			self.items[self.current_item].set_font_color(globvar.MENU_INACTIVE)
		
		# check if control change is to be performed
		if self.change_keys and key == pygame.K_ESCAPE:
			text = self.items[self.current_item].text
			self.resetText(text)
			self.change_keys = False
			key = None
			self.setKeySelection(key)
		elif self.change_keys and key != pygame.K_RETURN:
			text = self.items[self.current_item].text
			self.changeKey(text, key)
			self.change_keys = False
			key = None
			self.setKeySelection(key) 
 
        # check if any menu button was "pressed"
		if key == pygame.K_RETURN and not self.change_keys:
			text = self.items[self.current_item].text
			if text == 'Start':
				self.initGame(pygame.font.SysFont("comicsansms", 40), "Mario", player.Player(self.player_positions['1'], globvar.PLAYER_SIZE, globvar.PLAYER_FILL), pygame.time.Clock(), 1)
			elif text == 'Settings':
				self.settings()
			elif text == 'Choose level':
				self.chooseLevel()
			elif text == 'Quit':
				sys.exit()
			elif text.startswith('Toggle sound'):
				self.toggleSound()
				# a little trick to refresh menu positions in real time
				key = None
				self.setKeySelection(key)
			elif text == 'Controls':
				self.controls()
			elif text == 'Sound volume' and self.items[self.current_item].is_active():
				self.volume()
			elif text == 'Sound volume' and not self.items[self.current_item].is_active():
				return	
			elif text.startswith('Left') or text.startswith('Right') or text.startswith('Jump'):
				self.change_keys = True
				self.updateText(text)
				self.setKeySelection(key)
			else:
				self.initGame(pygame.font.SysFont("comicsansms", 40), "Mario", player.Player(self.player_positions[text], globvar.PLAYER_SIZE, globvar.PLAYER_FILL), pygame.time.Clock(), int(text))
		
		# escape key allows the user to go level up in menu
		if self.menu_id in (2, 3) and key == pygame.K_ESCAPE:
			self.menu_loop = False
			self.initMenu(pygame.time.Clock(), None, 40, globvar.MENU_DEFAULT, ['Start', 'Choose level', 'Settings', 'Quit'], True, 1)
			self.menuLoop()
		elif self.menu_id == 4 and key == pygame.K_ESCAPE:
			self.menu_loop = False
			self.settings()
			
	
	    # handle option choice
	def setKeyVolSelection(self, key):
		if self.current_item is None:
			if key == pygame.K_LEFT and self.game_music.sound_level == 0:
				self.current_item = 0
			elif key == pygame.K_LEFT and self.game_music.sound_level > 0:
				self.current_item = self.game_music.sound_level - 1
				self.game_music.sound_level -= 1
			elif key == pygame.K_RIGHT and self.game_music.sound_level < globvar.MENU_VOL_NO-1:
				self.current_item = self.game_music.sound_level + 1
				self.game_music.sound_level += 1
			elif key == pygame.K_RIGHT and self.game_music.sound_level == globvar.MENU_VOL_NO-1:
				self.current_item = globvar.MENU_VOL_NO -1
		else:
			if key == pygame.K_ESCAPE:
				self.menu_loop = False
				self.settings()
			if key == pygame.K_LEFT and self.current_item == 0:
				self.current_item = 0
			elif key == pygame.K_LEFT and self.current_item > 0:
				self.current_item -= 1
				self.game_music.sound_level -= 1
			elif key == pygame.K_RIGHT and self.current_item < globvar.MENU_VOL_NO-1:
				self.current_item += 1
				self.game_music.sound_level += 1
			elif key == pygame.K_RIGHT and self.current_item == globvar.MENU_VOL_NO-1:
				self.current_item = globvar.MENU_VOL_NO -1
				
		for item in self.items:
			# set color based on current volume
			if item.value <= self.game_music.sound_level:
				item.set_color(globvar.MENU_DEFAULT)
			else:
				item.set_color(globvar.MENU_INACTIVE)
    
    # display the start menu  
	def menuLoop(self):
		# a little trick to highlight the first position when menu is entered
		self.setKeySelection(None)
		while self.menu_loop:
			self.clock.tick(globvar.TICK)
            
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
						self.setKeySelection(event.key)

			if self.menu_loop:
				self.screen.fill(globvar.MENU_FILL)
				
				if self.menu_label is not None:
					self.screen.blit(self.menu_label.label, self.menu_label.position)
 
				for item in self.items:
					self.screen.blit(item.label, item.position)
 
				pygame.display.flip()
    
    
    # display the volume selection menu  
	def volMenuLoop(self):
		while self.menu_loop:
			self.clock.tick(globvar.TICK)
            
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
					self.setKeyVolSelection(event.key)

			if self.menu_loop:
				self.screen.fill(globvar.MENU_FILL)
				
				if self.menu_label is not None:
					self.screen.blit(self.menu_label.label, self.menu_label.position)
 
				for item in self.items:
					self.screen.blit(item.image, item.position)
 
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
					if event.key == self.left:
						self.character.move_left()
					elif event.key == self.right:
						self.character.move_right()
					elif event.key == self.jump:
						self.character.jump()
						self.playSound('jump')
					#elif key == pygame.K_ESCAPE:
						
				# on key release
				if event.type == pygame.KEYUP:
					if event.key == self.left and self.character.change_x < 0:
						self.character.stop()
					elif event.key == self.right and self.character.change_x > 0:
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
				
	# level choice submenu
	def chooseLevel(self):
		# add numbers of all available levels (no level names for now)
		level_numbers = []
		for i in range (0, self.max_levels):
			level_numbers.append(str(i + 1))
		
		# initialize and display a submenu	
		menu_label = menuItem.MenuItem('Levels', None, 50, globvar.MENU_LABEL, 0, 0)
		pos_x = (self.scr_width / 2) - (menu_label.width / 2)
		pos_y = 120
		menu_label.set_position(pos_x, pos_y)
		self.initMenu(pygame.time.Clock(), None, 40, globvar.MENU_DEFAULT, level_numbers, True, 2, menu_label)	
		self.menuLoop()
	
	# settings submenu
	def settings(self):
		# initialize and display a submenu	
		menu_label = menuItem.MenuItem('Settings', None, 50, globvar.MENU_LABEL, 0, 0)
		pos_x = (self.scr_width / 2) - (menu_label.width / 2)
		pos_y = 120
		menu_label.set_position(pos_x, pos_y)
		
		self.initMenu(pygame.time.Clock(), None, 40, globvar.MENU_DEFAULT, ['Toggle sound', 'Sound volume', 'Controls'], True, 3, menu_label)	
		self.menuLoop()

	# customize controls
	def controls(self):
		# initialize and display a submenu	
		menu_label = menuItem.MenuItem('Controls', None, 50, globvar.MENU_LABEL, 0, 0)
		pos_x = (self.scr_width / 2) - (menu_label.width / 2)
		pos_y = 120
		menu_label.set_position(pos_x, pos_y)
		
		self.initMenu(pygame.time.Clock(), None, 40, globvar.MENU_DEFAULT, ['Left' + ' [ ' + pygame.key.name(self.left) + ' ]' , 'Right' + ' [ ' + pygame.key.name(self.right) + ' ]', 'Jump' + ' [ ' + pygame.key.name(self.jump) + ' ]'], True, 4, menu_label)	
		self.menuLoop()

	# check if sound is enabled
	def isSound(self):
		return self.game_music.isSound()
		
	# set sound
	def setSound(self, is_sound):
		self.game_music.setSound(is_sound)
		
	# toggle sound
	def toggleSound(self):
		self.setSound(not self.isSound())
		self.items[self.pos_volume].set_active(self.isSound())
		self.items[self.pos_toggle].set_text('Toggle sound' + ' ' + ('(Off)' if self.isSound() else '(On)'))	
			
	# play a given sound
	def playSound(self, key):
		self.game_music.playSound(key)
	
	# show how the key is entered
	def updateText(self, text):
		if text.startswith('Left'):
			self.items[0].set_text('Left <SELECT KEY>')
		elif text.startswith('Right'):
			self.items[1].set_text('Right <SELECT KEY>')
		else:
			self.items[2].set_text('Jump <SELECT KEY>')
	
	# change selected key
	def changeKey(self, text, current_key):
		if text.startswith('Left'):
			self.items[0].set_text('Left' + ' [ ' + pygame.key.name(current_key) + ' ]')
			self.left = current_key
		elif text.startswith('Right'):
			self.items[1].set_text('Right' + ' [ ' + pygame.key.name(current_key) + ' ]')
			self.right = current_key
		else:
			self.items[2].set_text('Jump' + ' [ ' + pygame.key.name(current_key) + ' ]')
			self.jump = current_key

    # reset control text
	def resetText(self, text):
		if text.startswith('Left'):
			self.items[0].set_text('Left' + ' [ ' + pygame.key.name(self.left) + ' ]')
		elif text.startswith('Right'):
			self.items[1].set_text('Right' + ' [ ' + pygame.key.name(self.right) + ' ]')
		else:
			self.items[2].set_text('Jump' + ' [ ' + pygame.key.name(self.jump) + ' ]')
	
	def volume(self):
		menu_label = menuItem.MenuItem('Customize sound volume', None, 50, globvar.MENU_LABEL, 0, 0)
		pos_x = (self.scr_width / 2) - (menu_label.width / 2)
		pos_y = 120
		menu_label.set_position(pos_x, pos_y)
		self.initVolMenu(pygame.time.Clock(), True, 5, menu_label)
		self.volMenuLoop()
	    
    
