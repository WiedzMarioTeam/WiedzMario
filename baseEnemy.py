import pygame, globvar, enemy1Animation, enemy2Animation
 
# Podstawowa klasa reprezentujaca przeciwnika
class BaseEnemy(pygame.sprite.Sprite):
	# constructor allowing to set positon, size and color of the player
	def __init__(self, pos_x, pos_y, sizeWidth, sizeHeight, min_x, max_x, min_y, max_y, speed_x, speed_y, level, pointsForKill, animation):
		# call the parent constructor
		pygame.sprite.Sprite.__init__(self) 
			
		# set Enemy size
		self.image = pygame.Surface([sizeWidth, sizeHeight])
		self.animations = animation
	 
		# pozycja startowa przeciwnika
		self.rect = self.image.get_rect()
		self.rect.x = pos_x
		self.rect.y = pos_y
		
		#wspolrzedne pierwotne wroga
		self.originalX = pos_x
		self.originalY = pos_y
		
		# predkosc poczatkowa
		self.change_x = speed_x
		self.change_y = speed_y
		
		# zapisujemy predkosc wroga
		self.speed_x = speed_x
		self.speed_y = speed_y
		
		# ograniczenie ruchu wroga
		self.min_x = min_x
		self.max_x = max_x
		self.min_y = min_y
		self.max_y = max_y
		
		# Poziom w ktorym wystepuje przeciwnik
		self.level = level
		
		#punkty za zabicie wroga
		self.pointsForKill = pointsForKill
		
		#animacja roga
		self.current_img = 0
		self.ticksFromLastChange = 0
		self.flipImage = 0
		
		
	def moveEnemy(self):
		if self.rect.left <= self.min_x  and self.speed_x < 0:
			self.change_x = 0
			self.speed_x = -self.speed_x
		elif self.rect.right >= self.max_x and self.speed_x > 0:
			self.change_x = 0
			self.speed_x = -self.speed_x
		else: 
			self.change_x = self.speed_x
			
		# check if the Enemy is standing on a platform
		self.rect.y += 1
		platform_hit_list = pygame.sprite.spritecollide(self, self.level.platformsSet.platforms, False)
		self.rect.y -= 1
 
        # if so, jump
		if len(platform_hit_list) > 0:
			self.change_y = -self.speed_y
			
		
	# zaktualizuj pozycje wroga
	def update(self):
		# update gravity
		self.update_gravity()
		# przesun przeciwnika w poziomie
		self.rect.x += self.change_x
		
		# check for collisions (x axis)
		collisions = pygame.sprite.spritecollide(self, self.level.platformsSet.platforms, False)
		for col in collisions:
			# Kolizje uwzgledniamy tylko jesli nie lecimy do gory
			if self.change_y >= 0:
				# make sure that there are no overlapping pixels
				if self.change_x < 0:
					self.rect.left = col.rect.right
					self.speed_x *= -1
				else:
					self.rect.right = col.rect.left
					self.speed_x *= -1
					
			
		# move player vertically
		self.rect.y += self.change_y
	 
		# check for collisions (y axis)
		collisions = pygame.sprite.spritecollide(self, self.level.platformsSet.platforms, False)
		for col in collisions:
			# make sure that there are no overlapping pixels
			#if self.change_y < 0:
			#	self.rect.top = col.rect.bottom
			if self.change_y > 0:
				self.rect.bottom = col.rect.top				
				# reset vertical movement indicator only if we found conflict while moving down
				self.change_y = 0	
				
		if self.change_x == 0:
			self.ticksFromLastChange = 0
			self.current_img = 0
			if self.flipImage:
				self.image = pygame.transform.flip(self.animations.imageEnemyWalk[self.current_img], True, False)
			else:
				self.image = self.animations.imageEnemyWalk[0]
			
		else:
			self.ticksFromLastChange += 1
			self.ticksFromLastChange = self.ticksFromLastChange % (globvar.TICK/len(self.animations.imageEnemyWalk)/2)
		if self.ticksFromLastChange == 0:
				self.current_img += 1
				self.current_img = self.current_img % len(self.animations.imageEnemyWalk)
				if self.change_x < 0:
					self.image = pygame.transform.flip(self.animations.imageEnemyWalk[self.current_img], True, False)
					self.flipImage = True
				else:
					self.image = self.animations.imageEnemyWalk[self.current_img]
					self.flipImage = False

	# compute gravity
	def update_gravity(self):
		# we don't want the player to be stuck under a platform
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += 0.30
 
		if self.rect.bottom > self.level.height:
			self.level.enemiesSet.enemies.remove(self)
 
	def resetPosition(self):
		self.rect.x = self.originalX
		self.rect.y = self.originalY