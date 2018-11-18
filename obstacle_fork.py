from pico2d import *
import mygame
import obstacle
class Obstacle_Fork:
    def __init__(self):
        self.image = load_image("image\\obstacle_3.png")
        self.x = 900
        self.y = 360
        self.velocity = mygame.GRASS_SPEED_PPS
        self.active = False
    def enter(self):
        pass
    def draw(self):
        self.image.draw(self.x,self.y)
    def update(self):
        mygame.move_update(self)
    def enter(self):
        self.x = 900
    def set_active(self,_active):
        self.active = _active
    def exit(self):
        pass
    def get_bb(self):
        return self.x - 33,self.y - 241 , self.x + 33 , self.y + 241