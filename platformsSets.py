import pygame, globvar, envsurface, platformModule

# create platforms for a given level
class PlatformSet1(object):
 
    def __init__(self, player):
		self.platforms = pygame.sprite.Group()
		self.player = player
 
        # position, width, height and color of the platform
		platforms = [[200, 600, 210, 80, globvar.SURFACE_FILL],
                 [300, 400, 230, 70, globvar.SURFACE_FILL],
                 [600, 300, 1200, 60, globvar.SURFACE_FILL],
                 [320, 200, 270, 50, globvar.SURFACE_FILL],
				 [1400, 950, 230, 70, globvar.SURFACE_FILL],
                 [1000, 1300, 800, 60, globvar.SURFACE_FILL],
                 [290, 1400, 270, 50, globvar.SURFACE_FILL],
				 [400, 950, 230, 70, globvar.SURFACE_FILL],
                 [800, 1050, 1200, 60, globvar.SURFACE_FILL],
                 [500, 1200, 270, 50, globvar.SURFACE_FILL],
				 [0, 750, 1200, 50, globvar.SURFACE_FILL],
				 [1400, 750, 800, 50, globvar.SURFACE_FILL],
                 [0, 1500, 800, 100, globvar.SURFACE_FILL],
				 [1000, 1500, 1500, 100, globvar.SURFACE_FILL]]
 
        # add the platforms
		for surface in platforms:
			platform = platformModule.Platform(surface[0], surface[1], surface[2], surface[3], surface[4])
			self.platforms.add(platform)
	
	# update the level
    def update(self):
        self.platforms.update()
 
    def draw(self, screen):
        # draw the sprites
        self.platforms.draw(screen)
 
######################  LEVEL 2 ##############################################
class PlatformSet2(object):
 
    def __init__(self, player):
		self.platforms = pygame.sprite.Group()
		self.player = player
 
        # position, width, height and color of the platform
		platforms = [[300, 400, 230, 70, globvar.SURFACE_FILL],
                 [600, 300, 400, 60, globvar.SURFACE_FILL],
                 [0, 748, 1024, 20, globvar.SURFACE_FILL]]
 
        # add the platforms
		for platform in platforms:
			surface = envsurface.EnvSurface(platform[0], platform[1], platform[2], platform[3], platform[4])
			surface.player = self.player
			self.platforms.add(surface)
	
	# update the level
    def update(self):
        self.platforms.update()
 
    def draw(self, screen):
        # draw the sprites
        self.platforms.draw(screen)
 