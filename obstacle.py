from pico2d import *
import mygame

class Obstacle:
    def __init__(self):
        self.frame = 0
        self.obstacle_image = load_image("image\\obstacle_1.png")
        self.x = 900
        self.y = 100
        self.velocity = mygame.GRASS_SPEED_PPS

    def draw(self):
        self.obstacle_image.draw(self.x,self.y)

    def update(self):
        mygame.move_update(self)
        if self.x < -100:
            self.x = 850
    def get_bb(self):
        return self.x - 31, self.y - 50, self.x + 31, self.y + 50