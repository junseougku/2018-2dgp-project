from pico2d import *

class HP:
    def __init__(self):
        self.x = 150
        self.y = 350
        self.image = load_image("image\\bar_hp.png")
    def draw(self):
        self.image.draw(self.x,self.y)
    def update(self):
        pass