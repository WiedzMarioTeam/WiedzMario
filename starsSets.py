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
		stars = [baseStar.BaseStar(250, 550, 30, 45, 5, 0),
                 baseStar.BaseStar(350, 350, 30, 45, 5, 0),
                 baseStar.BaseStar(600, 700, 30, 45, 5, 0)]

		for star in stars:
			self.stars.add(star)

        # update the level
    def update(self):
        self.stars.update()
 
    def draw(self, screen): 
        # draw the sprites
        self.stars.draw(screen)
