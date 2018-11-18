from pico2d import *
import mygame
import obstacle
import random
class Obstacle_Pin:
    def __init__(self):
        self.type = random.randint(0,1)
        self.image = obstacle.obstacle_list[self.type]
        self.x = 900
        self.velocity = mygame.GRASS_SPEED_PPS
        if self.type == 0:
            self.y = 100 - 27
        elif self.type == 1:
            self.y = 100
        self.active = False
    def draw(self):
        self.image.draw(self.x,self.y)
    def set_active(self,_active):
        self.active = _active
    def enter(self):
        self.x = 900
        self.type = random.randint(0, 1)
        self.image = obstacle.obstacle_list[self.type]
        if self.type == 0:
            self.y = 100 - 27
        elif self.type == 1:
            self.y = 100
    def update(self):
        mygame.move_update(self)
    def get_bb(self):
        if self.type == 0:
            return self.x - 16, self.y - 50, self.x + 16, self.y + 45
        elif self.type == 1:
            return self.x - 28,self.y - 84 , self.x + 28 , self.y + 84