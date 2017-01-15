import pygame, globvar, envsurface, baseEnemy, enemy1Animation, enemy2Animation

class EnemiesSet1(object):
 
	def __init__(self, player, level):
		self.enemies = pygame.sprite.Group()
		self.player = player
 
        # pos_x, pos_y, sizew, size H, min_x, max_x, min_y, max_y, speed_x, speed_y, level, pointsForKill, 
		enemies = [baseEnemy.BaseEnemy(200, 710, 74, 86, 100, 800, 748, 748, 1, 0, level, 15, enemy1Animation.enemy1Animation()),
						baseEnemy.BaseEnemy(200, 748, 74,86, 950, 950, 748, 748, 0, 11, level, 15, enemy1Animation.enemy1Animation()),
						baseEnemy.BaseEnemy(650, 250, 74,86, 600, 1000, 748, 748, 5, 0, level, 30, enemy1Animation.enemy1Animation()),
						baseEnemy.BaseEnemy(650, 250, 74,86, 0, 1024, 748, 748, 3, 10, level, 50, enemy2Animation.enemy2Animation())]
						
		for enemy in enemies:
			self.enemies.add(enemy)

	def update(self):
		self.enemies.update()
	
	def draw(self, screen):
		self.enemies.draw(screen)
		
	#Powrot wrogow na pierwotne miejsce
	def resetPositions(self):
		for enemy in self.enemies:
			enemy.resetPosition()
			
################################ LEVEL 2 ##################################
class EnemiesSet2(object):
 
	def __init__(self, player, level):
		self.enemies = pygame.sprite.Group()
		self.player = player
 
        # pos_x, pos_y, sizeH, sizeW, min_x, max_x, min_y, max_y, speed_x, speed_y, level, pointsForKill
		enemies = [baseEnemy.BaseEnemy(200, 748, 80,102, 100, 800, 748, 748, 1, 0, level, 15, enemy1Animation.enemy1Animation()),
						baseEnemy.BaseEnemy(200, 748, 80,102, 950, 950, 748, 748, 0, 11, level, 15, enemy1Animation.enemy1Animation()),
						baseEnemy.BaseEnemy(650, 250, 80,102, 0, 1024, 748, 748, 2, 10, level, 50, enemy2Animation.enemy2Animation())]
						
		for enemy in enemies:
			self.enemies.add(enemy)

	def update(self):
		self.enemies.update()
	
	def draw(self, screen):
		self.enemies.draw(screen)
		
	#Powrot wrogow na pierwotne miejsce
	def resetPositions(self):
		for enemy in self.enemies:
			enemy.resetPosition()