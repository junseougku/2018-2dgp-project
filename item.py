from pico2d import *
import mygame
import random
class Medicine:
    def __init__(self):
        self.frame = 0
        self.medicine_image = load_image("image\\hp_item_.png")
        self.x = 550
        self.y = 250
        self.velocity = mygame.GRASS_SPEED_PPS
    def draw(self):
        self.medicine_image.clip_draw(self.frame * 85, 0, 85, 87, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 4
        mygame.move_update(self)
    def get_bb(self):
        return self.x - 42.5, self.y -43.5 , self.x + 42.5, self.y + 43.5

coin_list = [load_image("image\\silvercoin_item_.png"),load_image("image\\goldcoin_item_.png")]
class Coin:
    def __init__(self):
        self.frame = 0
        self.type = random.randint(0,1)
        self.coin_image = coin_list[self.type]
        self.x = 650
        self.y = 250
        self.velocity = mygame.GRASS_SPEED_PPS
    def draw(self):
        if self.type == 0:
            self.coin_image.clip_draw(self.frame * 48,0,48,48,self.x,self.y)
        elif self.type == 1:
            self.coin_image.clip_draw(self.frame * 58,0,58,59,self.x,self.y)

    def update(self):
        mygame.move_update(self)
        if self.type == 0:
            self.frame = (self.frame + 1) % 4
        elif self.type == 1:
            self.frame = (self.frame + 1) % 6
    def get_bb(self):
        if self.type == 0:
            return self.x - 24, self.y -24 , self.x + 24, self.y + 24
        elif self.type == 1:
            return self.x - 29, self.y -29.5, self.x + 29 ,self.y + 29.5
    def get_score(self):
        if self.type == 0:
            return 5
        elif self.type == 1:
            return 10