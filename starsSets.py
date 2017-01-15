import pygame, globvar, envsurface

# create stars for a given level
class StarsSet1(object):
 
    def __init__(self, player):
		self.stars = pygame.sprite.Group()
		self.player = player
 
        # position, width, height and color of the platform
		stars = [[540, 850, 20, 20, globvar.COLOR_YELLOW],
                 [730, 650, 20, 20, globvar.COLOR_YELLOW],
                 [1050, 650, 20, 20, globvar.COLOR_YELLOW],
                 [1330, 650, 20, 20, globvar.COLOR_YELLOW],
                 [1650, 650, 20, 20, globvar.COLOR_YELLOW],
                 [3250, 900, 20, 20, globvar.COLOR_YELLOW]
                 ]
		
		for star in stars:
			surface = envsurface.EnvSurface(star[0], star[1], star[2], star[3], star[4])
			surface.player = self.player
			self.stars.add(surface)
	
	# update the level
    def update(self):
        self.stars.update()
 
    def draw(self, screen): 
        # draw the sprites
        self.stars.draw(screen)
		
		
########################### LEVEL 2 ###################################
class StarsSet2(object):
 
    def __init__(self, player):
		self.stars = pygame.sprite.Group()
		self.player = player
 
        # position, width, height and color of the platform
		stars = [[640, 700, 20, 20, globvar.COLOR_YELLOW],
                 [2460, 180, 15, 15, globvar.COLOR_YELLOW], #pierwszy rzad
                 [2500, 180, 15, 15, globvar.COLOR_YELLOW],
                 [2540, 180, 15, 15, globvar.COLOR_YELLOW],
                 [2580, 180, 15, 15, globvar.COLOR_YELLOW],
                 [2620, 180, 15, 15, globvar.COLOR_YELLOW],
                 [2480, 160, 15, 15, globvar.COLOR_YELLOW], #drugi rzad
                 [2520, 160, 15, 15, globvar.COLOR_YELLOW],
                 [2560, 160, 15, 15, globvar.COLOR_YELLOW],
                 [2600, 160, 15, 15, globvar.COLOR_YELLOW],
                 [2500, 140, 15, 15, globvar.COLOR_YELLOW], #trzeci rzad
                 [2540, 140, 15, 15, globvar.COLOR_YELLOW],
                 [2580, 140, 15, 15, globvar.COLOR_YELLOW],
                 [2520, 120, 15, 15, globvar.COLOR_YELLOW], #czwarty rzad
                 [2560, 120, 15, 15, globvar.COLOR_YELLOW],
                 [2540, 100, 15, 15, globvar.COLOR_YELLOW], #pierwszy rzad
                 [3865, 600, 15, 15, globvar.COLOR_YELLOW],  #dwie ostatnie
                 [4265, 600, 15, 15, globvar.COLOR_YELLOW]
                 ]

                 #[350, 350, 15, 15, globvar.COLOR_YELLOW],
                 #[600, 700, 15, 15, globvar.COLOR_YELLOW]]
		
		for star in stars:
			surface = envsurface.EnvSurface(star[0], star[1], star[2], star[3], star[4])
			surface.player = self.player
			self.stars.add(surface)
	
	# update the level
    def update(self):
        self.stars.update()
 
    def draw(self, screen): 
        # draw the sprites
        self.stars.draw(screen)