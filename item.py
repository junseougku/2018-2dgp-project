from pico2d import *

class Medicine:
    def __init__(self):
        self.frame = 0
        self.medicine_image = load_image("image\\hp_item_.png")
        self.x = 250
        self.y = 250
    def draw(self):
        self.medicine_image.clip_draw(self.frame * 85, 0, 85, 87, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 4