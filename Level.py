import globvar

class Level(object):
	
	def __init__(self):
		self.platformsSet = None
		self.starsSet = None
		self.enemiesSet = None
		self.timeStart = None
		self.levelExit = None
	
	def update(self):
		self.starsSet.update()
		self.platformsSet.update()
		self.enemiesSet.update()
		self.levelExit.update()
		
	def draw(self, screen):
        # fill the background
		screen.fill(globvar.BACKGROUND_FILL)
		#update objects
		self.starsSet.draw(screen)
		self.platformsSet.draw(screen)
		self.enemiesSet.draw(screen)
		self.levelExit.draw(screen)