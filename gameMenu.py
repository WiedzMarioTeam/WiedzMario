import pygame, menuItem, volMenuItem, globvar

class GameMenu(object):
	def __init__(self):
		#create the game screen
		self.menu_loop = True
		self.change_keys = False
		self.current_item = None
		self.is_reset = False
		self.items = []
        
	
	# initialization of text menu object
	def initTextMenu(self, scr_width, scr_height, is_sound, font, font_size, font_color, menu_items, start_menu, menu_name, menu_label = None):
		#create the game screen
		self.font = font
		self.menu_items = menu_items
		self.start_menu = start_menu
		self.menu_name = menu_name
		self.menu_label = menu_label
        
		for index, item in enumerate(self.menu_items):
			# toggle sound logic
			if item == 'Toggle sound':
				item = 'Toggle sound' + ' ' + ('(Off)' if is_sound else '(On)')
			menu_item = menuItem.MenuItem(item, font, font_size, font_color, 0, 0)
			
			# sound volume logic
			if item == 'Sound volume':
				if not is_sound:
					menu_item.set_active(False)
					menu_item.set_font_color(globvar.MENU_INACTIVE)
 
            # height of text block
			block_height = len(self.menu_items) * menu_item.height
			pos_x = (scr_width / 2) - (menu_item.width / 2)
			pos_y = (scr_height / 2) - (block_height / 2) + ((index * 2) + index * menu_item.height)
            
			menu_item.set_position(pos_x, pos_y)
			self.items.append(menu_item)
			
			self.current_item = None
		
	
	# initialization of sound menu object
	def initVolMenu(self, scr_width, scr_height, game_music, menu_name, menu_label):
		#create the game screen
		self.menu_name = menu_name
		self.menu_label = menu_label
        
		initial_x = (scr_width - (globvar.MENU_VOL_NO * globvar.MENU_VOL_WIDTH) - ((globvar.MENU_VOL_NO - 1) *globvar.MENU_SPACE_BETWEEN)) / 2
		initial_y = scr_height - scr_height / 4
		
		for i in range(0, globvar.MENU_VOL_NO):
			width = globvar.MENU_VOL_WIDTH
			height = (i + 1) * globvar.MENU_VOL_HEIGHT

			menu_item = volMenuItem.VolMenuItem(width, height, (globvar.MENU_DEFAULT if i <= (game_music.sound_level) else globvar.MENU_INACTIVE), i, 0, 0)
 
			pos_x = initial_x + (i * globvar.MENU_VOL_WIDTH + i * globvar.MENU_SPACE_BETWEEN)
			pos_y = initial_y - (i * globvar.MENU_VOL_HEIGHT)
			menu_item.set_position(pos_x, pos_y)
			self.items.append(menu_item)
			
			self.current_item = None


	
