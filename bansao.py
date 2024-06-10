# import pygame
# import random as rd
# from setting import Setting
# from phat import Phat
# from loc import Loc
# from huong import Huong
# from tu import Tu
# from screen import Screen
# from map import Map
# from logic import Logic


# class UII:
#     def __init__(self):
#         pygame.init()
#         self.logic = Logic()
#         self.setting = Setting()
#         self.screen = Screen()
#         self.map = Map()
#         self.phat = Phat("phat.png")
#         self.loc = Loc("Loc.png")
#         self.huong = Huong("Huong.png")
#         self.tu = Tu("Tu.png")
#         self.Phat_x = self.phat.x
#         self.Phat_y = self.phat.y
#         self.Loc_x = self.loc.x
#         self.Loc_y = self.loc.y
#         self.Huong_x = self.huong.x
#         self.Huong_y = self.huong.y
#         self.Tu_x = self.tu.x
#         self.Tu_y = self.tu.y
#         self.block1_image = self.map.block1_image
#         self.Phat = self.screen.play_screen.blit(
#             self.phat.image, (self.phat.x, self.phat.y))
#         self.Loc = self.screen.play_screen.blit(
#             self.loc.image, (self.loc.x, self.loc.y))
#         self.Tu = self.screen.play_screen.blit(
#             self.tu.image, (self.tu.x, self.tu.y))
#         self.Huong = self.screen.play_screen.blit(
#             self.huong.image, (self.huong.x, self.huong.y))
#         self.block1 = self.screen.play_screen.blit(
#             self.map.block1_image, (self.map.block1_x, self.setting.block1_y))
#         self.block2 = self.screen.play_screen.blit(
#             self.map.block2_image, (self.map.block2_x, self.setting.block2_y))
#         self.block3 = self.screen.play_screen.blit(
#             self.map.block3_image, (self.map.block3_x, self.setting.block3_y))
#         pygame.display.set_caption("UII")

#     def run_game(self):
#         while self.setting.running:
#             self.setting.clock_set.tick(60)
#             self.check_events()
#             self.screen.draw_screen(self.screen.screen)
#             self.screen.draw()
#             if self.setting.Start:
#                 self.screen.draw_play_screen(self.screen.play_screen)
#                 self.setting.clock_setting()
#                 self.screen.draw_font(self.screen.play_screen, self.setting.time_now,
#                                       self.setting.time_location, self.setting.Black)
#                 self.screen.draw_font(self.screen.play_screen, self.setting.point_now,
#                                       self.setting.point_location, self.setting.Black)
#                 self.logic.map_run(self.setting.speed)
#                 self.cay1 = self.screen.draw_tree(
#                     self.logic.cay1_x, self.setting.cay1_y)
#                 self.cay2 = self.screen.draw_tree(
#                     self.logic.cay2_x, self.setting.cay2_y)
#                 self.cay3 = self.screen.draw_tree(
#                     self.logic.cay3_x, self.setting.cay3_y)
#                 self.cay4 = self.screen.draw_tree(
#                     self.logic.cay4_x, self.setting.cay4_y)
#                 # self.cay1 = self.screen.draw_tree(
#                 #     self.map.cay1_x, self.setting.cay1_y)
#                 # self.cay2 = self.screen.draw_tree(
#                 #     self.map.cay2_x, self.setting.cay2_y)
#                 # self.cay3 = self.screen.draw_tree(
#                 #     self.map.cay3_x, self.setting.cay3_y)
#                 # self.cay4 = self.screen.draw_tree(
#                 #     self.map.cay4_x, self.setting.cay4_y)
#                 # self.block1 = self.screen.play_screen.blit(
#                 #     self.map.block1_image, (self.logic.b1_x, self.setting.block1_y))
#                 # self.block2 = self.screen.play_screen.blit(
#                 #     self.map.block2_image, (self.logic.b2_x, self.setting.block2_y))
#                 # self.block3 = self.screen.play_screen.blit(
#                 #     self.map.block3_image, (self.logic.b3_x, self.setting.block3_y))

#                 # self.screen.draw_map(self.map.block1_image,
#                 #                      self.map.block1_x, self.setting.block1_y)
#                 # self.screen.draw_map(self.map.block2_image,
#                 #                      self.map.block2_x, self.setting.block2_y)
#                 # self.screen.draw_map(self.map.block3_image,
#                 #                      self.map.block3_x, self.setting.block3_y)
#                 # self.Phat = self.screen.play_screen.blit(
#                 #     self.phat.image, (self.phat.x, self.phat.y))
#                 # self.Loc = self.screen.play_screen.blit(
#                 #     self.loc.image, (self.loc.x, self.loc.y))
#                 # self.Tu = self.screen.play_screen.blit(
#                 #     self.tu.image, (self.tu.x, self.tu.y))
#                 # self.Huong = self.screen.play_screen.blit(
#                 #     self.huong.image, (self.huong.x, self.huong.y))
#                 self.logic.logic_colli(self.logic.Phat)
#                 # self.logic_colli(self.Phat)
#                 # self.logic_draw(self.Phat_x)
#                 self.logic.logic_draw(self.Phat_x)
#                 self.logic.action()
#                 # self.phat.action()
#                 # self.loc.action()
#                 # self.huong.action()
#                 # self.tu.action()
#                 # self.logic.logic_draw(self.Phat_x, self.map.block2_x,
#                 #                 self.setting.block2_y, self.setting.block2)
#                 # self.logic.logic_draw(self.Phat_x, self.map.block3_x,
#                 #                 self.setting.block3_y, self.setting.block3)
#             self.logic.map_return()
#             pygame.display.flip()
#         pygame.quit()

#     def check_events(self):
#         mouse_x, mouse_y = pygame.mouse.get_pos()
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 self.setting.running = False
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if event.button == 1:
#                     print(2)
#                     print(self.setting.cay1_x,
#                           self.setting.cay2_x, self.setting.speed)
#                     if (self.setting.start_location[0] <= mouse_x <= self.setting.start_location[0]+87) and (self.setting.start_location[1] <= mouse_y <= self.setting.start_location[1]+59):
#                         self.setting.Start = True
#                         self.setting.clock = True

#                     # self.screen.start()
#                     # print(Dinh_Loc.cha1())
#             if event.type == pygame.KEYDOWN:
#                 if event.key == pygame.K_SPACE:
#                     print(3)
#                     # self.jump = True
#                     # else:
#                     #     self.setting.jump = False
#                     if self.setting.pausing:
#                         #     #     Phat_y = Loc_y = Huong_y = Tu_y = 300
#                         #     #     speed = 3
#                         self.setting.score = 0
#                         self.setting.pausing = False
#                     self.logic.update()
#                     # self.phat.update()
#                     # self.loc.update()
#                     # self.huong.update()
#                     # self.tu.update()

#     def logic_colli(self, Character):
#         self.block1 = self.screen.play_screen.blit(
#             self.map.block1_image, (self.map.block1_x, self.setting.block1_y))
#         self.block2 = self.screen.play_screen.blit(
#             self.map.block2_image, (self.map.block2_x, self.setting.block2_y))
#         self.block3 = self.screen.play_screen.blit(
#             self.map.block3_image, (self.map.block3_x, self.setting.block3_y))
#         self.Phat = self.screen.play_screen.blit(
#             self.phat.image, (self.phat.x, self.phat.y))
#         self.Loc = self.screen.play_screen.blit(
#             self.loc.image, (self.loc.x, self.loc.y))
#         self.Tu = self.screen.play_screen.blit(
#             self.tu.image, (self.tu.x, self.tu.y))
#         self.Huong = self.screen.play_screen.blit(
#             self.huong.image, (self.huong.x, self.huong.y))
#         if Character.colliderect(self.block1):
#             if self.map.block1_image == self.map.image1:
#                 self.setting.block1 = True
#             else:
#                 pass
#         if Character.colliderect(self.block2):
#             if self.map.block2_image == self.map.image1:
#                 self.setting.block2 = True
#             else:
#                 pass
#         if Character.colliderect(self.block3):
#             if self.map.block3_image == self.map.image1:
#                 self.setting.block3 = True
#             else:
#                 pass

#     def logic_draw(self, cha_x):
#         if self.setting.block1 == True:
#             if cha_x <= self.setting.block_length+self.map.block1_x:
#                 # print("ok2")
#                 pygame.draw.rect(self.screen.play_screen, self.setting.Green,
#                                  (self.map.block1_x, self.setting.block1_y, round((self.setting.block_length*(1-((self.setting.block_length+self.map.block1_x)-cha_x)/self.setting.block_length)), -1), 50))
#                 # self.map.map_run(2)
#                 self.phat.y = self.loc.y = self.huong.y = self.tu.y = self.setting.block1_y
#             else:
#                 pygame.draw.rect(self.screen.play_screen, self.setting.Green,
#                                  (self.map.block1_x, self.setting.block1_y, 400, 50))
#                 # print("ok1")
#         if self.map.block1_x <= -self.setting.block_length:
#             self.setting.block1 = False

#         if self.setting.block2 == True:
#             if cha_x <= self.setting.block_length+self.map.block2_x:
#                 # print("ok2")
#                 pygame.draw.rect(self.screen.play_screen, self.setting.Green,
#                                  (self.map.block2_x, self.setting.block2_y, round((self.setting.block_length*(1-((self.setting.block_length+self.map.block2_x)-cha_x)/self.setting.block_length)), -1), 50))
#                 # self.map.map_run(2)
#                 self.phat.y = self.loc.y = self.huong.y = self.tu.y = self.setting.block2_y
#             else:
#                 pygame.draw.rect(self.screen.play_screen, self.setting.Green,
#                                  (self.map.block2_x, self.setting.block2_y, 400, 50))
#                 # print("ok1")
#         if self.map.block2_x <= -self.setting.block_length:
#             self.setting.block2 = False

#         if self.setting.block3 == True:
#             if cha_x <= self.setting.block_length+self.map.block3_x:
#                 # print("ok2")
#                 pygame.draw.rect(self.screen.play_screen, self.setting.Green,
#                                  (self.map.block3_x, self.setting.block3_y, round((self.setting.block_length*(1-((self.setting.block_length+self.map.block3_x)-cha_x)/self.setting.block_length)), -1), 50))
#                 # self.map.map_run(2)
#                 self.phat.y = self.loc.y = self.huong.y = self.tu.y = self.setting.block3_y
#             else:
#                 pygame.draw.rect(self.screen.play_screen, self.setting.Green,
#                                  (self.map.block3_x, self.setting.block3_y, 400, 50))
#                 # print("ok1")
#         if self.map.block3_x <= -self.setting.block_length:
#             self.setting.block3 = False


# if __name__ == '__main__':
#     ai = UII()
#     ai.run_game()
