from pico2d import *

class HP:
    def __init__(self):
        self.x = 50
        self.y = 550
        self.image = load_image("image\\hp.png")
        self.count = 3
    def draw(self):
        for i in range(self.count):
            self.image.draw(self.x + (i * 50),self.y)

    def update(self):
        pass

    def setCount(self,_change):
        self.count = self.count +_change
    def getCount(self):
        return self.count