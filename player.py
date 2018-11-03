
from pico2d import *


DOWN_DOWN ,DOWN_UP,SPACE_DOWN,TIME_OUT,JUMP_DOWN ,  = range(5)
key_event_table = {
    #(SDL_KEYDOWN, SDLK_RIGHT): RIGHT,
    #(SDL_KEYDOWN, SDLK_LEFT): LEFT,
    #(SDL_KEYDOWN, SDLK_UP): UP,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP,SDLK_DOWN) : DOWN_UP,
    (SDL_KEYDOWN,SDLK_SPACE) : SPACE_DOWN,
    (SDL_KEYDOWN,SDLK_x) : JUMP_DOWN,
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
jumpcount = 0
class Jump:
    @staticmethod
    def enter(obj):
        obj.frame = 0
        obj.start_y = obj.y
        obj.max_y = obj.y + 100
        obj.end_y = obj.y
        obj.jumping = True
    @staticmethod
    def exit(obj):
        obj.jumping = False
    @staticmethod
    def draw(obj):
        global jumpcount
        if jumpcount < 25:
            obj.jump_image[0].draw_now(obj.x ,obj.y)
        elif jumpcount >= 25 and jumpcount <= 75:
            obj.jump_image[1].clip_draw(obj.frame * 132 ,0,132,136,obj.x,obj.y)
        elif jumpcount > 75:
            obj.jump_image[2].draw_now(obj.x,obj.y)
    @staticmethod
    def update(obj):
        obj.frame = (obj.frame + 1) % 2
        global jumpcount
        jumpcount += 2

        t = jumpcount / 100
        x = (2 * t ** 2 - 3 * t + 1) * obj.x + (-4 * t ** 2 + 4 * t) * obj.x + (2 * t ** 2 - t) * obj.x
        y = (2 * t ** 2 - 3 * t + 1) * obj.start_y + (-4 * t ** 2 + 4 * t) * obj.max_y + (2 * t ** 2 - t) * obj.end_y
        obj.x = x
        obj.y = y
        if jumpcount == 100:
            jumpcount = 0
            obj.add_event(TIME_OUT)
    @staticmethod
    def doublejump_enter(obj):
        obj.end_y = obj.start_y
        obj.start_y = obj.y
        obj.max_y = obj.y + 100
    @staticmethod
    def doublejump_update(obj):
        obj.frame = (obj.frame + 1) % 3
        global jumpcount
        jumpcount += 2

        t = jumpcount / 100
        x = (2 * t ** 2 - 3 * t + 1) * obj.x + (-4 * t ** 2 + 4 * t) * obj.x + (2 * t ** 2 - t) * obj.x
        y = (2 * t ** 2 - 3 * t + 1) * obj.start_y + (-4 * t ** 2 + 4 * t) * obj.max_y + (2 * t ** 2 - t) * obj.end_y
        obj.x = x
        obj.y = y
        if jumpcount == 200:
            jumpcount = 0
            obj.add_event(TIME_OUT)

next_state_table = {
    Work: {DOWN_DOWN: Head , DOWN_UP : Work , SPACE_DOWN : Run ,JUMP_DOWN : Jump},
    Head: {DOWN_DOWN: Head, DOWN_UP: Work, SPACE_DOWN : Head , JUMP_DOWN : Jump},
    Run: {DOWN_DOWN: Head , DOWN_UP : Run, SPACE_DOWN : Run , TIME_OUT : Work , JUMP_DOWN : Jump},
    Jump : {DOWN_DOWN : Jump, DOWN_UP : Jump , SPACE_DOWN : Jump , JUMP_DOWN : Jump , TIME_OUT : Work}
}

import mygame
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
        self.jump_image = [ load_image("image\\player_jump_1.png"), load_image("image\\jump_player_.png"),
                            load_image("image\\player_jump_4.png")]
        self.doublejump_image = [ load_image("image\\player_doublejump_1.png") , load_image("image\\doublejump_player_.png")
                                  , load_image("image\\player_doublejump_5.png")]
        self.start_y = 0
        self.max_y = 0
        self.end_y = 0
        self.jumping = False
    def draw(self):
        self.current_state.draw(self)
    def update(self):
        self.current_state.update(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            if self.current_state == next_state_table[self.current_state][event]:
                return
            self.current_state.exit(self)
            self.current_state = next_state_table[self.current_state][event]
            self.current_state.enter(self)
    def enter(self):
        self.current_state.enter(self)
    def exit(self):
        self.current_state.exit(self)
    def add_event(self,event):
        self.event_que.insert(0, event)
    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                mygame.running = False
                close_canvas()
                del(mygame.playerchar)
                del(mygame.grass_01)
            if event.type == SDL_KEYDOWN and event.key == SDLK_p:
                mygame.timestop = True
            elif (event.type, event.key) in key_event_table:
                key_event = key_event_table[(event.type, event.key)]
                self.add_event(key_event)
