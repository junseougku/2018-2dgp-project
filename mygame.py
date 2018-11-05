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
running = True
timestop = False

stage1 = None

objects = [[],[]]
def add_object(o,layer):
    objects[layer].append(o)

def remove_object(o):
    for i in range(len(objects)):
        if i == 1:
            break
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break
def clear():
    for o in all_objects():
        del o
    objects.clear()

def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o




def handle_events():
    global timestop
    if timestop == True:
        for event in get_events():
            if event.type == SDL_KEYDOWN and event.key == SDLK_p:
                timestop = False

def init(obj,layer):
    add_object(obj,layer)

def enter():
    global  playerchar, grass_01,grass_02 , medicine , stage1,current_time,silver_coin,obstacle_01
    playerchar = player.Player()
    grass_01 = grass.Grass(431)
    grass_02 = grass.Grass(1293)
    medicine = item.Medicine()
    stage1 = load_image("image\\stage_1.png")
    obstacle_01 = obstacle.Obstacle()
    current_time = time.time()
    silver_coin = item.SilverCoin()
    init(medicine,0)
    init(grass_01,0)
    init(grass_02,0)
    init(silver_coin,0)
    add_object(obstacle_01,1)



def move_update(obj):
    obj.x -= obj.velocity * frame_time

def update():
    global frame_time, current_time
    playerchar.update()
    for o in all_objects():
        o.update()
    for o in all_objects():
        if playerchar.get_bb(o):
            print("remove")
            remove_object(o)
    frame_time = time.time() - current_time
    current_time += frame_time

def draw():
    clear_canvas()
    stage1.draw(400, 180)
    for o in all_objects():
        o.draw()
    playerchar.draw()
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
    while running:
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