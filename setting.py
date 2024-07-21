import pygame


class Setting:
    def __init__(self):
        # caidat man hinh
        self.screen_width = 650
        self.screen_length = 800
        # self.screen = pygame.display.set_mode(
        #     (self.screen_length, self.screen_width))
        self.Red = (255, 0, 0)
        self.Blue = (0, 0, 255)
        self.Green = (0, 255, 0)
        self.Brown = (165, 42, 42)
        self.Yellow = (255, 234, 0)
        self.Gray = (128, 128, 128)
        self.Orange = (255, 165, 0)
        self.Black = (0, 0, 0)
        self.Co_text = (0, 0, 255)
        self.GRAVITY = 0.5
        self.speed = 4
        self.clock_set = pygame.time.Clock()
        self.running = True
        # self.jump = False
        self.char_drop_velocity = 0
        self.start_location = (360, 550)
        self.time_location = (700, 575)
        self.point_location = (700, 550)
        self.Start = None
        self.mouse_x, self.mouse_y = pygame.mouse.get_pos()
        self.pausing = None
        self.score = 0
        self.clock = None
        self.block1 = None
        self.block2 = None
        self.block3 = None
        self.point = 0
        self.total_secs = 0
        self.plus = 0
        self.mins = 0
        self.secs = 0
        self.time_now = str(self.mins) + " : " + str(self.secs)
        self.point_now = str(self.point)
        self.block1_x = 1325
        self.block2_x = 1800
        self.block3_x = 1625
        self.block1_y = 50
        self.block2_y = 200
        self.block3_y = 350
        self.block_length = 400
        self.block_width = 50
        self.cay1_x = 1100
        self.cay2_x = 1310
        self.cay3_x = 1520
        self.cay4_x = 1730
        self.cay1_y = self.cay2_y = self.cay3_y = self.cay4_y = 450
        self.block_out = None
        self.bird_x = 1100
        self.fly_x = 1310
        self.bird_y = 175
        self.fly_y = 225
        self.cot1_x = 1100
        self.cot1_y = 100
        self.cot2_x = 900
        self.cot2_y = 350
        self.sen1_x = self.cot1_x+self.block_length-50
        self.sen1_y = self.cot1_y-50
        self.sen2_x = self.cot2_x+self.block_length-50
        self.sen2_y = self.cot2_y-50

        self.mon_x = 1120
        self.mon_y = 450
        self.donnut_x=500
        self.donnut_y=575
        self.score_report_x=250
        self.score_report_y=200
        self.score_boldfont_x=self.time_boldfont_x=300
        self.score_boldfont_y=350
        self.time_boldfont_y=275
        self.report_timex=self.report_pointx=400
        self.report_timey=284
        self.report_pointy=359
        self.notice_x=285
        self.notice_y=420
