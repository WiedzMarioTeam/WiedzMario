import globvar

class Level(object):
	
	def __init__(self, width, height, player_x, player_y):
		self.platformsSet = None
		self.starsSet = None
		self.enemiesSet = None
		self.timeStart = None
		self.levelExit = None
		self.levelExitCastle = None
		self.nextLevelEntrance = None
		self.lifeSet = None
		self.width = width
		self.height = height
		self.start_x = player_x
		self.start_y = player_y
	
	def update(self):
		self.starsSet.update()
		self.platformsSet.update()
		self.enemiesSet.update()
		self.levelExit.update()
		if self.lifeSet is not None:
			self.lifeSet.update()
		if self.levelExitCastle is not None:
			self.levelExitCastle.update()
		if self.nextLevelEntrance is not None:
			self.nextLevelEntrance.update()
		
	def draw(self, screen):
        # fill the background
		screen.fill(globvar.BACKGROUND_FILL)
		#update objects
		self.starsSet.draw(screen)
		self.platformsSet.draw(screen)
		self.enemiesSet.draw(screen)
		self.levelExit.draw(screen)
		self.levelExitCastle.draw(screen)
		self.nextLevelEntrance.draw(screen)
		self.lifeSet.draw(screen)