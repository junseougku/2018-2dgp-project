from pico2d import *

import mygame
PIXEL_PER_METER = (10.0/ 0.3)
GRASS_SPEED = 20.0
GRASS_SPEED_MPM = (GRASS_SPEED * 1000.0 / 60.0)
GRASS_SPEED_MPS = (GRASS_SPEED_MPM / 60.0)
GRASS_SPEED_PPS = (GRASS_SPEED_MPS * PIXEL_PER_METER)


class Grass:
    def __init__(self,_x):
        self.x = _x
        self.y = 30
        self.velocity = GRASS_SPEED_PPS
        self.grass_image = load_image("image\\grass_01.png")
    def draw(self):
        self.grass_image.draw(self.x,self.y)
    def update(self):
        mygame.dyna_update(self)
        if self.x < -431:
            self.x = 370 + 862


