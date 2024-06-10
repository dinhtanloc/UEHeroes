import pygame
from setting import Setting


class Loc:
    def __init__(self):
        self.setting = Setting()
        self.image = pygame.image.load('loc.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.x = 150
        self.y = 300
        self.x_screen=400
