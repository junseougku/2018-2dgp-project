from pico2d import *
import mygame
import random
import time
class Medicine:
    def __init__(self):
        self.frame = 0
        self.medicine_image = load_image("image\\hp_item_.png")
        self.x = 900
        self.y = 250
        self.velocity = mygame.GRASS_SPEED_PPS
        self.active = True
        self.random_time = 0.0
        self.currenttime = get_time()
    def enter(self):
        self.y = random.randint(1, 4) * 100
        self.x = 900
        self.active = True
        self.currenttime = get_time()
    def draw(self):
        if self.active:
            self.medicine_image.clip_draw(int(self.frame) * 85, 0, 85, 87, self.x, self.y)
    def update(self):
        if mygame.delay_check:
            print(self.active)
            if self.active and self.x < -250:
                self.exit()
                self.active = False
            elif self.active :

                self.frame = (self.frame + 4 * mygame.ACTION_PER_TIME * mygame.frame_time) % 4
                mygame.move_update(self)
            elif self.active == False and get_time() - self.currenttime > self.random_time:
                self.enter()

    def get_bb(self):
        if self.active:
            return self.x - 42.5, self.y -43.5 , self.x + 42.5, self.y + 43.5
        else : return 0,0,0,0
    def change_active(self):
        if self.active :
            self.active = False
        else :
            self.active = True

    def exit(self):
        self.random_time = random.randint(5, 11)
        self.currenttime = get_time()




coin_list = [load_image("image\\silvercoin_item_.png"),load_image("image\\goldcoin_item_.png")]
class Coin:
    def __init__(self):
        self.frame = 0
        self.type = random.randint(0,1)
        self.coin_image = coin_list[self.type]
        self.x = 900
        self.y = 450
        self.velocity = mygame.GRASS_SPEED_PPS
        self.active = False

    def enter(self):
        self.y = random.randint(2,5) * 100
        self.x = 900
    def draw(self):
        if self.active :
            if self.type == 0:
                self.coin_image.clip_draw(int(self.frame) * 48,0,48,48,self.x,self.y)
            elif self.type == 1:
                self.coin_image.clip_draw(int(self.frame) * 58,0,58,59,self.x,self.y)

    def update(self):
        if self.active:
            mygame.move_update(self)
            if self.type == 0:
                self.frame = (self.frame + 4 * mygame.ACTION_PER_TIME * mygame.frame_time) % 4
            elif self.type == 1:
                self.frame = (self.frame + 6 * mygame.ACTION_PER_TIME * mygame.frame_time) % 6
            if self.x < -100:
                self.active = False

    def get_bb(self):
        if self.active:
            if self.type == 0:
                return self.x - 24, self.y -24 , self.x + 24, self.y + 24
            elif self.type == 1:
                return self.x - 29, self.y -29.5, self.x + 29 ,self.y + 29.5
        else :
            return 0,0,0,0
    def get_score(self):
        if self.type == 0:
            return 5
        elif self.type == 1:
            return 10
    def change_active(self):
        if self.active :
            self.active = False
        else :
            self.active = True