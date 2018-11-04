from pico2d import *
import mygame
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
        mygame.dyna_update(self)
    def get_bb(self):
        return 0,0,0,0

class SilverCoin:
    def __init__(self):
        self.frame = 0
        self.coin_image = load_image("image\\silvercoin_item_.png")
        self.x = 600
        self.y = 250
        self.velocity = mygame.GRASS_SPEED_PPS
    def draw(self):
        self.coin_image.clip_draw(self.frame * 48,0,48,48,self.x,self.y)

    def update(self):
        self.frame = (self.frame + 1) % 4
        mygame.dyna_update(self)
    def get_bb(self):
        return self.x - 24, self.y -24 , self.x + 24, self.y + 24