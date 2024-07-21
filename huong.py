import pygame
from setting import Setting


class Huong:
    def __init__(self, file):
        self.setting = Setting()
        self.file = file
        self.image = pygame.image.load(self.file)
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.x = 100
        self.y = 300

  