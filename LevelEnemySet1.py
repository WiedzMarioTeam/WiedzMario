import pygame, globvar, envsurface, baseEnemy

class LevelEnemySet1(object):
 
	def __init__(self, player, level):
		self.enemies = pygame.sprite.Group()
		self.player = player
 
        # pos_x, pos_y, size, min_x, max_x, min_y, max_y, speed_x, speed_y, level, pointsForKill, fill_color
		enemies = [baseEnemy.BaseEnemy(200, 748, 40, 100, 800, 748, 748, 1, 0, level, 15, globvar.COLOR_BLUE),
						baseEnemy.BaseEnemy(200, 748, 40, 950, 950, 748, 748, 0, 11, level, 15, globvar.COLOR_RED),
						baseEnemy.BaseEnemy(650, 250, 40, 600, 1000, 748, 748, 5, 0, level, 30, globvar.COLOR_GREEN),
						baseEnemy.BaseEnemy(650, 250, 40, 0, 1024, 748, 748, 3, 10, level, 50, globvar.COLOR_BLACK)]
						
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