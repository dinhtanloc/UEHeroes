import pygame
import random as rd
from map import Map
from setting import Setting
from phat import Phat
from loc import Loc
from huong import Huong
from tu import Tu
from screen import Screen
class Logic:
    def __init__(self):
        self.setting = Setting()
        self.screen = Screen()
        self.map = Map()
        self.phat = Phat("phat.png")
        self.loc = Loc("Loc.png")
        self.huong = Huong("Huong.png")
        self.tu = Tu("Tu.png")
        self.logic_variable_definition()

    def clock_setting(self):
        if self.clock:
            self.mins = int(self.total_secs/60)
            self.total_secs += self.sec
            self.secs = self.total_secs - self.mins*60
            self.point = self.total_secs*1
            self.time_now = str(self.mins) + " : " + str(self.secs)
            self.point_now = str(self.point)


    def map_law(self):
        if self.check_Phat != True:
            if self.Phat_y >= 500:
                self.Phat_y = self.Loc_y = self.Huong_y = self.Tu_y = 500
                self.GRAVITY = 0
                self.mon_return()
            elif self.Phat_y <= 0:
                self.Phat_y = self.Loc_y = self.Huong_y = self.Tu_y = 0
            else:
                self.GRAVITY = 0.5
        elif self.check_Loc != True:
            if self.Loc_y >= 500:
                self.Loc_y = self.Huong_y = self.Tu_y = 500
                self.GRAVITY = 0
                self.mon_return()
            elif self.Loc_y <= 0:
                self.Loc_y = self.Huong_y = self.Tu_y = 0
            else:
                self.GRAVITY = 0.5
        elif self.check_Huong != True:
            if self.Huong_y >= 500:
                self.Huong_y = self.Tu_y = 500
                self.GRAVITY = 0
                self.mon_return()
            elif self.Huong_y <= 0:
                self.Huong_y = self.Tu_y = 0
            else:
                self.GRAVITY = 0.5
        elif self.check_Tu != True:
            if self.Tu_y >= 500:
                self.Tu_y = 500
                self.GRAVITY = 0
                self.mon_return()
            elif self.Tu_y <= 0:
                self.Tu_y = 0
            else:
                self.GRAVITY = 0.5

    def mon_return(self):
        self.mon = self.screen.play_screen.blit(
            self.mon_image, (self.mon_x, self.mon_y))
        if self.mon_x <= -50:
            self.mon_x = 810

    def main_logic(self):
        if self.Phat_out == False:
            self.logic_colli(self.Phat, 1, self.Phat_x)
            self.logic_draw(self.Phat_x,1)
        elif self.Phat_out == True and self.Loc_out == False:
            self.logic_colli(self.Loc, 2, self.Loc_x)
            self.logic_draw(self.Loc_x,2)
            print("Phat out")
        elif self.Loc_out == True and self.Huong_out == False:
            self.logic_colli(self.Huong, 3, self.Huong_x)
            self.logic_draw(self.Huong_x,3)
            print("Loc out")
        elif self.Huong_out == True and self.Tu_out == False:
            self.logic_colli(self.Tu, 4, self.Tu_x)
            self.logic_draw(self.Tu_x,4)
            print("Huong out")
        elif self.Tu_out:
            print('SEKF',self.Tu_out)
            self.donut_count -= 1
            self.donut_count_now = str(self.donut_count)
            self.Tu_out=False
        self.block_out()
        self.cha_out_bool()
        self.logic_lose_condition()


    def logic_colli(self, Character, check, cha_x):
        self.donut = self.screen.play_screen.blit(
            self.donut_image, (self.donut_x, self.donut_y))
        if self.point % 500 == 0:
            self.donut_bool = False
        self.tree1 = self.screen.play_screen.blit(
            self.cay1_image, (self.cay1_x, self.setting.cay1_y))
        self.tree2 = self.screen.play_screen.blit(
            self.cay2_image, (self.cay2_x, self.setting.cay2_y))
        self.tree3 = self.screen.play_screen.blit(
            self.cay3_image, (self.cay3_x, self.setting.cay3_y))
        self.tree4 = self.screen.play_screen.blit(
            self.cay4_image, (self.cay4_x, self.setting.cay4_y))
        self.block1 = self.screen.play_screen.blit(
            self.block1_image, (self.b1_x, self.b1_y))
        self.block2 = self.screen.play_screen.blit(
            self.block2_image, (self.b2_x, self.b2_y))
        self.block3 = self.screen.play_screen.blit(
            self.block3_image, (self.b3_x, self.b3_y))
        self.Phat = self.screen.play_screen.blit(
            self.phat.image, (self.Phat_x, self.Phat_y))
        self.Loc = self.screen.play_screen.blit(
            self.loc.image, (self.Loc_x, self.Loc_y))
        self.Tu = self.screen.play_screen.blit(
            self.tu.image, (self.Tu_x, self.Tu_y))
        self.Huong = self.screen.play_screen.blit(
            self.huong.image, (self.Huong_x, self.Huong_y))
        self.mon = self.screen.play_screen.blit(
            self.mon_image, (self.mon_x, self.mon_y))
        if self.block1_check:
            print("conbocuoi")
            if Character.colliderect(self.block1):
                if self.block1_image==self.map.image1 or self.block1_image==self.map.image5:
                    self.setting.block1 = True
                elif check == 4 and (self.block1_image!=self.map.image1 or self.block1_image!=self.map.image5):
                    self.donut_count -= 1
                    self.donut_count_now = str(self.donut_count)
                    self.block1_out = True
                else:
                    self.check_character_lose(check)
                    self.block1_out = True
                    self.block1_check=False
        if self.block2_check:
            if Character.colliderect(self.block2):
                if self.block2_image==self.map.image1 or self.block2_image==self.map.image5:
                    self.setting.block2 = True
                elif check == 4 and (self.block2_image!=self.map.image1 or self.block2_image!=self.map.image5):
                    self.donut_count -= 1
                    self.donut_count_now = str(self.donut_count)
                    self.block2_out = True
                else:
                    self.check_character_lose(check)
                    self.block2_out = True
                    self.block2_check=False
        if self.block3_check:
            if Character.colliderect(self.block3):
                if self.block3_image==self.map.image1 or self.block3_image==self.map.image5:
                    self.setting.block3 = True
                elif check == 4 and (self.block3_image!=self.map.image1 or self.block3_image!=self.map.image5):
                    self.donut_count -= 1
                    self.donut_count_now = str(self.donut_count)
                    self.block3_out = True
                else:
                    self.check_character_lose(check)
                    self.block3_out = True
                    self.block3_check=False
        if Character.colliderect(self.donut):
            self.donut_count += 1
            self.donut_count_now = str(self.donut_count)
            self.donut_bool = True
        if self.donut_bool:
            self.donut_x = 810
            self.donut_y = rd.choice(
                (rd.randint(105, 150), rd.randint(255, 300)))
        for i in [self.tree1, self.tree2, self.tree3, self.tree4]:
            if Character.colliderect(i):
                self.check_tree_bool(i)
                self.speed = 3
                # am thanh cay dung
            else:
                self.speed = 4
        if Character.colliderect(self.mon):
            self.donut_count -= 1
            self.donut_count_now = str(self.donut_count)
            # time.sleep(0.5)
            if self.donut_count >= 0:
                self.mon_x = cha_x-50
    def logic_draw_law(self,check,y):
        if check==1:
            self.Phat_y = self.Loc_y = self.Huong_y = self.Tu_y = y-50
        elif check==2:
            self.Loc_y=self.Huong_y=self.Tu_y=y-50
        elif check ==3:
            self.Huong_y=self.Tu_y=y-50
        else:self.Tu_y=y-50
    def logic_draw(self, cha_x,check):
        if self.setting.block1 == True:
            if cha_x <= self.setting.block_length+self.b1_x:
                pygame.draw.rect(self.screen.play_screen, self.setting.Green,
                                 (self.b1_x, self.b1_y, round((self.setting.block_length*(1-((self.setting.block_length+self.b1_x)-cha_x)/self.setting.block_length)), -1), self.setting.block_width))

                self.map_run_plus(2)
                self.logic_draw_law(check,self.b1_y)
                self.GRAVITY = 0
                self.check_mouse=False
            else:
                pygame.draw.rect(self.screen.play_screen, self.setting.Green,
                                 (self.b1_x, self.b1_y, self.setting.block_length, self.setting.block_width))
                self.GRAVITY = 0.5
                self.check_mouse=True
        if self.b1_x <= -self.setting.block_length:
            self.setting.block1 = False

        if self.setting.block2 == True:
            if cha_x <= self.setting.block_length+self.b2_x:
                pygame.draw.rect(self.screen.play_screen, self.setting.Green,
                                 (self.b2_x, self.b2_y, round((self.setting.block_length*(1-((self.setting.block_length+self.b2_x)-cha_x)/self.setting.block_length)), -1), self.setting.block_width))
                self.map_run_plus(2)
                self.logic_draw_law(check,self.b2_y)
                self.GRAVITY = 0
                self.check_mouse=False
            else:
                pygame.draw.rect(self.screen.play_screen, self.setting.Green,
                                 (self.b2_x, self.b2_y, self.setting.block_length, self.setting.block_width))
                self.GRAVITY = 0.5
                self.check_mouse=True
        if self.b2_x <= -self.setting.block_length:
            self.setting.block2 = False
        if self.setting.block3 == True:
            if cha_x <= self.setting.block_length+self.b3_x:
                pygame.draw.rect(self.screen.play_screen, self.setting.Green,
                                 (self.b3_x, self.b3_y, round((self.setting.block_length*(1-((self.setting.block_length+self.b3_x)-cha_x)/self.setting.block_length)), -1), self.setting.block_width))
                self.map_run_plus(2)
                self.logic_draw_law(check,self.b3_y)
                self.GRAVITY = 0
                self.check_mouse=False
            else:
                pygame.draw.rect(self.screen.play_screen, self.setting.Green,
                                 (self.b3_x, self.b3_y, self.setting.block_length, self.setting.block_width))
                self.GRAVITY = 0.5
                self.check_mouse=True

        if self.b3_x <= -self.setting.block_length:
            self.setting.block3 = False

    def block_out(self):
        if self.block1_out == True:
            self.block1_image = self.map.block1_gay_image
        elif self.block2_out == True:
            self.block2_image = self.map.block2_gay_image
        elif self.block3_out == True:
            self.block3_image = self.map.block3_gay_image
    

    def logic_lose(self):
        self.speed = 0
        self.setting.char_drop_velocity = 0
        self.GRAVITY = 0
        self.pause = True
        self.count = False
        self.score_report=True
        self.sec=0

    def logic_lose_condition(self):
        if self.donut_count == 0:
            pass
        if self.donut_count < 0:
            self.logic_lose()
    
    def check_tree_bool(self, a):
        if a == self.tree1:
            self.check_tree1 = True
            if self.check_tree1:
                # self.cay1_x = 801
                self.cay1_image = self.map.caygay_image
                self.check_tree1 = False
        if a == self.tree2:
            self.check_tree2 = True
            if self.check_tree2:
                # self.cay2_x = 801
                self.cay2_image = self.map.caygay_image
                self.check_tree2 = False
        if a == self.tree3:
            self.check_tree3 = True
            if self.check_tree3:
                # self.cay3_x = 801
                self.cay3_image = self.map.caygay_image
                self.check_tree3 = False
        if a == self.tree4:
            self.check_tree4 = True
            if self.check_tree4:
                # self.cay4_x = 801
                self.cay4_image = self.map.caygay_image
                self.check_tree4 = False
    
    def check_character_lose(self, check):
        if check == 1:
            self.check_Phat = True
            print(self.check_Phat)
        elif check == 2:
            self.check_Loc = True
        elif check == 3:
            self.check_Huong = True
        elif check == 4:
            self.check_Tu = True

    def cha_out(self):
        if self.check_Phat == True:
            self.Phat_y += 15
            self.Phat_out = True
        if self.check_Loc == True:
            self.Loc_y += 15
            self.Loc_out = True
        if self.check_Huong == True:
            self.Huong_y += 15
            self.Huong_out = True
        if self.check_Tu == True:
            self.Tu_out = True

    def cha_out_bool(self):
        self.cha_out()
        if self.Phat_y >= 700:
            self.Phat_x = -600
        if self.Loc_y >= 700:
            self.Loc_x = -600
        if self.Huong_y >= 700:
            self.Huong_x = -600
    
    def logic_reset(self):
        if self.pause:
            self.Phat_x = 200
            self.Loc_x = 150
            self.Huong_x = 100
            self.Tu_x = 50
            self.Phat_y = self.Loc_y = self.Huong_y = self.Tu_y = 300
            self.b1_x = 1325
            self.b2_x = 1800
            self.b3_x = 1625
            self.mon_x = 810
            self.cay1_x, self.cay2_x, self.cay3_x, self.cay4_x = (
                1100, 1310, 1520, 1730)
            self.speed = 4
            self.point = 0
            self.total_secs = 0
            self.mins = 0
            self.secs = 0
            self.count = True
            self.block1_out=False
            self.block2_out=False
            self.block3_out=False
            self.block1_check=True
            self.block2_check=True
            self.block3_check=True
            self.time_now = str(self.mins) + " : " + str(self.secs)
            self.point_now = str(self.point)
            self.GRAVITY = 0.5
            self.check_Huong = self.check_Loc = self.check_Phat = False
            self.check_tree1=False
            self.check_tree2=False
            self.check_tree3=False
            self.check_tree4=False
            self.Phat_out = False
            self.Loc_out = False
            self.Huong_out = False
            self.Tu_out = False
            self.donut_count = 0
            self.donut_count_now = str(self.donut_count)
            self.pause = False
            self.check_mouse=True
            self.sec=1
            self.score_report=0
    def update(self):
        self.setting.char_drop_velocity = 0
        self.setting.char_drop_velocity -= 10

    def action(self):
        self.setting.char_drop_velocity += self.GRAVITY
        self.Phat_y += self.setting.char_drop_velocity
        self.Loc_y += self.setting.char_drop_velocity*0.95
        self.Huong_y += self.setting.char_drop_velocity*0.9
        self.Tu_y += self.setting.char_drop_velocity*0.85

    def map_run(self):
        self.b1_x -= self.speed
        self.b2_x -= self.speed
        self.b3_x -= self.speed
        self.cay1_x -= self.speed
        self.cay2_x -= self.speed
        self.cay3_x -= self.speed
        self.cay4_x -= self.speed
        self.donut_x -= self.speed
        self.mon_x -= self.speed*2

    def map_run_plus(self, speed):
        self.b1_x -= speed
        self.b2_x -= speed
        self.b3_x -= speed
        self.cay1_x -= speed
        self.cay2_x -= speed
        self.cay3_x -= speed
        self.cay4_x -= speed
        self.donut_x -= speed

    def map_return(self):
        if self.b1_x <= -self.setting.block_length:
            if self.block1_image==self.map.image1 or self.block1_image==self.map.image5:
                self.setting.block1 = False
            self.b1_x = 810
            self.block1_image =rd.choice(
                [self.map.image1, self.map.image2, self.map.image3, self.map.image4, self.map.image5])
            self.block1_out=False
            self.block1_check=True
            # self.block1_image = rd.choice(
            #     [self.map.image1, self.map.image2, self.map.image3, self.map.image4, self.map.image5])
        if self.b2_x <= -self.setting.block_length:
            if self.block2_image==self.map.image1 or self.block1_image==self.map.image5:
                self.setting.block2 = False
            self.b2_x = 810
            self.block2_image = rd.choice(
                [self.map.image1, self.map.image2, self.map.image3, self.map.image4, self.map.image5])
            self.block2_out=False
            self.block2_check=True

        if self.b3_x <= -self.setting.block_length:
            if self.block3_image==self.map.image1 or self.block3_image==self.map.image5:
                self.setting.block3 = False
            self.b3_x = 810
            self.block3_image = rd.choice(
                [self.map.image1, self.map.image2, self.map.image3, self.map.image4, self.map.image5])
            self.block3_out=False
            self.block3_check=True

        if self.cay1_x <= -50:
            self.cay1_x = 803
            self.cay1_image = self.map.cay_image
        if self.cay2_x <= -50:
            self.cay2_x = 803
            self.cay2_image = self.map.cay_image
        if self.cay3_x <= -50:
            self.cay3_x = 803
            self.cay3_image = self.map.cay_image
        if self.cay4_x <= -50:
            self.cay4_x = 803
            self.cay4_image = self.map.cay_image
        if self.donut_x <= -50:
            self.donut_bool = True

    def logic_variable_definition(self):
        self.mon_image = self.map.image_mon1ngc
        self.cot1_x = self.setting.cot1_x
        self.cot1_y = self.setting.cot1_y
        self.cot2_x = self.setting.cot2_x
        self.cot2_y = self.setting.cot2_y
        self.sen1x = self.setting.sen1_x
        self.sen1y = self.setting.sen1_y
        self.sen2x = self.setting.sen2_x
        self.sen2y = self.setting.sen2_y
        self.mon_x = self.setting.mon_x
        self.mon_y = self.setting.mon_y
        self.fly_x = self.setting.fly_x
        self.fly_y = self.setting.fly_y
        self.bird_x = self.setting.bird_x
        self.bird_y = self.setting.bird_y
        self.block1_out = None
        self.block2_out = None
        self.block3_out = None
        self.Phat_out = False
        self.Loc_out = False
        self.Huong_out = False
        self.Tu_out = False
        self.check_Phat = None
        self.check_Loc = None
        self.check_Huong = None
        self.check_Tu = None
        self.pause = None
        self.check_tree1 = None
        self.check_tree2 = None
        self.check_tree3 = None
        self.check_tree4 = None
        self.donut_bool = False
        self.count = True
        self.Phat_x = self.phat.x
        self.Phat_y = self.phat.y
        self.Loc_x = self.loc.x
        self.Loc_y = self.loc.y
        self.Huong_x = self.huong.x
        self.Huong_y = self.huong.y
        self.Tu_x = self.tu.x
        self.Tu_y = self.tu.y
        self.GRAVITY = self.setting.GRAVITY
        self.speed = 4
        self.cay1_x = self.setting.cay1_x
        self.cay2_x = self.setting.cay2_x
        self.cay3_x = self.setting.cay3_x
        self.cay4_x = self.setting.cay4_x
        self.donut_x, self.donut_y = (810, rd.choice(
            (rd.randint(105, 150), rd.randint(255, 300))))
        self.b1_x = self.setting.block1_x
        self.b2_x = self.setting.block2_x
        self.b3_x = self.setting.block3_x
        self.b1_y = self.setting.block1_y
        self.b2_y = self.setting.block2_y
        self.b3_y = self.setting.block3_y
        self.cay1_x = self.setting.cay1_x
        self.cay2_x = self.setting.cay2_x
        self.cay3_x = self.setting.cay3_x
        self.cay4_x = self.setting.cay4_x
        self.point = self.setting.point
        self.mins = self.setting.mins
        self.secs = self.setting.secs
        self.donut_count = 0
        self.donut_count_now = str(self.donut_count)
        self.donut_count_now = str(self.donut_count)
        self.block1_image = self.map.block1_image
        self.block2_image = self.map.block2_image
        self.block3_image = self.map.block3_image
        self.random_image1=rd.choice(
                [self.map.image1, self.map.image2, self.map.image3, self.map.image4, self.map.image5])
        self.random_image2=rd.choice(
                [self.map.image1, self.map.image2, self.map.image3, self.map.image4, self.map.image5])
        self.random_image3=rd.choice(
                [self.map.image1, self.map.image2, self.map.image3, self.map.image4, self.map.image5])
        self.cay1_image = self.map.cay_image
        self.cay2_image = self.map.cay_image
        self.cay3_image = self.map.cay_image
        self.cay4_image = self.map.cay_image
        self.donut_image = self.map.donut_image
        self.Phat = self.screen.play_screen.blit(
            self.phat.image, (self.phat.x, self.phat.y))
        self.Loc = self.screen.play_screen.blit(
            self.loc.image, (self.loc.x, self.loc.y))
        self.Tu = self.screen.play_screen.blit(
            self.tu.image, (self.tu.x, self.tu.y))
        self.Huong = self.screen.play_screen.blit(
            self.huong.image, (self.huong.x, self.huong.y))
        self.block1 = self.screen.play_screen.blit(
            self.block1_image, (self.setting.block1_x, self.setting.block1_y))
        self.block2 = self.screen.play_screen.blit(
            self.block2_image, (self.setting.block2_x, self.setting.block2_y))
        self.block3 = self.screen.play_screen.blit(
            self.block3_image, (self.setting.block3_x, self.setting.block3_y))
        self.donut = self.screen.play_screen.blit(
            self.donut_image, (self.donut_x, self.donut_y))
        self.tree1 = self.screen.play_screen.blit(
            self.cay1_image, (self.cay1_x, self.setting.cay1_y))
        self.tree2 = self.screen.play_screen.blit(
            self.cay2_image, (self.cay2_x, self.setting.cay2_y))
        self.tree3 = self.screen.play_screen.blit(
            self.cay3_image, (self.cay3_x, self.setting.cay3_y))
        self.tree4 = self.screen.play_screen.blit(
            self.cay4_image, (self.cay4_x, self.setting.cay4_y))
        self.diahinh1 = self.screen.play_screen.blit(
            self.map.image_ground, (self.cot1_x, self.cot1_y))
        self.diahinh2 = self.screen.play_screen.blit(
            self.map.image_ground, (self.cot2_x, self.cot2_y))
        self.time_now = str(self.mins) + " : " + str(self.secs)
        self.point_now = str(self.point)
        self.clock = None
        self.total_secs = self.setting.total_secs
        self.score_report=None
        self.sec=1
        self.donut_check=False
        self.block1_check=True
        self.block2_check=True
        self.block3_check=True
        self.check_mouse=True
