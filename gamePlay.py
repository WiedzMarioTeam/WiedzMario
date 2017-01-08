import pygame, player, envsurface, platformsSets, globvar, baseEnemy, enemiesSets, starsSets, Level, time, levelExit, utilsSet, cameraModule, menuItem, volMenuItem, gameMusic, gameMenu, sys

class GamePlay(object):
	# set basic game settings
	def __init__(self):
		self.main_loop = True
		self.gameplay_loop = False
		self.max_levels = globvar.LEVEL_NO
		self.player_positions = {'1': (100, 1300), '2': (100, 650)}
		# object handling class music
		self.game_music = gameMusic.GameMusic(2, {'jump': 'sfx/jump.wav',
                                                  'enemy_death': 'sfx/death1.wav',
                                                  'player_death': 'sfx/death2.wav',
                                                  'gameover': 'sfx/gameover.wav',
                                                  'win': 'sfx/win.wav'})
		# control keys
		self.jump = pygame.K_SPACE
		self.left = pygame.K_LEFT
		self.right = pygame.K_RIGHT
		self.change_keys = False
		# screen parameters
		self.screen = pygame.display.set_mode((globvar.SCREEN_WIDTH, globvar.SCREEN_HEIGHT), 0, 32)
		self.scr_width = self.screen.get_rect().width
		self.scr_height = self.screen.get_rect().height
		pygame.display.set_caption('Mario')	
		self.utils = utilsSet.Utils(self.screen)
		self.clock = pygame.time.Clock()
		# menu tree
		self.menu_tree = {}
		self.fun_dict = {}
		self.populateMenuTree()
		self.setFunDict()
		self.menuLoop(self.menu_tree['main'])

	
	# create game menu
	def populateMenuTree(self):
		self.menu_tree['main'] = gameMenu.GameMenu()
		self.menu_tree['main_game'] = gameMenu.GameMenu()
		self.menu_tree['settings'] = gameMenu.GameMenu()
		self.menu_tree['levels'] = gameMenu.GameMenu()
		self.menu_tree['controls'] = gameMenu.GameMenu()
		self.menu_tree['sound'] = gameMenu.GameMenu()
		
		self.menu_tree['main'].initTextMenu(self.scr_width, self.scr_height, self.isSound(), None, 40, globvar.MENU_DEFAULT, ['Start', 'Choose level', 'Settings', 'Quit'], True, 'main')
		self.menu_tree['main_game'].initTextMenu(self.scr_width, self.scr_height, self.isSound(), None, 40, globvar.MENU_DEFAULT, ['Resume', 'Settings', 'Return to main menu', 'Quit'], False, 'main_game')
		self.menu_tree['settings'].initTextMenu(self.scr_width, self.scr_height, self.isSound(), None, 40, globvar.MENU_DEFAULT, ['Toggle sound', 'Sound volume', 'Controls'], True, 'settings', self.getMenuLabel('Settings'))
		self.menu_tree['levels'].initTextMenu(self.scr_width, self.scr_height, self.isSound(), None, 40, globvar.MENU_DEFAULT, self.getLevels(), True, 'levels', self.getMenuLabel('Choose level'))
		self.menu_tree['controls'].initTextMenu(self.scr_width, self.scr_height, self.isSound(), None, 40, globvar.MENU_DEFAULT, ['Left' + ' [ ' + pygame.key.name(self.left) + ' ]' , 'Right' + ' [ ' + pygame.key.name(self.right) + ' ]', 'Jump' + ' [ ' + pygame.key.name(self.jump) + ' ]'], True, 'controls', self.getMenuLabel('Customize controls'), self.left, self.right, self.jump)
		self.menu_tree['sound'].initVolMenu(self.scr_width, self.scr_height, self.game_music, 'sound', self.getMenuLabel('Customize sound volume'))
		
	
	# set function dictionary
	def setFunDict(self):
		self.fun_dict['main'] = self.setKeySelectionMain
		self.fun_dict['main_game'] = self.setKeySelectionMain
		self.fun_dict['settings'] = self.setKeySelectionSettings
		self.fun_dict['levels'] = self.setKeySelectionLevels
		self.fun_dict['controls'] = self.setKeySelectionControls
		self.fun_dict['sound'] = self.setKeySelectionSound
	
	# create menu label
	def getMenuLabel(self, text):
		menu_label = menuItem.MenuItem(text, None, 50, globvar.MENU_LABEL, 0, 0)
		pos_x = (self.scr_width / 2) - (menu_label.width / 2)
		pos_y = globvar.MENU_LABEL_Y
		menu_label.set_position(pos_x, pos_y)
		
		return menu_label
		
	
	# get levels list
	def getLevels(self):
		# add numbers of all available levels (no level names for now)
		level_numbers = []
		for i in range (0, self.max_levels):
			level_numbers.append(str(i + 1))
		
		return level_numbers
	
	
	# display the menu  
	def menuLoop(self, menu):
		# a little trick to highlight the first position when menu is entered
		self.fun_dict[menu.menu_name](menu, None)
		
		while menu.menu_loop:
			self.clock.tick(globvar.TICK)
            
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
				if event.type == pygame.KEYDOWN:
						self.fun_dict[menu.menu_name](menu, event.key)

			if menu.menu_loop:
				self.screen.fill(globvar.MENU_FILL)
				
				if menu.menu_label is not None:
					self.screen.blit(menu.menu_label.label, menu.menu_label.position)
				
				if menu.save_sound or menu.is_error:
					self.screen.blit(menu.menu_label_save.label, menu.menu_label_save.position)
				if menu.is_saved:
					self.screen.blit(menu.menu_label_saved.label, menu.menu_label_saved.position)	
 
				# display menu positons depending on their type
				if menu.menu_name == 'sound':
					for item in menu.items:
						if isinstance(item, volMenuItem.VolMenuItem):
							self.screen.blit(item.image, item.position)
						else:
							self.screen.blit(item.label, item.position)
				else:
					for item in menu.items:
						self.screen.blit(item.label, item.position)
 
				pygame.display.flip()
				
	
			
    # process main menu events
	def setKeySelectionMain(self, menu, key):
			
		for item in menu.items:
			item.set_bold(False)
			# reset all active items
			if item.is_active():
				item.set_font_color(globvar.MENU_DEFAULT)
			else:
				item.set_font_color(globvar.MENU_INACTIVE)
	
		if menu.current_item is None:
			menu.current_item = 0
			menu.items[menu.current_item].set_font_color(globvar.MENU_ACTIVE)
		else:	
			if key == pygame.K_UP and menu.current_item > 0:
				menu.current_item -= 1
			elif key == pygame.K_UP and menu.current_item == 0:
				menu.current_item = len(menu.items) - 1
			elif key == pygame.K_DOWN and menu.current_item < len(menu.items) - 1:
				menu.current_item += 1
			elif key == pygame.K_DOWN and menu.current_item == len(menu.items) - 1:
				menu.current_item = 0
 
		# highlight the selected item
		menu.items[menu.current_item].set_bold(True)
		menu.items[menu.current_item].set_font_color(globvar.MENU_ACTIVE)
        
        # check if any menu button was "pressed"
		if key == pygame.K_RETURN:
			text = menu.items[menu.current_item].text
			if text == 'Start':
				self.main_loop = True
				self.initGame(pygame.font.SysFont("comicsansms", 40), player.Player(self.player_positions['1'], globvar.PLAYER_SIZE, globvar.PLAYER_FILL), pygame.time.Clock(), 1)
			elif text == 'Settings':
				self.menu_tree['settings'].menu_loop = True
				self.menuLoop(self.menu_tree['settings'])
			elif text == 'Choose level':
				self.menu_tree['levels'].menu_loop = True
				self.menuLoop(self.menu_tree['levels'])
			elif text == 'Quit':
				sys.exit()
			elif text == 'Resume':
				menu.current_item = 0
				menu.menu_loop = False
			elif text == 'Return to main menu':
				menu.menu_loop = False
				self.main_loop = False
		
		# resume game logic
		if key == pygame.K_ESCAPE and not menu.start_menu:
			menu.current_item = 0
			menu.menu_loop = False
			

	
	# process settings menu events
	def setKeySelectionSettings(self, menu, key):
		for item in menu.items:
			item.set_bold(False)
			# reset all active items
			if item.is_active():
				item.set_font_color(globvar.MENU_DEFAULT)
			else:
				item.set_font_color(globvar.MENU_INACTIVE)
				
		if menu.current_item is None:
			menu.current_item = 0
			menu.items[menu.current_item].set_font_color(globvar.MENU_ACTIVE)
		else:
			if key == pygame.K_UP and menu.current_item > 0:
				menu.current_item -= 1
			elif key == pygame.K_UP and menu.current_item == 0:
				menu.current_item = len(menu.items) - 1
			elif key == pygame.K_DOWN and menu.current_item < len(menu.items) - 1:
				menu.current_item += 1
			elif key == pygame.K_DOWN and menu.current_item == len(menu.items) - 1:
				menu.current_item = 0
 
		# highlight the selected item
		menu.items[menu.current_item].set_bold(True)
		menu.items[menu.current_item].set_font_color(globvar.MENU_ACTIVE)
        
        # check if any menu button was "pressed"
		if key == pygame.K_RETURN:
			text = menu.items[menu.current_item].text
			if text.startswith('Toggle sound'):
				self.toggleSound(menu)
				# a little trick to refresh menu positions in real time
				key = None
				self.setKeySelectionSettings(menu, key)
			elif text == 'Controls':
				self.menu_tree['controls'].menu_loop = True
				self.menuLoop(self.menu_tree['controls'])
			elif text == 'Sound volume' and menu.items[menu.current_item].is_active():
				self.menu_tree['sound'].menu_loop = True
				self.menuLoop(self.menu_tree['sound'])
			elif text == 'Sound volume' and not menu.items[menu.current_item].is_active():
				return	
		
		# escape key allows the user to go level up in menu
		if key == pygame.K_ESCAPE:
			menu.current_item = 0
			menu.menu_loop = False
	
	
	# process levels menu events
	def setKeySelectionLevels(self, menu, key):
		for item in menu.items:
			item.set_bold(False)
			# reset all active items
			item.set_font_color(globvar.MENU_DEFAULT)
				
		if menu.current_item is None:
			menu.current_item = 0
			menu.items[menu.current_item].set_font_color(globvar.MENU_ACTIVE)
		else:	
			if key == pygame.K_UP and menu.current_item > 0:
				menu.current_item -= 1
			elif key == pygame.K_UP and menu.current_item == 0:
				menu.current_item = len(menu.items) - 1
			elif key == pygame.K_DOWN and menu.current_item < len(menu.items) - 1:
				menu.current_item += 1
			elif key == pygame.K_DOWN and menu.current_item == len(menu.items) - 1:
				menu.current_item = 0
 
		# highlight the selected item
		menu.items[menu.current_item].set_bold(True)
		menu.items[menu.current_item].set_font_color(globvar.MENU_ACTIVE)
        
        # check if any menu button was "pressed"
		if key == pygame.K_RETURN:
			text = menu.items[menu.current_item].text
			menu.menu_loop = False
			self.main_loop = True
			menu.current_item = 0
			self.initGame(pygame.font.SysFont("comicsansms", 40), player.Player(self.player_positions[text], globvar.PLAYER_SIZE, globvar.PLAYER_FILL), pygame.time.Clock(), int(text))
			# a little trick to reset main menu after gameplay 
			self.setKeySelectionMain(self.menu_tree['main'], pygame.K_UP) 
		# escape key allows the user to go level up in menu
		if key == pygame.K_ESCAPE:
			menu.menu_loop = False
			menu.current_item = 0		
	
	
	# process control customization menu
	def setKeySelectionControls(self, menu, key):
		for item in menu.items:
			item.set_bold(False)
			# reset all active items
			if item.is_active and item.text == 'Apply the change(s)':
				item.set_font_color(globvar.MENU_SAVE)
			else:
				item.set_font_color(globvar.MENU_DEFAULT)
		
		if menu.current_item is None:
			menu.current_item = 0
			menu.items[menu.current_item].set_font_color(globvar.MENU_ACTIVE)
		elif not menu.change_keys:
			# reset the error message
			if key == pygame.K_UP or key == pygame.K_DOWN and menu.is_error:
				menu.is_error = False
			# reset the save message
			if key == pygame.K_UP or key == pygame.K_DOWN and menu.is_saved:
				menu.is_saved = False
 			if key == pygame.K_UP and menu.current_item > 0:
				menu.current_item -= 1
			elif key == pygame.K_UP and menu.current_item == 0:
				menu.current_item = len(menu.items) - 1
			elif key == pygame.K_DOWN and menu.current_item < len(menu.items) - 1:
				menu.current_item += 1
			elif key == pygame.K_DOWN and menu.current_item == len(menu.items) - 1:
				menu.current_item = 0

		# highlight the selected item
		menu.items[menu.current_item].set_bold(True)
		menu.items[menu.current_item].set_font_color(globvar.MENU_ACTIVE)
		
		# show which item is being modified
		if menu.change_keys:
			menu.is_saved = False
			menu.items[menu.current_item].set_font_color(globvar.MENU_CHANGE)
		else:
			menu.items[menu.current_item].set_font_color(globvar.MENU_ACTIVE)
			
		# check if control change is to be performed
		if menu.change_keys and key == pygame.K_ESCAPE:
			text = menu.items[menu.current_item].text
			self.resetText(menu, text)
			menu.change_keys = False
			key = None
			self.setKeySelectionControls(menu, key)
		elif menu.change_keys and key != pygame.K_RETURN:
			text = menu.items[menu.current_item].text
			self.changeKey(menu, text, key)
			if menu.tmp_left != self.left or menu.tmp_right != self.right or menu.tmp_jump != self.jump:
				# detect duplicate key assignment
				if len([menu.tmp_left, menu.tmp_right, menu.tmp_jump]) != len(set([menu.tmp_left, menu.tmp_right, menu.tmp_jump])):
					menu.is_error = True
					self.resetAllText(menu)
					menu.current_item = 0
				elif not menu.pending_change:
					self.enableSaveKeys(menu)
			elif menu.pending_change:
				self.removeApply(menu)
				menu.pending_change = False
			menu.change_keys = False
			key = None
			self.setKeySelectionControls(menu, key)

        # check if any menu button was "pressed"
		if key == pygame.K_RETURN and not menu.change_keys:
			menu.menu_loop = True
			text = menu.items[menu.current_item].text
			if text.startswith('Left') or text.startswith('Right') or text.startswith('Jump'):
				menu.change_keys = True
				self.updateText(menu, text)
				self.setKeySelectionControls(menu, key)
			# save changes
			if text == 'Apply the change(s)':
				self.saveChanges(menu)
				self.resetAllText(menu)
				self.removeApply(menu)
				menu.is_saved = True
				menu.pending_change = False
				self.setKeySelectionControls(menu, None)
		
		# escape key allows the user to go level up in menu
		if key == pygame.K_ESCAPE:
			self.resetAllText(menu)
			if menu.pending_change:
				self.removeApply(menu)
			menu.menu_loop = False
			menu.is_saved = False
			menu.is_error = False
			menu.current_item = 0
    
	
	# process volume customization menu
	def setKeySelectionSound(self, menu, key):
		if menu.current_item is None:
			if key == pygame.K_LEFT and menu.tmp_sound == 0:
				menu.current_item = 0
			elif key == pygame.K_LEFT and menu.tmp_sound > 0:
				menu.current_item = menu.tmp_sound - 1
				menu.tmp_sound -= 1
			elif key == pygame.K_RIGHT and menu.tmp_sound < globvar.MENU_VOL_NO - 1:
				menu.current_item = menu.tmp_sound + 1
				menu.tmp_sound += 1
			elif key == pygame.K_RIGHT and menu.tmp_sound == globvar.MENU_VOL_NO - 1:
				menu.current_item = globvar.MENU_VOL_NO -1
		else:
			menu.is_saved = False
			if key == pygame.K_LEFT and menu.current_item == 0:
				menu.current_item = 0
			elif key == pygame.K_LEFT and menu.current_item > 0:
				menu.current_item -= 1
				menu.tmp_sound -= 1
			elif key == pygame.K_RIGHT and menu.current_item < globvar.MENU_VOL_NO - 1:
				menu.current_item += 1
				menu.tmp_sound += 1
			elif key == pygame.K_RIGHT and menu.current_item == globvar.MENU_VOL_NO - 1:
				menu.current_item = globvar.MENU_VOL_NO -1
			elif key == pygame.K_DOWN and menu.pending_change:
				menu.current_item = globvar.MENU_VOL_NO
		
		# escape key allows the user to go level up in menu
		if key == pygame.K_ESCAPE:
				self.resetSoundMenu(menu)
				menu.menu_loop = False
				
		if menu.tmp_sound != self.game_music.sound_level:
			menu.save_sound = True
		elif menu.save_sound and menu.tmp_sound == self.game_music.sound_level:
			menu.save_sound = False
		
		# save new sound settings
		if menu.save_sound and key == pygame.K_RETURN:
			self.saveSound(menu)
				
		for item in menu.items:
			# set color based on current volume
			if item.value <= menu.tmp_sound:
				item.set_color(globvar.MENU_DEFAULT)
			else:
				item.set_color(globvar.MENU_INACTIVE)
		
	
	# initialization of the actual gameplay
	def initGame(self, font, character, clock, current_level_no):
		self.font = font
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
		while self.main_loop:
		
			#przetwarzamy ruchy przeciwnikow
			for enemy in self.currentLevel.enemiesSet.enemies:
				enemy.moveEnemy()
		
			# process game events
			for event in pygame.event.get():
				
				if event.type == pygame.QUIT:
					self.main_loop = False
				# on key press
				if event.type == pygame.KEYDOWN:
					if event.key == self.left:
						self.character.move_left()
					elif event.key == self.right:
						self.character.move_right()
					elif event.key == self.jump:
						self.character.jump(self.game_music)
					elif event.key == pygame.K_ESCAPE:
						self.menu_tree['main_game'].menu_loop = True
						self.menuLoop(self.menu_tree['main_game'])
						
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
	 
			self.character.checkCollisionsWithEnemies(self.game_music)

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
						self.playSound('win')
						pygame.time.delay(3000)
						self.main_loop = False
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
				self.game_music.playSound('player_death')
				self.character.lifeLost()
				
			#Jesli zostalo 0 zyc, to funkcja informuje o koncu gry			
			if self.character.lives == 0:
				self.playSound('gameover')
				self.utils.gameOver(self.currentLevel, self.screen, self.character)
				self.main_loop = False
			
			# in case of end-game
			if self.main_loop == False:
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
				


	# check if sound is enabled
	def isSound(self):
		return self.game_music.isSound()
		

	# set sound
	def setSound(self, is_sound):
		self.game_music.setSound(is_sound)

		
	# toggle sound
	def toggleSound(self, menu):
		self.setSound(not self.isSound())
		menu.items[globvar.SOUND].set_active(self.isSound())
		menu.items[globvar.TOGGLE].set_text('Toggle sound' + ' ' + ('(Off)' if self.isSound() else '(On)'))	

			
	# play a given sound
	def playSound(self, key):
		self.game_music.playSound(key)

	
	# show how the key is entered
	def updateText(self, menu, text):
		if text.startswith('Left'):
			menu.items[0].set_text('Left <SELECT KEY>')
		elif text.startswith('Right'):
			menu.items[1].set_text('Right <SELECT KEY>')
		else:
			menu.items[2].set_text('Jump <SELECT KEY>')
	

	# change selected key
	def changeKey(self, menu, text, current_key):
		if text.startswith('Left'):
			menu.items[0].set_text('Left' + ' [ ' + pygame.key.name(current_key) + ' ]')
			#self.left = current_key
			menu.tmp_left = current_key
		elif text.startswith('Right'):
			menu.items[1].set_text('Right' + ' [ ' + pygame.key.name(current_key) + ' ]')
			#self.right = current_key
			menu.tmp_right = current_key
		else:
			menu.items[2].set_text('Jump' + ' [ ' + pygame.key.name(current_key) + ' ]')
			#self.jump = current_key
			menu.tmp_jump = current_key


	# change selected key
	def saveChanges(self, menu):
			self.left = menu.tmp_left
			self.right = menu.tmp_right
			self.jump = menu.tmp_jump


    # reset control text
	def resetText(self, menu, text):
		if text.startswith('Left'):
			menu.items[0].set_text('Left' + ' [ ' + pygame.key.name(self.left) + ' ]')
		elif text.startswith('Right'):
			menu.items[1].set_text('Right' + ' [ ' + pygame.key.name(self.right) + ' ]')
		else:
			menu.items[2].set_text('Jump' + ' [ ' + pygame.key.name(self.jump) + ' ]')
			
			
	# reset all texts
	def resetAllText(self, menu):
			menu.tmp_left = self.left
			menu.tmp_right = self.right
			menu.tmp_jump = self.jump
			menu.items[0].set_text('Left' + ' [ ' + pygame.key.name(self.left) + ' ]')
			menu.items[1].set_text('Right' + ' [ ' + pygame.key.name(self.right) + ' ]')
			menu.items[2].set_text('Jump' + ' [ ' + pygame.key.name(self.jump) + ' ]')

	
	# def remove apply button
	def removeApply(self, menu):
		menu.items.pop()
		menu.current_item = None
	
	
	# make it possible to save settings
	def enableSaveKeys(self, menu):
		menu_item = menuItem.MenuItem('Apply the change(s)', None, 40, globvar.MENU_SAVE, 0, 0)
		pos_x = (self.scr_width / 2) - (menu_item.width / 2)
		block_height = (len(menu.items)) * menu_item.height
		pos_y = (self.scr_height / 2) - (block_height / 2) + ((len(menu.items)) * 2) + (len(menu.items)) * menu_item.height
		menu_item.set_position(pos_x, pos_y)
		menu.items.append(menu_item)
		menu.pending_change = True

	
	# save sound value
	def saveSound(self, menu):
		self.game_music.sound_level = menu.tmp_sound
		menu.save_sound = False
		menu.is_saved = True
		
	# reset sound menu
	def resetSoundMenu(self, menu):
		menu.tmp_sound = self.game_music.sound_level
		menu.save_sound = False
