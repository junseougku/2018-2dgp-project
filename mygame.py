from pico2d import *
import time
import player
import grass
import item
import obstacle

playerchar = None
grass_01 = None
grass_02 = None
medicine = None
silver_coin = None
obstacle_01 = None


PIXEL_PER_METER = (10.0/ 0.3)
GRASS_SPEED = 20.0
GRASS_SPEED_MPM = (GRASS_SPEED * 1000.0 / 60.0)
GRASS_SPEED_MPS = (GRASS_SPEED_MPM / 60.0)
GRASS_SPEED_PPS = (GRASS_SPEED_MPS * PIXEL_PER_METER)

frame_time = 0.0
loop = True
timestop = False
timestop_exit = False
drawbb =True
stage1 = None
sky_stage1 = None
background = None
background2 =None
count_pause_time_image = None
objects = [[],[]]       #움직이고 없어질수 있는 객체들
static_objects = [ [],[]]       #ui 배경등 의미가없는 객체들
def add_object(o,layer):
    objects[layer].append(o)

def add_static_object(o,layer):
    static_objects[layer].append(o)

def remove_object(o):
    for i in range(len(objects)):
        if i == 1 and playerchar.blink == False:
            playerchar.cooltime_enter()
            playerchar.change_state(player.Wound)
            print("collsion")
            break
        if o in objects[i]:
            if i == 1: break
            print("remove")
            objects[i].remove(o)
            del o
            break
def clear():
    for o in all_objects():
        del o
    objects.clear()
    for o in all_static_objects():
        del o
    static_objects.clear()

def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o

def all_static_objects():
    for i in range(len(static_objects)):
        for o in static_objects[i]:
            yield o

exit_pause_time = get_time()

def handle_events():
    global timestop,exit_pause_time,timestop_exit
    if timestop == True:
        for event in get_events():
            if event.type == SDL_KEYDOWN and event.key == SDLK_p:
                exit_pause_time = get_time()
                timestop_exit = True
        exit_pause()


def exit_pause():
    global timestop_exit,timestop
    if timestop_exit == True:
        if get_time() - exit_pause_time > 3.0:
            timestop_exit = False
            timestop = False
        elif get_time() - exit_pause_time > 2.0:
            count_pause_time_image.clip_draw(190, 0, 95, 114, playerchar.x, playerchar.y + 100)
            update_canvas()
        elif get_time() - exit_pause_time > 1.0:
            count_pause_time_image.clip_draw(95,0,95,114,playerchar.x,playerchar.y + 100)
            update_canvas()
        elif get_time() - exit_pause_time < 1.0:
            count_pause_time_image.clip_draw(0, 0, 95, 114, playerchar.x, playerchar.y + 100)
            update_canvas()

def init(obj,layer):
    add_object(obj,layer)

def static_object_init(obj,layer):
    add_static_object(obj,layer)

def enter():
    global  playerchar, grass_01,grass_02 , medicine , stage1,current_time,silver_coin,obstacle_01,sky_stage1,background1,background2
    global count_pause_time_image
    playerchar = player.Player()
    grass_01 = grass.Grass(431)
    grass_02 = grass.Grass(1293)
    medicine = item.Medicine()
    stage1 = load_image("image\\stage_1.png")
    sky_stage1 = load_image("image\\stage_sky_1.png")
    background1 = load_image("image\\stage_background_1.png")
    background2 = load_image("image\\stage_background_2.png")
    count_pause_time_image = load_image("image\\count_pause_time_.png")
    obstacle_01 = obstacle.Obstacle()
    current_time = time.time()
    silver_coin = item.SilverCoin()
    init(medicine,0)
    init(grass_01,0)
    init(grass_02,0)
    init(silver_coin,0)
    add_object(obstacle_01,1)
    static_object_init(stage1,0)
    static_object_init(background1,0)
    static_object_init(background2,0)
    static_object_init(count_pause_time_image,1)


def move_update(obj):
    if playerchar.running == False:
        obj.x -= obj.velocity * frame_time
    else:
        obj.x -= obj.velocity * frame_time * 2

def depth_machine():
    pass

def update():
    global frame_time, current_time
    playerchar.update()
    playerchar.cooltime()
    for o in all_objects():
        o.update()
    for o in all_objects():
        if playerchar.get_bb(o):
            remove_object(o)
    frame_time = time.time() - current_time
    current_time += frame_time

def static_object_draw(obj,_x,_y):
    obj.draw(_x,_y)

#뎁스를 하다말음
def draw():
    clear_canvas()
    static_object_draw(sky_stage1,400,270)
    static_object_draw(stage1,400,180)
    static_object_draw(background2,400,450)
    for o in all_objects():
        o.draw()
    playerchar.draw()
    if drawbb == True:
        for o in all_objects():
            draw_rectangle(*o.get_bb())
    update_canvas()

def exit():
    global grass_01,grass_02,playerchar,medicine
    del(playerchar)
    for o in all_objects():
        del(o)
    close_canvas()

def main():
    global current_time, playerchar
    enter()
    while loop:
        handle_events()
        if timestop == True:
            current_time = time.time()
            continue
        update()
        draw()
        playerchar.handle_events()
        delay(0.05)
    exit()
if __name__  == '__main__':
    main()