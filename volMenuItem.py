import pygame

# class for volume adjustment
class VolMenuItem(pygame.sprite.Sprite):
    def __init__(self, size_x, size_y, color, value, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        
        self.image = pygame.Surface([size_x, size_y])
        self.color = color
        self.image.fill(color)
        self.value = value
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.position = pos_x, pos_y
        
        #self.width = self.width
        #self.height = self.height
        #self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y
        self.active = True
 
    # set the postion of volume menu item
    def set_position(self, x, y):
        self.position = (x, y)
        self.rect.x = x
        self.rect.y = y
 
    # set the color of volume menu item
    def set_color(self, rgb_tuple):
		self.color = rgb_tuple
		self.image.fill(rgb_tuple)
    
    # set active
    def set_active(self, active):
        self.active = active

    # check if item is active
    def is_active(self):
        return self.active
