
from pico2d import *
gravity = 0.0
import math

current_time = get_time()

class Player:
    def __init__(self):
        self.x = 150
        self.y = 100
        self.image = load_image("image\\work_player_.png")
        self.frame = 0

        self.jumpspeed = 0.0
    def draw(self):
        self.image.clip_draw(self.frame * 129, 0, 129, 146, self.x, self.y)
       # self.image.clip_draw(self.frame * 160, 0, 160, 152, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 3
    def draw_curve(self,curxx,heix,dotx,cury,heiy,doty):
        for i in range(0,100,2):
            t = i / 100
            x = (2*t**2-3*t+1) * curxx + (-4 * t ** 2 + 4 * t) * heix+(2*t**2-t)*doty
            y = (2*t **2-3*t+1) * cury +(-4 * t ** 2 + 4 * t) * heiy+(2*t**2-t)*doty
            self.x = x
            self.y = y
    def jump(self):
        self.draw_curve(self.x, self.x + 35, self.x + 70, self.y, self.y + 100, self.y)

