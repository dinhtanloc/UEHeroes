import pygame
from setting import Setting
from phat import Phat
from loc import Loc
from huong import Huong
from tu import Tu
from screen import Screen
from map import Map
from logic import Logic


class UII:
    def __init__(self):
        pygame.init()
        self.logic = Logic()
        self.setting = Setting()
        self.screen = Screen()
        self.map = Map()
        self.phat = Phat("phat.png")
        self.loc = Loc("loc.png")
        self.huong = Huong("Huong.png")
        self.tu = Tu("Tu.png")
        pygame.display.set_caption("UII")
        pygame.mixer.music.load('nhacnen.mp3')
    def run_game(self):
        while self.setting.running:
            self.setting.clock_set.tick(60)
            self.check_events()
            self.screen.draw_screen(self.screen.screen)
            self.screen.draw()
            if self.setting.Start:
                self.screen.draw_play_screen(self.screen.play_screen)
                self.logic.clock_setting()
                if self.logic.count:
                    self.screen.draw_font(self.screen.play_screen, self.logic.time_now,
                                          self.setting.time_location, self.setting.Black)
                    self.screen.draw_font(self.screen.play_screen, self.logic.point_now,
                                          self.setting.point_location, self.setting.Black)
                    self.screen.draw_font(
                        self.screen.play_screen, self.logic.donut_count_now, (self.setting.donnut_x, self.setting.donnut_y), self.setting.Black)
                self.logic.map_run()
                self.logic.map_law()
                self.logic.main_logic()
                if self.logic.score_report:
                    self.screen.draw_score_report(self.screen.play_screen,self.logic.time_now,self.logic.point_now,(self.setting.report_timex,self.setting.report_timey),(self.setting.report_pointx,self.setting.report_pointy),self.setting.Black)
                self.logic.action()
            self.logic.map_return()
            pygame.display.flip()
        pygame.quit()
    def check_events(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.setting.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if self.logic.check_mouse:
                        self.logic.update()
                    if (self.setting.start_location[0] <= mouse_x <= self.setting.start_location[0]+87) and (self.setting.start_location[1] <= mouse_y <= self.setting.start_location[1]+59):
                        pygame.mixer.music.play(-1)
                        self.setting.Start = True
                        self.logic.clock = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.logic.logic_reset()
if __name__ == '__main__':
    ai = UII()
    ai.run_game()
