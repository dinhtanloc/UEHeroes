import pygame
from setting import Setting


class Huong:
    def __init__(self):
        self.setting = Setting()
        self.image = pygame.image.load('Huong.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.x = 100
        self.y = 300
        self.x_screen=300

  