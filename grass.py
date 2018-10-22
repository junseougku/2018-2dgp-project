from pico2d import *



class Grass:
    def __init__(self):
        self.x1 =431
        self.y = 30
        self.x2 = 1293
        self.grass_image = load_image("image\\grass_01.png")
    def draw(self):
        self.grass_image.draw(self.x1 ,self.y)
        self.grass_image.draw( self.x2 ,self.y)
    def update(self):
        self.x1 -= 10;
        self.x2 -=10
        if self.x1 < -431:
            self.x1 = self.x2 + 862
        if self.x2 < -431:
            self.x2 = self.x1 + 862

