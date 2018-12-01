from pico2d import *
import mygame
import obstacle
class Obstacle_Dynamic:
    def __init__(self):
        self.image = load_image("image\\obstacle_dynamic_.png")
        self.x = 900
        self.y = 104.5
        self.velocity = mygame.GRASS_SPEED_PPS
        self.active = False
        self.frame = 0
        self.reverse = False
    def draw(self):
        self.image.clip_draw(int(self.frame) * 161,0,161,209,self.x,self.y)

    def update(self):
        if self.frame <= 5 and self.reverse == False:
            self.frame = (self.frame + 5 * mygame.ACTION_PER_TIME * mygame.frame_time) % 6
        else:
            self.frame = (self.frame - 5 * mygame.ACTION_PER_TIME * mygame.frame_time)
            self.reverse = True
        if self.frame <= 0 and self.reverse:
            self.reverse = False
        mygame.move_update(self)

    def enter(self):
        self.x = 900
        self.frame = 0
    def set_active(self,_active):
        self.active = _active
    def exit(self):
        self.frame = 0
    def get_bb(self):
        return self.x - 60.5,self.y - 64.5 , self.x + 60.5 , self.y + 44.5