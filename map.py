import pygame
import random as rd
from setting import Setting


class Map:
    def __init__(self):
        self.setting = Setting()
        self.image_1 = pygame.image.load('uiicheck.jpg')
        self.image_2 = pygame.image.load('error1.jpg')
        self.image_3 = pygame.image.load('error2.jpg')
        self.image_4 = pygame.image.load('error3.jpg')
        self.image_ground = pygame.image.load('dat.jpg')
        self.image_mon1ngc = pygame.image.load('thay.png')
        self.image_mon1ngc = pygame.transform.scale(
            self.image_mon1ngc, (50, 100))
        self.image_ground = pygame.transform.scale(
            self.image_ground, (self.setting.block_length, self.setting.block_width))
        self.image1 = pygame.transform.scale(
            self.image_1, (self.setting.block_length, self.setting.block_width))
        self.image2 = pygame.transform.scale(
            self.image_2, (self.setting.block_length, self.setting.block_width))
        self.image3 = pygame.transform.scale(
            self.image_3, (self.setting.block_length, self.setting.block_width))
        self.image4 = pygame.transform.scale(
            self.image_4, (self.setting.block_length, self.setting.block_width))
        self.image_5 = pygame.image.load('done.jpg')
        self.image5 = pygame.transform.scale(
            self.image_5, (self.setting.block_length, self.setting.block_width))
        self.block1_image = rd.choice(
            [self.image1, self.image2, self.image3, self.image4, self.image5])
        self.block2_image = rd.choice(
            [self.image1, self.image2, self.image3, self.image4, self.image5])
        self.block3_image = rd.choice(
            [self.image1, self.image2, self.image3, self.image4, self.image5])
        self.cay_image = pygame.image.load('cay.png')
        self.cay_image = pygame.transform.scale(self.cay_image, (50, 100))
        self.caygay_image = pygame.image.load('cay_gay.png')
        self.caygay_image = pygame.transform.scale(
            self.caygay_image, (50, 100))
        self.donut_image = pygame.image.load('donut.png')
        self.donut_image = pygame.transform.scale(self.donut_image, (50, 50))
        self.donut1_image = pygame.transform.scale(self.donut_image, (30, 30))
        self.block1_gay_image=pygame.image.load('error1_gay.png')
        self.block1_gay_image=pygame.transform.scale(self.block1_gay_image,(self.setting.block_length,self.setting.block_width))
        self.block2_gay_image=pygame.image.load('error2_gay.png')
        self.block2_gay_image=pygame.transform.scale(self.block2_gay_image,(self.setting.block_length,self.setting.block_width))
        self.block3_gay_image=pygame.image.load('error3_gay.png')
        self.block3_gay_image=pygame.transform.scale(self.block3_gay_image,(self.setting.block_length,self.setting.block_width))
        self.cay1_x = self.setting.cay1_x
        self.cay2_x = self.setting.cay2_x
        self.cay3_x = self.setting.cay3_x
        self.cay4_x = self.setting.cay4_x
        self.block1_x = self.setting.block1_x
        self.block2_x = self.setting.block2_x
        self.block3_x = self.setting.block3_x

   