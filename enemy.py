from pico2d import*
import mygame
import random
class Walk:
    @staticmethod
    def enter(obj):
        obj.x = 900
        obj.y = random.randint(150,550)
        obj.frame = 0
        obj.active = True
    @staticmethod
    def draw(obj):
        obj.images[0].clip_draw(obj.frame * 124, 0, 124, 73, obj.x, obj.y)
    @staticmethod
    def update(obj):
        obj.frame = (obj.frame + 1) % 3
    @staticmethod
    def exit(obj):
        pass
    @staticmethod
    def get_bb(obj):
        return obj.x - 62, obj.y - 36.5, obj.x + 62, obj.y + 36.5
class Dead:
    @staticmethod
    def enter(obj):
        obj.frame = 0

    @staticmethod
    def draw(obj):
        obj.images[1].clip_draw(obj.frame * 174,0,174,175,obj.x,obj.y)

    @staticmethod
    def update(obj):
        if obj.frame == 6:
            obj.active = False
            return
        obj.frame+= 1
    @staticmethod
    def exit(obj):
        obj.active = False
    @staticmethod
    def get_bb(obj):
        return 0,0,0,0

class Enemy:
    def __init__(self):
        self.x = 900
        self.y = 200
        self.frame = 0
        self.images = [load_image("image\\enemy_.png"),load_image("image\\enemy_death_.png")]
        self.velocity = mygame.GRASS_SPEED_PPS * 1.5
        self.active = False
        self.current_state = Dead
    def enter(self):
        self.current_state.enter(self)
    def draw(self):
        self.current_state.draw(self)
        draw_rectangle(*self.current_state.get_bb(self))
    def update(self):
        self.current_state.update(self)
        mygame.move_update(self)
    def exit(self):
        self.current_state.exit(self)
    def get_bb(self):
        return self.current_state.get_bb(self)
    def change_state(self,state):
        self.current_state.exit(self)
        self.current_state = state
        self.current_state.enter(self)
