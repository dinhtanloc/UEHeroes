import pygame
from setting import Setting


class Phat:
    def __init__(self):
        self.setting = Setting()
        self.image = pygame.image.load('phat.png')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.x = 200
        self.y = 300
        self.x_screen=500
