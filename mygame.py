from pico2d import *
import time
import player
import grass
import item
import obstacle
import static_objects_group
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


item_table = {
    item.SilverCoin : 5,
    item.Medicine : 10
}

objects = [[],[]]       #움직이고 없어질수 있는 객체들
def add_object(o,layer):
    objects[layer].append(o)

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

            if type(o) in item_table:
                eat_item_score = item_table[type(o)]
                static_objects_group.change_score(eat_item_score)
            objects[i].remove(o)
            del o
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
    global  playerchar, grass_01,grass_02 , medicine , stage1,current_time,silver_coin,obstacle_01
    playerchar = player.Player()
    grass_01 = grass.Grass(431)
    grass_02 = grass.Grass(1293)
    medicine = item.Medicine()
    obstacle_01 = obstacle.Obstacle()
    current_time = time.time()
    silver_coin = item.SilverCoin()
    init(medicine,0)
    init(grass_01,0)
    init(grass_02,0)
    init(silver_coin,0)
    init(obstacle_01,1)
    static_objects_group.enter()


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


def draw():
    if timestop == False:
        clear_canvas()
    static_objects_group.draw()
    for o in all_objects():
        o.draw()
    playerchar.draw()
    if drawbb == True:
        for o in all_objects():
            draw_rectangle(*o.get_bb())
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
        if timestop:
            current_time = time.time()
        if timestop == False:
            update()
            draw()
        playerchar.handle_events()
        delay(0.05)
    exit()



if __name__  == '__main__':
    main()