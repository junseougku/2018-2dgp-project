from pico2d import *
import time
import player
import grass
import item
import obstacle
import static_objects_group
import effect
import stage01
import ball
playerchar = None
grass_01 = None
grass_02 = None
grass_03 = None
medicine = None
coins = None
obstacle_ = None
stage1_sequence = None
attack_ball = None

PIXEL_PER_METER = (10.0/ 0.3)
GRASS_SPEED = 40.0
GRASS_SPEED_MPM = (GRASS_SPEED * 1000.0 / 60.0)
GRASS_SPEED_MPS = (GRASS_SPEED_MPM / 60.0)
GRASS_SPEED_PPS = (GRASS_SPEED_MPS * PIXEL_PER_METER)

frame_time = 0.0
loop = True
timestop = False
timestop_exit = False
drawbb =True
slow_start = False
slow_speed_start = get_time()
item_table = {
    item.Coin : 0,
    item.Medicine : 10
}
eat_effect = effect.Effect()

objects = [[],[]]       #움직이고 없어질수 있는 객체들
def add_object(o,layer):
    objects[layer].append(o)

def collision_enemy():
    pass

def remove_object(o):
    for i in range(len(objects)):
        if i == 1 and playerchar.blink == False:
            global slow_speed_start,slow_start
            playerchar.cooltime_enter()
            playerchar.change_state(player.Wound)
            slow_speed_start = get_time()
            slow_start = True
            print("collsion")
            break
        if o in objects[i]:
            if i == 1: break
            print("remove")
            if type(o) in item_table:
                if type(o) == item.Coin:
                    if o.active == False: break
                    eat_item_score = o.get_score()
                    o.change_active()
                else :
                    eat_item_score = item_table[type(o)]
                    objects[i].remove(o)
                    del o
                eat_effect.enter(playerchar.x, playerchar.y)
            static_objects_group.change_score(eat_item_score)
            break
def clear():
    print("aa")
    for o in all_objects():
        del o
    objects.clear()

def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o

exit_pause_time = get_time()

def handle_events():
    global timestop,exit_pause_time,timestop_exit,loop
    if timestop == True:
        for event in get_events():
            if event.type == SDL_KEYDOWN and event.key == SDLK_p:
                exit_pause_time = get_time()
                timestop_exit = True
            if event.type == SDL_QUIT:
                loop = False
        exit_pause()


def exit_pause():
    global timestop_exit,timestop
    if timestop_exit == True:
        if get_time() - exit_pause_time > 3.0:
            timestop_exit = False
            timestop = False
        elif get_time() - exit_pause_time > 2.0:
            clear_canvas()
            draw()
            static_objects_group.count_pause_time_image.clip_draw(190, 0, 95, 114, playerchar.x+30, playerchar.y + 100)
            update_canvas()
        elif get_time() - exit_pause_time > 1.0:
            clear_canvas()
            draw()
            static_objects_group.count_pause_time_image.clip_draw(95,0,95,114,playerchar.x+10,playerchar.y + 100)
            update_canvas()
        elif get_time() - exit_pause_time < 1.0:
            clear_canvas()
            draw()
            static_objects_group.count_pause_time_image.clip_draw(0, 0, 95, 114, playerchar.x-10, playerchar.y + 100)
            update_canvas()
def init(obj,layer):
    add_object(obj,layer)

def enter():
    global  playerchar, grass_01,grass_02 , medicine , stage1,current_time,coins,obstacle_,stage1_sequence,grass_03,attack_ball
    playerchar = player.Player()
    grass_01 = grass.Grass(431)
    grass_02 = grass.Grass(862)
    grass_03 = grass.Grass(1293)
    medicine = item.Medicine()
    obstacle_ = obstacle.Obstacle_line()
    current_time = time.time()
    coins = [item.Coin() for i in range(10)]
    init(medicine,0)
    init(grass_01,1)
    init(grass_02,1)
    init(grass_03,1)
    for i in range(10):
        init(coins[i],0)
    init(obstacle_,1)
    static_objects_group.enter()

    stage1_sequence = stage01.Stage01()

    attack_ball = ball.Ball()
def move_update(obj):
    global slow_start
    if slow_start == True:        #충돌시 객체들은 느려짐
        global slow_speed_start
        if get_time() - slow_speed_start > 0.5:
            slow_start = False
            return
        elif get_time() - slow_speed_start < 0.1:
            obj.x -= obj.velocity * frame_time / 2
        elif get_time() - slow_speed_start < 0.2:
            obj.x -= obj.velocity * frame_time / 3
        elif get_time() - slow_speed_start < 0.3:
            obj.x -= obj.velocity * frame_time / 4
        elif get_time() - slow_speed_start < 0.4:
            obj.x -= obj.velocity * frame_time / 3
        elif get_time() - slow_speed_start < 0.5:
            obj.x -= obj.velocity * frame_time / 2
    elif playerchar.running == False:
        obj.x -= obj.velocity * frame_time
    else:
        obj.x -= obj.velocity * frame_time * 2

new_coin_time = get_time()
def update():
    global frame_time, current_time,coins,new_coin_time
    playerchar.update()
    playerchar.cooltime()
    for i in range(10) :
        if coins[i].active == False and get_time() - new_coin_time > 0.2:
            new_coin_time = get_time()
            coins[i].enter()
            coins[i].change_active()
            break
    for o in all_objects():
        o.update()
    for o in all_objects():
        if playerchar.get_bb(o):
            remove_object(o)
    stage1_sequence.update()
    stage1_sequence.collision(playerchar)
    eat_effect.update()
    frame_time = time.time() - current_time
    current_time += frame_time
    print(eat_effect.active)


def draw():
    if timestop == False:
        clear_canvas()
    static_objects_group.draw()
    for o in all_objects():
        o.draw()
    playerchar.draw()
    stage1_sequence.draw()
    eat_effect.draw()
    if drawbb == True:
        for o in all_objects():
            draw_rectangle(*o.get_bb())
        stage1_sequence.draw_bb()
        playerchar.draw_bb()
    if timestop == False:
        update_canvas()

def exit():
    global playerchar
    del(playerchar)
    for o in all_objects():
        del(o)
    for o in static_objects_group.all_static_objects():
        del(o)
    objects.clear()
    static_objects_group.static_objects.clear()

def main():
    global current_time, playerchar
    enter()
    while loop:
        handle_events()
        stage1_sequence.do()
        if timestop:
            current_time = time.time()
        if timestop == False:
            update()
            draw()
        playerchar.handle_events()
        delay(0.04)
    exit()



if __name__  == '__main__':
    main()