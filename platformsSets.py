import pygame, globvar, envsurface, platformModule

# create platforms for a given level
class PlatformSet1(object):
 
    def __init__(self, player):
		self.platforms = pygame.sprite.Group()
		self.player = player
 
        # position, width, height and color of the platform
		platforms = [[0, 950, 2800, 50, globvar.SURFACE_FILL], #ziemia
                     [500, 900, 100, 50, globvar.SURFACE_FILL],
                     [700, 700, 400, 50, globvar.SURFACE_FILL],
                     [1300, 700, 400, 50, globvar.SURFACE_FILL],
                     [1900, 900, 100, 50, globvar.SURFACE_FILL],
                     [2400, 900, 100, 50, globvar.SURFACE_FILL],
                     [2700, 900, 100, 50, globvar.SURFACE_FILL],
                     [3200, 950, 1300, 50, globvar.SURFACE_FILL], #druga ziemia
                     [3300, 850, 400, 100, globvar.SURFACE_FILL],
                     [3400, 750, 300, 100, globvar.SURFACE_FILL],
                     [3500, 650, 200, 100, globvar.SURFACE_FILL],
                     [3600, 550, 100, 100, globvar.SURFACE_FILL]
                     ]
 
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
		platforms = [[0, 950, 300, 50, globvar.SURFACE_FILL], #ziemia
                     [600, 950, 100, 50, globvar.SURFACE_FILL], #ziemia
                     [1000, 950, 200, 50, globvar.SURFACE_FILL], #ziemia
                     [1100, 900, 100, 50, globvar.SURFACE_FILL],
                     [1550, 700, 100, 50, globvar.SURFACE_FILL],#gorne_polki
                     [2000, 500, 100, 50, globvar.SURFACE_FILL],
                     [2450, 400, 200, 50, globvar.SURFACE_FILL],
                     [2450, 200, 200, 50, globvar.SURFACE_FILL],
                     [1400, 950, 250, 50, globvar.SURFACE_FILL], #dol_pod_polkami
                     [1850, 950, 50, 50, globvar.SURFACE_FILL],
                     [2200, 950, 50, 50, globvar.SURFACE_FILL],
                     [2450, 950, 250, 50, globvar.SURFACE_FILL],
                     [2900, 950, 3000, 50, globvar.SURFACE_FILL],
                     [2900, 900, 100, 50, globvar.SURFACE_FILL],
                     [3400, 900, 100, 50, globvar.SURFACE_FILL],
                     [3400, 900, 100, 50, globvar.SURFACE_FILL],
                     [3400, 900, 100, 50, globvar.SURFACE_FILL],
                     [3850, 700, 50, 50, globvar.SURFACE_FILL], #dwie gorne blizej konca
                     [4250, 700, 50, 50, globvar.SURFACE_FILL],
                     [4700, 850, 400, 100, globvar.SURFACE_FILL], #piramida
                     [4800, 750, 300, 100, globvar.SURFACE_FILL],
                     [4900, 650, 200, 100, globvar.SURFACE_FILL],
                     [5000, 550, 100, 100, globvar.SURFACE_FILL]
                     ]

 
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
 