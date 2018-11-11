from pico2d import *

class score:
    def __init__(self):
        self.font = load_font('ENCR10B.TTF', 32)
        self.x = 500
        self.y = 500
        self.score = 0
    def draw(self):
        self.font.draw(self.x , self.y , 'score : %3.0f'% self.score, (255, 0, 255))

    def update(self,_point):
        self.score += _point