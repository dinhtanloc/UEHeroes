import pygame
from setting import Setting


class Tu:
    def __init__(self):
        self.setting = Setting()
        self.image = pygame.image.load('Tu.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.x = 50
        self.y = 300
        self.x_screen=200