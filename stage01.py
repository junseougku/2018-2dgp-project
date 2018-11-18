from pico2d import *
import enemy
import random
class Stage01 :
    def __init__(self):
        self.basic_enemy = enemy.Enemy()
        self.monster_Createtime = get_time()
        self.enemy_active_cooltime = 2
    def do(self):
        if self.basic_enemy.x < -200 and self.basic_enemy.active == True:
            self.basic_enemy.active = False
        if get_time() - self.monster_Createtime > self.enemy_active_cooltime:
            if self.basic_enemy.active == True :
                self.monster_Createtime = get_time()
                return
            self.basic_enemy.change_state(enemy.Walk)
            self.active_random()
            self.monster_Createtime = get_time()
    def draw(self):
        if self.basic_enemy.active:
            self.basic_enemy.draw()

    def update(self):
        if self.basic_enemy.active:
            self.basic_enemy.update()

    def active_random(self):
        self.enemy_active_cooltime = random.randint(3,7)

    def collision(self,obj):
        if obj.get_bb(self.basic_enemy):
            if self.basic_enemy.active == False: return
            print("enemy collision")
            self.basic_enemy.change_state(enemy.Dead)


