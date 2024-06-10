import pygame
class Music:
    def __init__(self):
        self.path='nhacnen.mp3'
    def load_music(self,path):
        pygame.mixer.music.load(path)
    def play_nhac(self):
        pygame.mixer.music.play(-1)