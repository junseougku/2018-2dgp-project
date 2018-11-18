from pico2d import *
import mygame
import obstacle
import random
class Obstacle_Fork(obstacle.Obstacle):
    def __init__(self):
        self.image = load_image("image\\obstacle_3.png")
        self.x = 900
        self.y = 360
        self.velocity = mygame.GRASS_SPEED_PPS
    def enter(self):
        pass
    def draw(self):
        self.image.draw(self.x,self.y)
    def update(self):
        mygame.move_update(self)
        if self.x < -100:
            self.x = 900
    def exit(self):
        pass
    def get_bb(self):
        return self.x - 43,self.y - 241 , self.x + 43 , self.y + 241