from pico2d import*
import mygame
class Enemy:
    def __init__(self):
        self.x = 200
        self.y = 200
        self.frame = 0
        self.image = load_image("image\\enemy_.png")
        self.velocity = mygame.GRASS_SPEED_PPS
    def draw(self):
        self.image.clip_draw(self.frame * 124, 0, 124, 73, self.x, self.y)
    def update(self):
        self.frame = (self.frame + 1) % 3