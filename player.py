
from pico2d import *

import mygame
DOWN_DOWN ,DOWN_UP,SPACE_DOWN,TIME_OUT,JUMP_DOWN   = range(5)
key_event_table = {
    #(SDL_KEYDOWN, SDLK_RIGHT): RIGHT,
    #(SDL_KEYDOWN, SDLK_LEFT): LEFT,
    #(SDL_KEYDOWN, SDLK_UP): UP,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP,SDLK_DOWN) : DOWN_UP,
    (SDL_KEYDOWN,SDLK_SPACE) : SPACE_DOWN,
    (SDL_KEYDOWN,SDLK_x) : JUMP_DOWN,
}



class Walk:
    @staticmethod
    def enter(obj):
        obj.frame = 0
    @staticmethod
    def exit(obj):
        pass
    @staticmethod
    def draw(obj):
        obj.images[0].clip_draw(obj.frame * 129, 0, 129, 146, obj.x, obj.y)
        return obj.images[0]
    @staticmethod
    def update(obj):
        obj.frame = (obj.frame + 1) % 4
    @staticmethod
    def get_bb(obj):
        return obj.x - 64.5,obj.y - 73, obj.x + 64.5,obj.y + 73

class Head:
    @staticmethod
    def enter(obj):
        obj.frame = 0
        obj.y -= 30.5
    @staticmethod
    def exit(obj):
        obj.y += 30.5
    @staticmethod
    def draw(obj):
        obj.images[1].clip_draw(obj.frame * 184, 0, 184, 85, obj.x, obj.y)
        return obj.images[1]
    @staticmethod
    def update(obj):
        obj.frame = (obj.frame + 1) % 2
    @staticmethod
    def get_bb(obj):
        return obj.x - 92 , obj.y - 42.5 , obj.x + 92 , obj.y + 42.5

run_start_time = get_time()
cool_start_time = get_time()
class Run:
    @staticmethod
    def enter(obj):
        obj.frame = 0
        if obj.running == True: return
        global run_start_time
        run_start_time = get_time()
        obj.running = True
    @staticmethod
    def exit(obj):
        pass
    @staticmethod
    def draw(obj):
        obj.images[2].clip_draw(obj.frame * 132 , 0 ,132,148,obj.x,obj.y)
        return obj.images[2]
    @staticmethod
    def update(obj):
        obj.frame = (obj.frame + 1) % 4
    @staticmethod
    def get_bb(obj):
        return obj.x - 67 , obj.y - 74 , obj.x + 67 , obj.y + 74
jumpcount = 0
class Jump:
    @staticmethod
    def enter(obj):

        obj.frame = 0
        obj.start_y = obj.y
        obj.max_y = obj.y + 150
        obj.end_y = obj.y
        obj.jumping = True
    @staticmethod
    def exit(obj):
        for i in range(3):
            obj.images[3][i].opacify(1)
        obj.jumping = False
    @staticmethod
    def draw(obj):
        global jumpcount
        if jumpcount < 10:
            obj.images[3][0].draw_now(obj.x ,obj.y)
            return obj.images[3][0]
        elif jumpcount >= 10 and jumpcount <= 20:
            obj.images[3][1].clip_draw(obj.frame * 132 ,0,132,136,obj.x,obj.y)
            return obj.images[3][1]
        elif jumpcount > 20:
            obj.images[3][2].draw_now(obj.x,obj.y)
            return obj.images[3][2]
    @staticmethod
    def update(obj):
        obj.frame = (obj.frame + 1) % 2
        global jumpcount
        jumpcount += 2

        t = jumpcount / 40
        y = (2 * t ** 2 - 3 * t + 1) * obj.start_y + (-4 * t ** 2 + 4 * t) * obj.max_y + (2 * t ** 2 - t) * obj.end_y
        obj.y = y
        if jumpcount == 40:
            jumpcount = 0
            obj.add_event(TIME_OUT)
    @staticmethod
    def get_bb(obj):
        global jumpcount
        if jumpcount < 10:
            return obj.x - 51.5 , obj.y - 87 , obj.x + 51.5 , obj.y + 87
        elif jumpcount >= 10 and jumpcount <= 20:
            return obj.x - 66 , obj.y - 68 , obj.x + 66 , obj.y + 68
        elif jumpcount > 20:
            return obj.x - 60.5 , obj.y - 74 , obj.x + 60.5 , obj.y + 74

class DoubleJump:
    @staticmethod
    def enter(obj):
        global jumpcount
        obj.frame = 0
        obj.end_y = obj.start_y
        obj.start_y = obj.y
        obj.max_y = obj.y + 150
        jumpcount = 0
    @staticmethod
    def exit(obj):
        for i in range(3):
            obj.images[4][i].opacify(1)
    @staticmethod
    def draw(obj):
        global jumpcount
        if jumpcount < 40:
            obj.images[4][0].draw_now(obj.x, obj.y)
            return obj.images[4][0]
        elif jumpcount >= 40 and jumpcount <= 60:
            obj.images[4][1].clip_draw(obj.frame * 116, 0, 116, 127, obj.x, obj.y)
            return obj.images[4][1]
        elif jumpcount > 60:
            obj.images[4][2].draw_now(obj.x,obj.y)
            return obj.images[4][2]
    @staticmethod
    def update(obj):
        obj.frame = (obj.frame + 1) % 3
        global jumpcount
        jumpcount += 2

        t = jumpcount / 80
        y = (2 * t ** 2 - 3 * t + 1) * obj.start_y + (-4 * t ** 2 + 4 * t) * obj.max_y + (2 * t ** 2 - t) * obj.end_y
        obj.y = y
        if jumpcount == 80:
            jumpcount = 0
            obj.add_event(TIME_OUT)
    @staticmethod
    def get_bb(obj):
        return obj.x - 72 , obj.y - 71.5 , obj.x + 72 , obj.y + 71.5

wound_start_time = 0.0

class Wound:
    @staticmethod
    def enter(obj):
        global wound_start_time
        obj.frame = 0
        wound_start_time = get_time()
    @staticmethod
    def exit(obj):
        pass

    @staticmethod
    def draw(obj):
        obj.images[5].clip_draw(obj.frame * 148, 0, 148, 136, obj.x, obj.y)
        return obj.images[5]

    @staticmethod
    def update(obj):
        obj.frame = (obj.frame + 1) % 3
        if get_time() - wound_start_time > 2.0:
            obj.add_event(TIME_OUT)

    @staticmethod
    def get_bb(obj):
        return obj.x - 74, obj.y - 66, obj.x + 74, obj.y + 66


next_state_table = {
    Walk: {DOWN_DOWN: Head  , SPACE_DOWN : Run ,JUMP_DOWN : Jump  },
    Head: {DOWN_DOWN: Head, DOWN_UP: Walk, SPACE_DOWN : Head , JUMP_DOWN : Jump},
    Run: {DOWN_DOWN: Head ,  TIME_OUT : Walk , JUMP_DOWN : Jump},
    Jump : {  JUMP_DOWN : DoubleJump , TIME_OUT : Walk},
    DoubleJump : {  TIME_OUT : Walk},
    Wound : { TIME_OUT : Walk }
}
opstat = 1.0
cool_end_time = False

class Player:

    def __init__(self):
        self.images = [load_image("image\\work_player_.png"),load_image("image\\head_player_.png"),load_image("image\\run_player_.png")
                       ,[load_image("image\\player_jump_1.png"), load_image("image\\jump_player_.png"),
                            load_image("image\\player_jump_4.png")] , [ load_image("image\\player_doublejump_1.png") , load_image("image\\doublejump_player_.png")
                                  , load_image("image\\player_doublejump_5.png")]
                       ,load_image("image\\wound_player_.png")]
        self.x = 150
        self.y = 100
        self.frame = 0
        self.current_state = Walk
        self.jumpspeed = 0.0
        self.event_que = []
        self.start_y = 0
        self.max_y = 0
        self.end_y = 0
        self.jumping = False
        self.running = False
        self.blink = False
        self.now_image = self.images[0]
    def draw(self):
        self.now_image = self.current_state.draw(self)
        if mygame.drawbb == True:
            draw_rectangle(*self.current_state.get_bb(self))

    def update(self):
        self.current_state.update(self)
        self.run_speed_exit()
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            if (event not in next_state_table[self.current_state]) == True:
                return
            if self.current_state == next_state_table[self.current_state][event]:
                return
            self.exit()
            self.current_state = next_state_table[self.current_state][event]
            if self.running == True and self.current_state == Walk:
                self.current_state = Run
            self.enter()
    def change_state(self,state):
        self.exit()
        self.current_state = state
        self.enter()
    def enter(self):
        self.current_state.enter(self)
    def exit(self):
        self.now_image.opacify(1)
        self.current_state.exit(self)
    def add_event(self,event):
        self.event_que.insert(0, event)
    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                mygame.running = False
            if event.type == SDL_KEYDOWN and event.key == SDLK_p:
                mygame.timestop = True
            if event.type == SDL_KEYDOWN and event.key == SDLK_o:
                if mygame.drawbb == False:
                    mygame.drawbb = True
                else: mygame.drawbb = False
            if (event.type, event.key) in key_event_table:
                key_event = key_event_table[(event.type, event.key)]
                self.add_event(key_event)
    def get_bb(self,obj):
        left_a,bottom_a,right_a,top_a = self.current_state.get_bb(self)
        left_b,bottom_b,right_b,top_b = obj.get_bb()
        if left_a > right_b : return False
        if right_a < left_b : return False
        if top_a < bottom_b : return False
        if bottom_a > top_b : return False

        return True
    def cooltime_enter(self):
        global cool_start_time
        global cool_end_time
        cool_start_time = get_time()
        cool_end_time = get_time()
        self.blink = True
    def cooltime(self):
        global cool_start_time
        global opstat
        global cool_end_time
        if self.blink and get_time() - cool_start_time > 0.1:
            cool_start_time = get_time()
            if opstat == 1.0:
                opstat = 0.5
                self.now_image.opacify(opstat)
            elif opstat == 0.5:
                opstat = 1.0
                self.now_image.opacify(opstat)
            if get_time() - cool_end_time > 1:
                self.blink = False
                self.now_image.opacify(1)
    def run_speed_exit(self):
        global run_start_time
        if self.running == False:return
        if get_time() - run_start_time > 4.5:
            self.running = False
            if self.current_state == Run:
                self.add_event(TIME_OUT)
