import pygame, globvar, envsurface

# create platforms for a given level
class PlatformSet1(object):
 
    def __init__(self, player):
		self.platforms = pygame.sprite.Group()
		self.player = player
 
        # position, width, height and color of the platform
		platforms = [[200, 600, 210, 80, globvar.SURFACE_FILL],
                 [300, 400, 230, 70, globvar.SURFACE_FILL],
                 [600, 300, 400, 60, globvar.SURFACE_FILL],
                 [220, 200, 270, 50, globvar.SURFACE_FILL],
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
 