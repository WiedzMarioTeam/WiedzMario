import pygame, globvar, envsurface, baseStar


# create stars for a given level
class StarsSet1(object):
    def __init__(self, player):
        self.stars = pygame.sprite.Group()
        self.player = player
        # starsImg =
        # position, width, height and color of the platform
        # baseStar(200, 1450, 15, 15,5,0,0)
        # stars = [[350, 350, 15, 15, globvar.COLOR_YELLOW],
        #          [650, 250, 15, 15, globvar.COLOR_YELLOW],
        #          [270, 150, 15, 15, globvar.COLOR_YELLOW],
        #          [850, 700, 15, 15, globvar.COLOR_YELLOW]]

        stars = [baseStar.BaseStar(200, 1450, 30, 45, 5, 0),
                 baseStar.BaseStar(650, 250, 30, 45, 5, 0),
                 baseStar.BaseStar(270, 150, 30, 45, 5, 0),
                 baseStar.BaseStar(850, 700, 30, 45, 5, 0)]

        # self.stars.add(starrr)
        # self.stars.add(stars[0])
        for star in stars:
        #     surface = envsurface.EnvSurface( star[0], star[1], star[2], star[3], star[4])
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
