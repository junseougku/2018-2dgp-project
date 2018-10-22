
from pico2d import *
gravity = 0.0
import math
class Player:
    def __init__(self):
        self.x = 150
        self.y = 100
        self.image = load_image("image\\work_player_.png")
        self.frame = 0

        self.jumpspeed = 0.0
        self
    def draw(self):
        self.image.clip_draw(self.frame * 129, 0, 129, 146, self.x, self.y)
       # self.image.clip_draw(self.frame * 160, 0, 160, 152, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 3
    def jump(self):
        global gravity


