import pygame, menuItem, volMenuItem, globvar

class GameMenu(object):
	def __init__(self):
		#create the game screen
		self.menu_loop = True
		self.change_keys = False
		self.save_sound = False
		self.is_error = False
		self.pending_change = False
		self.is_saved = False
		self.current_item = None
		self.items = []
		self.tmp_sound = None
		self.tmp_left = None
		self.tmp_right = None
		self.tmp_jump = None
		self.menu_label_saved = None
		self.menu_label_save = None

	# initialization of text menu object
	def initTextMenu(self, scr_width, scr_height, is_sound, font, font_size, font_color, menu_items, start_menu, menu_name, menu_label = None, left = None, right = None, jump = None):
		#create the game screen
		self.font = font
		self.menu_items = menu_items
		self.start_menu = start_menu
		self.menu_name = menu_name
		self.menu_label = menu_label
		self.tmp_left = left
		self.tmp_right = right
		self.tmp_jump = jump
        
		for index, item in enumerate(self.menu_items):
			# toggle sound logic
			if item == 'Toggle sound':
				item = 'Toggle sound' + ' ' + ('(Off)' if is_sound else '(On)')
			menu_item = menuItem.MenuItem(item, font, font_size, font_color, 0, 0)
			
			# sound volume logic
			if item == 'Sound volume':
				if not is_sound:
					menu_item.set_active(False)
 
            # height of text block
			block_height = len(self.menu_items) * menu_item.height
			pos_x = (scr_width / 2) - (menu_item.width / 2)
			pos_y = (scr_height / 2) - (block_height / 2) + ((index * 2) + index * menu_item.height)
			
			menu_item.set_position(pos_x, pos_y)
			self.items.append(menu_item)
			
		self.menu_label_saved = menuItem.MenuItem('SETTINGS SUCCESSFULLY SAVED', None, 40, globvar.MENU_SAVED, 0, 0)
		block_height = (len(self.items) + 1) * self.menu_label_saved.height
		pos_x = (scr_width / 2) - (self.menu_label_saved.width / 2)
		pos_y = (scr_height / 2) - (block_height / 2) + ((len(self.items) * 2) + len(self.items) * self.menu_label_saved.height) + 2 * globvar.MENU_APPLY_SPACE
		self.menu_label_saved.set_position(pos_x, pos_y)
			
		self.menu_label_save = menuItem.MenuItem('ONE KEY CANNOT BE ASSIGNED TO MULTIPLE FUNCTIONS', None, 40, globvar.MENU_ERROR, 0, 0)
		block_height = (len(self.items) + 1) * self.menu_label_save.height
		pos_x = (scr_width / 2) - (self.menu_label_save.width / 2)
		pos_y = (scr_height / 2) - (block_height / 2) + ((len(self.items) * 2) + len(self.items) * self.menu_label_save.height) + 2 * globvar.MENU_APPLY_SPACE
		self.menu_label_save.set_position(pos_x, pos_y)
		
		self.current_item = None

	
	# initialization of sound menu object
	def initVolMenu(self, scr_width, scr_height, game_music, menu_name, menu_label):
		#create the game screen
		self.menu_name = menu_name
		self.menu_label = menu_label
		
		self.tmp_sound = game_music.sound_level
        
		initial_x = (scr_width - (globvar.MENU_VOL_NO * globvar.MENU_VOL_WIDTH) - ((globvar.MENU_VOL_NO - 1) * globvar.MENU_SPACE_BETWEEN)) / 2
		initial_y = scr_height - scr_height / 4
		
		for i in range(0, globvar.MENU_VOL_NO):
			width = globvar.MENU_VOL_WIDTH
			height = (i + 1) * globvar.MENU_VOL_HEIGHT

			menu_item = volMenuItem.VolMenuItem(width, height, (globvar.MENU_DEFAULT if i <= (game_music.sound_level) else globvar.MENU_INACTIVE), i, 0, 0)
 
			pos_x = initial_x + (i * globvar.MENU_VOL_WIDTH + i * globvar.MENU_SPACE_BETWEEN)
			pos_y = initial_y - (i * globvar.MENU_VOL_HEIGHT)
			menu_item.set_position(pos_x, pos_y)
			self.items.append(menu_item)
			
		self.menu_label_saved = menuItem.MenuItem('SETTINGS SUCCESSFULLY SAVED', None, 40, globvar.MENU_SAVED, 0, 0)
		block_height = (len(self.items) + 1) * self.menu_label_saved.height
		pos_x = (scr_width / 2) - (self.menu_label_saved.width / 2)
		pos_y = initial_y + globvar.MENU_APPLY_SPACE
		self.menu_label_saved.set_position(pos_x, pos_y)
		
		self.menu_label_save = menuItem.MenuItem('PRESS ENTER TO APPLY THE CHANGE', None, 40, globvar.MENU_SAVE, 0, 0)
		pos_x = (scr_width / 2) - (self.menu_label_save.width / 2)
		self.menu_label_save.set_position(pos_x, pos_y)
		
		self.current_item = None


	
