from pico2d import *

import mygame


class Grass:
    def __init__(self,_x):
        self.x = _x
        self.y = 30
        self.velocity = mygame.GRASS_SPEED_PPS
        self.grass_image = load_image("image\\grass_01.png")
    def draw(self):
        self.grass_image.draw(self.x,self.y)
    def enter(self):
        pass
    def update(self):
        mygame.move_update(self)
        if self.x < -431:
            self.x = 800+431
    def get_bb(self):
        return 0,0,0,0

