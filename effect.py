from pico2d import *

class Effect:
    def __init__(self):
        self.image = load_image("image\\eat_effect_.png")
        self.frame = 0
        self.x = 0
        self.y = 0
        self.active = False
    def enter(self,_x,_y):
        self.x = _x
        self.y = _y
        self.active = True
    def draw(self):
        if self.active :
            self.image.clip_draw(self.frame * 165,0,165,165,self.x,self.y)
    def update(self):
        if self.active :
            self.frame = (self.frame + 1) % 6
            if self.frame == 5:
                self.active = False
    def exit(self):
        pass