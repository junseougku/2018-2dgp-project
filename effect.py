from pico2d import *
import mygame
class Effect:
    def __init__(self):
        self.image = load_image("image\\eat_effect_.png")
        self.frame = 0
        self.x = 0
        self.y = 0
        self.active = False
        self.velocity = mygame.GRASS_SPEED_PPS
    def enter(self,_x,_y):
        self.x = _x
        self.y = _y
        self.active = True
    def draw(self):
        if self.active :
            self.image.clip_draw(int(self.frame) * 181,0,181,165,self.x,self.y)
    def update(self):
        if self.active :
            mygame.move_update(self)
            self.frame = (self.frame + 6 * mygame.ACTION_PER_TIME * mygame.frame_time) % 6
            if self.frame == 5:
                self.active = False
    def exit(self):
        pass