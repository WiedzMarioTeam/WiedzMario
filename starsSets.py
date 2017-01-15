import pygame, globvar, envsurface, baseStar

class StarsSet1(object):
 
    def __init__(self, player):
		self.stars = pygame.sprite.Group()
		self.player = player
 
        # position, width, height and color of the platform
		stars = [baseStar.BaseStar(540, 850, 30, 45, 5, 0),
                 baseStar.BaseStar(730, 650, 30, 45, 5, 0),
                 baseStar.BaseStar(1050, 650, 30, 45, 5, 0),
                 baseStar.BaseStar(1330, 650, 30, 45, 5, 0),
                 baseStar.BaseStar(1650, 650, 30, 45, 5, 0),
                 baseStar.BaseStar(3250, 900, 30, 45, 5, 0)
                 ]

        # self.stars.add(starrr)
        # self.stars.add(stars[0])
		for star in stars:
			self.stars.add(star)

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
#		stars = [[640, 700, 20, 20, globvar.COLOR_YELLOW],
#                 [2460, 180, 15, 15, globvar.COLOR_YELLOW], #pierwszy rzad
#                 [2500, 180, 15, 15, globvar.COLOR_YELLOW],
#                 [2540, 180, 15, 15, globvar.COLOR_YELLOW],
#                 [2580, 180, 15, 15, globvar.COLOR_YELLOW],
#                 [2620, 180, 15, 15, globvar.COLOR_YELLOW],
#                 [2480, 160, 15, 15, globvar.COLOR_YELLOW], #drugi rzad
#                 [2520, 160, 15, 15, globvar.COLOR_YELLOW],
#                 [2560, 160, 15, 15, globvar.COLOR_YELLOW],
#                 [2600, 160, 15, 15, globvar.COLOR_YELLOW],
#                 [2500, 140, 15, 15, globvar.COLOR_YELLOW], #trzeci rzad
#                 [2540, 140, 15, 15, globvar.COLOR_YELLOW],
#                 [2580, 140, 15, 15, globvar.COLOR_YELLOW],
#                 [2520, 120, 15, 15, globvar.COLOR_YELLOW], #czwarty rzad
#                 [2560, 120, 15, 15, globvar.COLOR_YELLOW],
#                 [2540, 100, 15, 15, globvar.COLOR_YELLOW], #pierwszy rzad
#                 [3865, 600, 15, 15, globvar.COLOR_YELLOW],  #dwie ostatnie
#                 [4265, 600, 15, 15, globvar.COLOR_YELLOW]
#                 ]

#		for star in stars:
#			self.stars.add(star)

        # update the level
    def update(self):
        self.stars.update()
 
    def draw(self, screen): 
        # draw the sprites
        self.stars.draw(screen)
