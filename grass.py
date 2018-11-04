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
    def update(self):
        mygame.dyna_update(self)
        if self.x < -431:
            self.x = 370 + 862


