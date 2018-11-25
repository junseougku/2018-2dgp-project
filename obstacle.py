from pico2d import *

obstacle_list = [load_image("image\\obstacle_1.png"),load_image("image\\obstacle_2.png")]
import obstacle_fork
import obstacle_pin
import random
class Obstacle_line:
    def __init__(self):
        self.choice = 0
        #self.image = load_image("C:\\2DGP\\2018-2dgp-project\\image\\Attack.png")
        self.fork = obstacle_fork.Obstacle_Fork()
        self.pin = obstacle_pin.Obstacle_Pin()
        #self.fork.set_active(False)
        #self.pin.set_active(True)
    def choice_obstacle(self):
        self.choice = random.randint(0,2)
    def update(self):
        if self.choice == 2:
            self.fork.update()
        else :
            self.pin.update()
        if self.fork.x <-100 or self.pin.x < -100:
            self.choice_obstacle()
            self.fork.enter()
            self.pin.enter()
    def draw(self):
        self.fork.draw()
        self.pin.draw()
        #self.image.clip_draw(0,0,526,513,600,250)
    def get_bb(self):
        if self.choice == 2:
            return self.fork.get_bb()
        else : return self.pin.get_bb()