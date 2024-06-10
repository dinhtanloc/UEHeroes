import pygame
import random as rd
from font import Font
from setting import Setting
from map import Map
from phat import Phat
from loc import Loc
from huong import Huong
from tu import Tu


class Screen:
    def __init__(self):
        self.setting = Setting()
        self.font = Font()
        self.map = Map()
        self.phat=Phat()
        self.loc=Loc()
        self.huong=Huong()
        self.tu=Tu()
        self.screen_width = self.setting.screen_width
        self.screen_length = self.setting.screen_length
        self.screen = pygame.display.set_mode((
            self.screen_length, self.screen_width))
        self.play_screen = pygame.display.set_mode((
            self.screen_length, self.screen_width))
        self.screen_image = pygame.image.load('screen.png')
        self.screen_image = pygame.transform.scale(
            self.screen_image, (self.screen_length, 500))
        self.play_screen_image = pygame.image.load('play_screen.png')
        self.dat = pygame.image.load('dat.jpg')
        self.dat = pygame.transform.scale(self.dat, (800, 100))
        self.dat1 = pygame.transform.scale(self.dat, (800, 250))
        self.phat_image = pygame.image.load('phat.png')
        self.phat_image = pygame.transform.scale(self.phat_image, (100, 100))
        self.loc_image = pygame.image.load('Loc.png')
        self.loc_image = pygame.transform.scale(self.loc_image, (100, 100))
        self.huong_image = pygame.image.load('Huong.png')
        self.huong_image = pygame.transform.scale(self.huong_image, (100, 100))
        self.tu_image = pygame.image.load('Tu.png')
        self.tu_image = pygame.transform.scale(self.tu_image, (100, 100))
        self.donut = self.map.donut1_image
        self.score_report=pygame.image.load("bang.jpeg")
        self.report=pygame.transform.scale(self.score_report,(333,333))
        self.Phat_screen_x=self.phat.x_screen
        self.Loc_screen_x=self.loc.x_screen
        self.Huong_screen_x=self.huong.x_screen
        self.Tu_screen_x=self.tu.x_screen
        self.Phat_screen_y=self.Loc_screen_y=self.Huong_screen_y=self.Tu_screen_y=420
        self.screen_ground_y=self.setting.screen_ground_y
        self.play_screen_ground_y=self.setting.playscreen_ground_y

    def draw_screen(self, screen):
        screen.blit(self.screen_image, (0, 0))

    def draw_head(self, screen, name, location, color,):
        head_word = self.font.head.render(name, True, color)
        screen.blit(head_word, location)
        return head_word
    
    def draw(self):
        self.screen.blit(self.dat1, (0, self.screen_ground_y))
        self.screen.blit(
            self.phat_image, (self.Phat_screen_x, self.Phat_screen_y))
        self.screen.blit(
            self.loc_image, (self.Loc_screen_x, self.Loc_screen_y))
        self.play_screen.blit(
            self.huong_image, (self.Huong_screen_x, self.Huong_screen_y))
        self.screen.blit(
            self.tu_image, (self.Tu_screen_x, self.Tu_screen_y))
        start_word = self.draw_head(self.screen, "Start",
                                    self.setting.start_location, self.setting.Co_text)
        word_rect = start_word.get_rect()
        pygame.Rect(
            self.setting.start_location[0], self.setting.start_location[1], word_rect[2], word_rect[3])
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if (self.setting.start_location[0] <= mouse_x <= self.setting.start_location[0]+word_rect[2]) and (self.setting.start_location[1] <= mouse_y <= self.setting.start_location[1]+word_rect[3]):
            self.setting.Co_text = (rd.randint(0, 255), rd.randint(
                0, 255), rd.randint(0, 255))
    
    def draw_play_screen(self, screen):
        screen.blit(self.play_screen_image, (0, 0))
        screen.blit(self.dat, (0, self.play_screen_ground_y))
        screen.blit(self.donut, (445, 575))



    def draw_font(self, screen, name, location, color):
        font_word = self.font.font.render(name, True, color)
        screen.blit(font_word, location)

    def draw_boldfont(self, screen, name, location, color):
        font_word = self.font.bold_font.render(name, True, color)
        screen.blit(font_word, location)
    
    def draw_score_report(self,screen,name,name2,location,location2,color):
        self.play_screen.blit(self.report,(self.setting.score_report_x,self.setting.score_report_y))
        self.draw_boldfont(self.play_screen,"Score:",(self.setting.score_boldfont_x,self.setting.score_boldfont_y),self.setting.Black)
        self.draw_font(screen,name,location,color)
        self.draw_boldfont(self.play_screen,"Time:",(self.setting.time_boldfont_x,self.setting.time_boldfont_y),self.setting.Black)
        self.draw_font(screen,name2,location2,color)
        self.draw_boldfont(self.play_screen,"Press space to restart",(self.setting.notice_x,self.setting.notice_y),self.setting.Black)

   
