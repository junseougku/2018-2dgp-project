from pico2d import *

import mygame
PIXEL_PER_METER = (10.0/ 0.3)
GRASS_SPEED = 20.0
GRASS_SPEED_MPM = (GRASS_SPEED * 1000.0 / 60.0)
GRASS_SPEED_MPS = (GRASS_SPEED_MPM / 60.0)
GRASS_SPEED_PPS = (GRASS_SPEED_MPS * PIXEL_PER_METER)


class Grass:
    def __init__(self):
        self.x1 =431
        self.y = 30
        self.x2 = 1293
        self.velocity = GRASS_SPEED_PPS
        self.grass_image = load_image("image\\grass_01.png")
    def draw(self):
        self.grass_image.draw(self.x1 ,self.y)
        self.grass_image.draw( self.x2 ,self.y)
    def update(self):
        self.x1 -= self.velocity * mygame.frame_time;
        self.x2 -=self.velocity * mygame.frame_time;
        if self.x1 < -431:
            self.x1 = self.x2 + 862
        if self.x2 < -431:
            self.x2 = self.x1 + 862

