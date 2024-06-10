import pygame
import random as rd
from setting import Setting


class Font:
    def __init__(self):
        self.setting = Setting()
        self.font = pygame.font.SysFont('sans', 20)
        self.head = pygame.font.SysFont('sans', 50)
        self.bold_font=pygame.font.SysFont('sans',30,bold=True)
