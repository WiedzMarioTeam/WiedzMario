# use pygame
import pygame

# screen size
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

# initialize pygame
pygame.init()

# create the game screen
screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])

# set the window title
pygame.display.set_caption('WiedzMario')

exit_clicked = False

# the event loop
while not exit_clicked:
	# process game events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_clicked = True

# after (x) button is clicked
pygame.quit()
