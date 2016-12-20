import pygame, globvar
 
# class representing the player
class Player(pygame.sprite.Sprite):
	# constructor allowing to set positon, size and color of the player
	def __init__(self, pos_x, pos_y, size, fill_color):
		# call the parent constructor
		pygame.sprite.Sprite.__init__(self) 
			
		# set player size
		self.image = pygame.Surface([size, size])
		self.image.fill(fill_color)
	 
		# place the player in desired position (defined by top left vertex)
		self.rect = self.image.get_rect()
		self.rect.x = pos_x
		self.rect.y = pos_y
	 
		# set initial movement indicator to zero
		self.change_x = 0
		self.change_y = 0
		
		# player relative position
		self.level = None
		
    # update next movement depending on user's actions    
	def go_left(self):
		self.change_x = -globvar.STRIDE
 
	def go_right(self):
		self.change_x = globvar.STRIDE
 
	def stop(self):
		self.change_x = 0

	# update player position depending on user's action and collision detection
	def update(self):
		# update gravity
		self.update_gravity()
		# move player horizontally
		self.rect.x += self.change_x
		
		# check for collisions (x axis)
		collisions = pygame.sprite.spritecollide(self, self.level.platforms, False)
		for col in collisions:
			# make sure that there are no overlapping pixels
			if self.change_x < 0:
				self.rect.left = col.rect.right
			else:
				self.rect.right = col.rect.left
		
		# move player vertically
		self.rect.y += self.change_y
	 
		# check for collisions (y axis)
		collisions = pygame.sprite.spritecollide(self, self.level.platforms, False)
		for col in collisions:
			# make sure that there are no overlapping pixels
			if self.change_y < 0:
				self.rect.top = col.rect.bottom
			elif self.change_y > 0:
				self.rect.bottom = col.rect.top
				
			# reset vertical movement indicator
			self.change_y = 0	
    
	# compute gravity
	def update_gravity(self):
		# we don't want the player to be stuck under a platform
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += 0.30
 
		# ground is the bottom limit 
		if self.rect.y >= globvar.SCREEN_HEIGHT - self.rect.height - globvar.GROUND_LEVEL and self.change_y >= 0:
			self.change_y = 0
			self.rect.y = globvar.SCREEN_HEIGHT - self.rect.height - globvar.GROUND_LEVEL
 
	def jump(self):
        # check if the player is standing on a platform
		self.rect.y += 1
		platform_hit_list = pygame.sprite.spritecollide(self, self.level.platforms, False)
		self.rect.y -= 1
 
        # if so, jump
		if len(platform_hit_list) > 0:
			self.change_y = -11
 
    # update next movement depending on user's actions    
	def move_left(self):
		self.change_x = -globvar.STRIDE
 
	def move_right(self):
		self.change_x = globvar.STRIDE
 
	def stop(self):
		self.change_x = 0
