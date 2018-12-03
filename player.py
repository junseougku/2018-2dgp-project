
from pico2d import *

import mygame
DOWN_DOWN ,DOWN_UP,SPACE_DOWN,TIME_OUT,JUMP_DOWN   = range(5)
key_event_table = {

    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP,SDLK_DOWN) : DOWN_UP,
    (SDL_KEYDOWN,SDLK_SPACE) : SPACE_DOWN,
    (SDL_KEYDOWN,SDLK_x) : JUMP_DOWN,
}



class Walk:
    @staticmethod
    def enter(obj):
        obj.frame = 0
        obj.bb_count = 2
        obj.now_image.opacify(1)
    @staticmethod
    def exit(obj):
        obj.now_image.opacify(1)
    @staticmethod
    def draw(obj):

        obj.images[0].clip_draw(int(obj.frame) * 129, 0, 129, 146, obj.x, obj.y)
        return obj.images[0]
    @staticmethod
    def update(obj):
        #obj.frame = (obj.frame + 1) % 4
        obj.frame = (obj.frame + 4 * mygame.ACTION_PER_TIME * mygame.frame_time) % 4
    @staticmethod
    def collider(obj):
        pass

    @staticmethod
    def get_bb(obj):
        return [(obj.x - 54,obj.y+(obj.y/3) - 30, obj.x + 54,obj.y+(obj.y/3) + 30),(obj.x+15 - 48,obj.y-(obj.y/3) - 30, obj.x + 48,obj.y-(obj.y/3) + 30)]

    @staticmethod
    def draw_bb(obj):
        draw_rectangle(obj.x - 54,obj.y+(obj.y/3) - 30, obj.x + 54,obj.y+(obj.y/3) + 30)
        draw_rectangle(obj.x+15 - 48,obj.y-(obj.y/3) - 30, obj.x + 48,obj.y-(obj.y/3) + 30)

class Head:
    @staticmethod
    def enter(obj):
        obj.frame = 0
        obj.y -= 30.5
        obj.sounds[1].play()
    @staticmethod
    def exit(obj):
        obj.y += 30.5
    @staticmethod
    def draw(obj):
        obj.images[1].clip_draw(int(obj.frame) * 184, 0, 184, 85, obj.x, obj.y)
        return obj.images[1]
    @staticmethod
    def update(obj):
        obj.frame = (obj.frame + 2 * mygame.ACTION_PER_TIME * mygame.frame_time) % 2
    @staticmethod
    def get_bb(obj):
        return [(obj.x - 82, obj.y - 42.5, obj.x + 82, obj.y + 27.5)]

    @staticmethod
    def draw_bb(obj):
        draw_rectangle( obj.x - 82, obj.y - 42.5, obj.x + 82, obj.y + 27.5)


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
        obj.images[2].clip_draw(int(obj.frame) * 132 , 0 ,132,148,obj.x,obj.y)
        return obj.images[2]
    @staticmethod
    def update(obj):
        obj.frame = (obj.frame + 4 * mygame.ACTION_PER_TIME * mygame.frame_time) % 4
    @staticmethod
    def collider(obj):
        pass
    @staticmethod
    def get_bb(obj):
        return [(obj.x - 47 , obj.y+22 - 52 , obj.x + 42 , obj.y+22 + 42),
                (obj.x-10 - 47, obj.y-22 - 42, obj.x + 37, obj.y-22 + 32)]
    @staticmethod
    def draw_bb(obj):
        draw_rectangle(obj.x - 47 , obj.y+22 - 52 , obj.x + 42 , obj.y+22 + 42)
        draw_rectangle(obj.x-10 - 47, obj.y-22 - 42, obj.x + 37, obj.y-22 + 32)

jump_stat = 0
class Jump:
    @staticmethod
    def enter(obj):
        global jump_stat
        jump_stat = 40
        obj.frame = 0
        obj.start_y = obj.y
        obj.max_y = obj.y + 150
        obj.end_y = 100
        obj.jumping = True
        obj.sounds[0].play()
    @staticmethod
    def exit(obj):
        for i in range(3):
            obj.images[3][i].opacify(1)
    @staticmethod
    def draw(obj):
        if obj.jumpcount < 10:
            obj.images[3][0].draw_now(obj.x ,obj.y)
            return obj.images[3][0]
        elif obj.jumpcount >= 10 and obj.jumpcount <= 20:
            obj.images[3][1].clip_draw(int(obj.frame) * 132 ,0,132,136,obj.x,obj.y)
            return obj.images[3][1]
        elif obj.jumpcount > 20:
            obj.images[3][2].draw_now(obj.x,obj.y)
            return obj.images[3][2]
    @staticmethod
    def update(obj):
        obj.frame = (obj.frame + 2 * mygame.ACTION_PER_TIME * mygame.frame_time) % 2
    @staticmethod
    def get_bb(obj):
        if obj.jumpcount < 10:
            return [(obj.x - 31.5 , obj.y - 67 , obj.x + 31.5 , obj.y + 47)]
        elif obj.jumpcount >= 10 and obj.jumpcount <= 20:
            return [(obj.x - 44 , obj.y - 53 , obj.x + 44 , obj.y + 48)]
        elif obj.jumpcount > 20:
            return [(obj.x - 38.5 , obj.y - 59 , obj.x + 38.5 , obj.y + 44)]

    @staticmethod
    def draw_bb(obj):
        if obj.jumpcount < 10:
            draw_rectangle( obj.x - 31.5 , obj.y - 67 , obj.x + 31.5 , obj.y + 47)
        elif obj.jumpcount >= 10 and obj.jumpcount <= 20:
            draw_rectangle (obj.x - 46 , obj.y - 53 , obj.x + 46 , obj.y + 48)
        elif obj.jumpcount > 20:
            draw_rectangle (obj.x - 40.5 , obj.y - 59 , obj.x + 40.5 , obj.y + 44)

jumpcount = 0

class DoubleJump:
    @staticmethod
    def enter(obj):
        obj.frame = 0
        obj.end_y = 100
        obj.start_y = obj.y
        obj.max_y = obj.y + 150
        obj.doublejumping = True
        obj.jumpcount = 0
        obj.sounds[0].play()
    @staticmethod
    def exit(obj):
        for i in range(3):
            obj.images[4][i].opacify(1)
    @staticmethod
    def draw(obj):
        if obj.jumpcount < 40:
            obj.images[4][0].draw_now(obj.x, obj.y)
            return obj.images[4][0]
        elif obj.jumpcount >= 40 and obj.jumpcount <= 60:
            obj.images[4][1].clip_draw(int(obj.frame) * 116, 0, 116, 127, obj.x, obj.y)
            return obj.images[4][1]
        elif obj.jumpcount > 60:
            obj.images[4][2].draw_now(obj.x,obj.y)
            return obj.images[4][2]
    @staticmethod
    def update(obj):
        obj.frame = (obj.frame + 3 * mygame.ACTION_PER_TIME * mygame.frame_time) % 3
    @staticmethod
    def get_bb(obj):
        if obj.jumpcount < 40:
            return [(obj.x - 57 , obj.y+20 - 21.5 , obj.x + 57 , obj.y+20 + 41.5),(obj.x+20 -37,obj.y-30 -21.5,obj.x+20+32 , obj.y -30 + 41.5)]
        elif obj.jumpcount >= 40 and obj.jumpcount <= 60:
            return [(obj.x - 52, obj.y - 51.5, obj.x + 52, obj.y + 51.5)]
        elif obj.jumpcount > 60:
            return [(obj.x - 47, obj.y - 61.5, obj.x + 47, obj.y + 41.5)]

    @staticmethod
    def draw_bb(obj):
        if obj.jumpcount < 40:
            draw_rectangle(obj.x - 57 , obj.y+20 - 21.5 , obj.x + 57 , obj.y+20 + 41.5)
            draw_rectangle(obj.x+20 -37,obj.y-30 -21.5,obj.x+20+32 , obj.y -30 + 41.5)
        elif obj.jumpcount >= 40 and obj.jumpcount <= 60:
            draw_rectangle(obj.x - 52, obj.y - 51.5, obj.x + 52, obj.y + 51.5)
        elif obj.jumpcount > 60:
            draw_rectangle(obj.x - 47, obj.y - 61.5, obj.x + 47, obj.y + 41.5)
wound_start_time = 0.0

class Wound:
    @staticmethod
    def enter(obj):
        global wound_start_time
        obj.frame = 0
        wound_start_time = get_time()
        obj.sounds[2].play()
    @staticmethod
    def exit(obj):
        pass

    @staticmethod
    def draw(obj):
        obj.images[5].clip_draw(int(obj.frame) * 148, 0, 148, 136, obj.x, obj.y)
        return obj.images[5]

    @staticmethod
    def update(obj):
        obj.frame = (obj.frame + 3 * mygame.ACTION_PER_TIME * mygame.frame_time) % 3
        if get_time() - wound_start_time > 1.2:
            obj.blink = False
            obj.now_image.opacify(1)
            obj.add_event(TIME_OUT)

    @staticmethod
    def get_bb(obj):
        return [(0,0,0,0)]

    @staticmethod
    def draw_bb(obj):
        pass

class Death:
    @staticmethod
    def enter(obj):
        obj.frame = 0
        obj.sounds[3].play()
    @staticmethod
    def exit(obj):
        pass
    @staticmethod
    def update(obj):
        if obj.frame <= 7:
            obj.frame = (obj.frame + 7 * mygame.ACTION_PER_TIME * mygame.frame_time /4)

    @staticmethod
    def draw(obj):
        if obj.frame <= 3:
            obj.images[5].clip_draw(int(obj.frame) * 148, 0, 148, 136, obj.x, obj.y)
        else :

            obj.images[6].clip_draw(int(obj.frame -4) * 199, 0, 199, 120, obj.x, obj.y-20)

    @staticmethod
    def get_bb(obj):
        return [(0, 0, 0, 0)]

    @staticmethod
    def draw_bb(obj):
        pass

next_state_table = {
    Walk: {DOWN_DOWN: Head  , SPACE_DOWN : Run ,JUMP_DOWN : Jump  },
    Head: {DOWN_DOWN: Head, DOWN_UP: Walk, SPACE_DOWN : Head , JUMP_DOWN : Jump},
    Run: {DOWN_DOWN: Head ,  TIME_OUT : Walk , JUMP_DOWN : Jump},
    Jump : {  JUMP_DOWN : DoubleJump , TIME_OUT : Walk},
    DoubleJump : {  TIME_OUT : Walk},
    Wound : { TIME_OUT : Walk },
    Death : { TIME_OUT : Walk}
}
opstat = 1.0
cool_end_time = False

class Player:

    def __init__(self):
        self.images = [load_image("image\\work_player_.png"),load_image("image\\head_player_.png"),load_image("image\\run_player_.png")
                       ,[load_image("image\\player_jump_1.png"), load_image("image\\jump_player_.png"),
                            load_image("image\\player_jump_4.png")] , [ load_image("image\\player_doublejump_1.png") , load_image("image\\doublejump_player_.png")
                                  , load_image("image\\player_doublejump_5.png")]
                       ,load_image("image\\wound_player_.png"), load_image("image\\death_player_.png")]
        self.sounds = [load_wav('sound\\jump_.wav'),load_wav("sound\\head_.wav"),load_wav("sound\\wound_.wav"),load_wav("sound\\end_.wav")]
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
        self.doublejumping = False
        self.running = False
        self.blink = False
        self.now_image = self.images[0]
        self.jumpcount = 0
        self.bb_count = 0
        for i in self.sounds:
            i.set_volume(48)
    def draw(self):
        self.now_image = self.current_state.draw(self)
       # if mygame.drawbb == True:
        #    draw_rectangle(*self.current_state.get_bb(self))
        #self.draw_bb()

    def update(self):
        self.current_state.update(self)
        self.run_speed_exit()
        self.update_jump()
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            if mygame.delay_check == False: return
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
            if event.type == SDL_KEYDOWN and event.key == SDLK_p:
                mygame.timestop = True
            if event.type == SDL_KEYDOWN and event.key == SDLK_o:
                if mygame.drawbb == False:
                    mygame.drawbb = True
                else: mygame.drawbb = False
            if event.type == SDL_QUIT:
                mygame.loop = False
                mygame.regame = False
            elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
                mygame.loop = False
                mygame.regame = False
            if event.type == SDL_KEYDOWN and event.key == SDLK_SPACE and mygame.delay_check and mygame.dead :
                mygame.loop = False
            elif (event.type, event.key) in key_event_table:
                key_event = key_event_table[(event.type, event.key)]
                self.add_event(key_event)
    def get_bb(self,obj):
        if obj.get_bb() == (0,0,0,0): return
        left_b,bottom_b,right_b,top_b = obj.get_bb()
        for (_a_l,_a_b,_a_r,_a_t) in self.current_state.get_bb(self):
            if _a_l > right_b : return False
            if _a_r < left_b : return False
            if _a_t < bottom_b : return False
            if _a_b > top_b : return False

            return True
    def cooltime_enter(self):
        if self.current_state == Death: return
        global cool_start_time
        global cool_end_time
        cool_start_time = get_time()
        cool_end_time = get_time()
        self.blink = True
    def cooltime(self):
        if self.current_state == Death: return
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
    def run_speed_exit(self):
        global run_start_time
        if self.running == False:return
        if get_time() - run_start_time > 4.5:
            self.running = False
            if self.current_state == Run:
                self.add_event(TIME_OUT)
    def update_jump(self):
        if self.jumping:
            if self.doublejumping:
                jump_stat = 80
            else: jump_stat = 40
            self.jumpcount = ( self.jumpcount + 35 *mygame.ACTION_PER_TIME * mygame.frame_time)
            #obj.frame = (obj.frame + 3 * mygame.ACTION_PER_TIME * mygame.frame_time) % 3
            #self.jumpcount = int(self.jumpcount + 80 * mygame.ACTION_PER_TIME * mygame.frame_time)
            t = self.jumpcount / jump_stat
            y = (2 * t ** 2 - 3 * t + 1) * self.start_y + (-4 * t ** 2 + 4 * t) * self.max_y + (2 * t ** 2 - t) * self.end_y
            self.y = y
            if self.jumpcount >= jump_stat:
                self.jumpcount = 0
                self.jumping = False
                self.doublejumping = False
                if self.current_state == Jump or self.current_state == DoubleJump:
                    self.add_event(TIME_OUT)
    def draw_bb(self):
        self.current_state.draw_bb(self)
