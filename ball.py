from pico2d import *
import mygame
class Ball:

    def __init__(self):
        self.frame = 0
        self.images = [load_image("image\\attack_fly_ball_.png"),load_image("image\\attack_last_ball_.png")]
        self.active = False
        self.end = False
    def enter(self):
        self.frame = 0
        self.active = True
        self.end = False
    def draw(self):
        if self.active :
            self.images[0].clip_draw(int(self.frame) * 123,0,123,32,self.x,self.y)
        if self.end :
            self.images[1].clip_draw(int(self.frame) * 134,0,134,134,self.x,self.y)
    def update(self):
        if self.active :
            self.frame = (self.frame + 2 * mygame.ACTION_PER_TIME * mygame.frame_time) % 2
        if self.end :
            self.active == False
            self.frame = (self.frame + 4 * mygame.ACTION_PER_TIME * mygame.frame_time) % 4
            if self.frame == 4 : self.end = False
    def get_bb(self):
        if self.active:
            return 0,0,0,0
            #return self.x - 24, self.y - 24, self.x + 24, self.y + 24
        else :
            return 0,0,0,0
        pass

