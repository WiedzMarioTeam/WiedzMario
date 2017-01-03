import pygame

# template class for all menu items
class MenuItem(pygame.font.Font):
    def __init__(self, text, font, font_size, font_color, pos_x, pos_y):
 
        pygame.font.Font.__init__(self, font, font_size)
        self.text = text
        self.font_size = font_size
        self.font_color = font_color
        self.label = self.render(self.text, 1, self.font_color)
        self.width = self.label.get_rect().width
        self.height = self.label.get_rect().height
        self.dimensions = (self.width, self.height)
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.position = pos_x, pos_y
        self.active = True
 
    # set the postion of menu item
    def set_position(self, x, y):
        self.position = (x, y)
        self.pos_x = x
        self.pos_y = y
 
    # set the font color of menu item
    def set_font_color(self, rgb_tuple):
        self.font_color = rgb_tuple
        self.label = self.render(self.text, 1, self.font_color)
    
    # set text of menu item
    def set_text(self, text):
		self.text = text

    # set active
    def set_active(self, active):
        self.active = active

    # check if item is active
    def is_active(self):
        return self.active
