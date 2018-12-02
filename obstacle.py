from pico2d import *

obstacle_list = [load_image("image\\obstacle_1.png"),load_image("image\\obstacle_2.png"),load_image("image\\obstacle_4.png")]
import obstacle_fork
import obstacle_pin
import obstacle_dynamic
import random
import mygame
class Obstacle_line:
    def __init__(self):
        self.choice = 0
        #self.image = load_image("C:\\2DGP\\2018-2dgp-project\\image\\Attack.png")
        self.fork = obstacle_fork.Obstacle_Fork()
        self.pin = obstacle_pin.Obstacle_Pin()
        self.dynamic = obstacle_dynamic.Obstacle_Dynamic()
        #self.fork.set_active(False)
        #self.pin.set_active(True)
    def choice_obstacle(self):
        self.choice = random.randint(0,3)
        self.choice = 3
    def update(self):
        if mygame.delay_check:
            if self.choice == 2:
                self.fork.update()
            elif self.choice == 3:
                self.dynamic.update()
            else :
                self.pin.update()

            if self.fork.x <-100 or self.pin.x < -100 or self.dynamic.x < -100:
                self.choice_obstacle()
                self.fork.enter()
                self.pin.enter()
                self.dynamic.enter()
    def draw(self):
        self.fork.draw()
        self.pin.draw()
        self.dynamic.draw()
        #self.image.clip_draw(0,0,526,513,600,250)
    def get_bb(self):
        if self.choice == 2:
            return self.fork.get_bb()
        elif self.choice == 3:
            return self.dynamic.get_bb()
        else : return self.pin.get_bb()