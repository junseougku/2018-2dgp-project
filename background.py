from pico2d import *
import mygame
class Background:
    def __init__(self,_x):
        self.background_image = load_image("image\\stage_background_2.png")
        self.x = _x
        self.y = 300
        self.velocity = mygame.GRASS_SPEED_PPS/2
    def draw(self):
        self.background_image.draw(self.x,self.y)
    def update(self):
        mygame.move_update(self)
        if self.x < -370:
            self.x = 1180
    def get_bb(self):
        return 0,0,0,0
