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
        if Character.colliderect(self.block1):
            for a in self.map.happi_image:
                if self.block1_image ==a:
                    self.setting.block1 = True
                    break
                # else:continue
                if a ==self.map.image_11:
                    # if check == 4 and self.block1_image!=a:
                    #     self.donut_count -= 1
                    #     self.donut_count_now = str(self.donut_count)
                    # else:
                        self.check_character_lose(check)
                        self.block1_out = True
        if Character.colliderect(self.block2):
            for b in self.map.happi_image:
                if self.block1_image ==b:
                    self.setting.block2 = True
                    break
                # else:continue
                if b ==self.map.image_11:
                    # if check == 4 and self.block2_image!=b:
                    #     self.donut_count -= 1
                    #     self.donut_count_now = str(self.donut_count)
                        self.check_character_lose(check)
                        self.block2_out = True
        if Character.colliderect(self.block3):
            for c in self.map.happi_image:
                if self.block3_image ==c:
                    self.setting.block3 = True
                    break
                # else:continue
                if c ==self.map.image_11:
                    # if check == 4 and self.block3_image!=a:
                    #     self.donut_count -= 1
                    #     self.donut_count_now = str(self.donut_count)
                        self.check_character_lose(check)
                        self.block3_out = True
        elif Character.colliderect(self.donut):
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