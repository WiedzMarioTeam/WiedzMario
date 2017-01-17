import pygame, globvar, envsurface, baseStar

class StarsSet1(object):
 
    def __init__(self, player):
		self.stars = pygame.sprite.Group()
		self.player = player
 
        # position, width, height and color of the platform
		stars = [baseStar.BaseStar(540, 850),
                 baseStar.BaseStar(730, 650),
                 baseStar.BaseStar(1050, 650),
                 baseStar.BaseStar(1330, 650),
                 baseStar.BaseStar(1650, 650),
                 baseStar.BaseStar(3250, 900)
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
		stars = [baseStar.BaseStar(640, 700),
                 baseStar.BaseStar(2460, 180), #pierwszy rzad
                 baseStar.BaseStar(2500, 180),
                 baseStar.BaseStar(540, 180),
                 baseStar.BaseStar(2580, 180),
                 baseStar.BaseStar(2620, 180),
                 baseStar.BaseStar(2480, 160), #drugi rzad
                 baseStar.BaseStar(2520, 160),
                 baseStar.BaseStar(2560, 160),
                 baseStar.BaseStar(600, 160),
                 baseStar.BaseStar(2500, 140), #trzeci rzad
				 baseStar.BaseStar(2540, 140),
                 baseStar.BaseStar(2580, 140),
                 baseStar.BaseStar(2520, 120), #czwarty rzad
                 baseStar.BaseStar(2560, 120),
                 baseStar.BaseStar(2540, 100), #pierwszy rzad
                 baseStar.BaseStar(3865, 600),  #dwie ostatnie
                 baseStar.BaseStar(4265, 600)
                 ]

		for star in stars:
			self.stars.add(star)

        # update the level
    def update(self):
        self.stars.update()
 
    def draw(self, screen): 
        # draw the sprites
        self.stars.draw(screen)
