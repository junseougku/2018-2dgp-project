
from pico2d import *
gravity = 0.0
import time
DOWN_DOWN ,DOWN_UP,SPACE_DOWN,TIME_OUT= range(4)
key_event_table = {
    #(SDL_KEYDOWN, SDLK_RIGHT): RIGHT,
    #(SDL_KEYDOWN, SDLK_LEFT): LEFT,
    #(SDL_KEYDOWN, SDLK_UP): UP,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP,SDLK_DOWN) : DOWN_UP,
    (SDL_KEYDOWN,SDLK_SPACE) : SPACE_DOWN,
}

class Work:
    @staticmethod
    def enter(obj):
        obj.frame = 0
    @staticmethod
    def exit(obj):
        pass
    @staticmethod
    def draw(obj):
        obj.work_image.clip_draw(obj.frame * 129, 0, 129, 146, obj.x, obj.y)
    @staticmethod
    def update(obj):
        obj.frame = (obj.frame + 1) % 4

class Head:
    @staticmethod
    def enter(obj):
        obj.frame = 0
    @staticmethod
    def exit(obj):
        pass
    @staticmethod
    def draw(obj):
        obj.head_image.clip_draw(obj.frame * 184, 0, 184, 85, obj.x, obj.y - 30.5)
    @staticmethod
    def update(obj):
        obj.frame = (obj.frame + 1) % 2

start_time = get_time()

class Run:
    @staticmethod
    def enter(obj):
        global start_time
        obj.frame = 0
        start_time = get_time()
    @staticmethod
    def exit(obj):
        pass
    @staticmethod
    def draw(obj):
        obj.run_image.clip_draw(obj.frame * 132 , 0 ,132,148,obj.x,obj.y)
    @staticmethod
    def update(obj):
        global start_time
        obj.frame = (obj.frame + 1) % 4
        if get_time() - start_time > 1.5:
            obj.add_event(TIME_OUT)

class Jump:
    @staticmethod
    def enter(obj):
        obj.frame = 0
    @staticmethod
    def exit(obj):
        pass
    @staticmethod
    def draw(obj):
        pass
    @staticmethod
    def update(obj):
        pass

next_state_table = {
    Work: {DOWN_DOWN: Head , DOWN_UP : Work , SPACE_DOWN : Run },
    Head: {DOWN_DOWN: Head, DOWN_UP: Work, SPACE_DOWN : Head},
    Run: {DOWN_DOWN: Head , DOWN_UP : Run, SPACE_DOWN : Run , TIME_OUT : Work}
}
class Player:
    def __init__(self):
        self.x = 150
        self.y = 100
        self.frame = 0
        self.current_state = Work
        self.jumpspeed = 0.0
        self.event_que = []
        self.work_image = load_image("image\\work_player_.png")
        self.run_image = load_image("image\\run_player_.png")
        self.head_image = load_image("image\\head_player_.png")
    def draw(self):
        self.current_state.draw(self)
    def update(self):
        self.current_state.update(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.current_state.exit(self)
            self.current_state = next_state_table[self.current_state][event]
            self.current_state.enter(self)
    def enter(self):
        self.current_state.enter(self)
    def exit(self):
        self.current_state.exit(self)
    def draw_curve(self,curxx,heix,dotx,cury,heiy,doty,i):
        global jump

        t = i / 100
        x = (2*t**2-3*t+1) * curxx + (-4 * t ** 2 + 4 * t) * heix+(2*t**2-t)*dotx
        y = (2*t **2-3*t+1) * cury +(-4 * t ** 2 + 4 * t) * heiy+(2*t**2-t)*doty
        self.x = x
        self.y = y
        self.draw()
        if i == 20:
            jump = False
    def jump(self):
        #self.draw_curve(self.x, self.x , self.x , self.y, self.y + 100, self.y,i)
        pass
    def add_event(self,event):
        self.event_que.insert(0, event)
    def handle_events(self):
        events = get_events()
        for event in events:
            if (event.type, event.key) in key_event_table:
                key_event = key_event_table[(event.type, event.key)]
                self.add_event(key_event)
jump = False
