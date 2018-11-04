from pico2d import *
import time
import player
import grass
import item

playerchar = None
grass_01 = None
grass_02 = None
medicine = None
silver_coin = None

PIXEL_PER_METER = (10.0/ 0.3)
GRASS_SPEED = 20.0
GRASS_SPEED_MPM = (GRASS_SPEED * 1000.0 / 60.0)
GRASS_SPEED_MPS = (GRASS_SPEED_MPM / 60.0)
GRASS_SPEED_PPS = (GRASS_SPEED_MPS * PIXEL_PER_METER)


frame_time = 0.0
running = True
timestop = False

stage1 = None

objects = [ [], []]

def add_object(o,layer):
    objects[layer].append(o)

def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o

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

def init(obj):
    add_object(obj,1)

def enter():
    global  playerchar, grass_01,grass_02 , medicine , stage1,current_time,silver_coin
    playerchar = player.Player()
    grass_01 = grass.Grass(431)
    grass_02 = grass.Grass(1293)
    medicine = item.Medicine()
    stage1 = load_image("image\\stage_1.png")
    current_time = time.time()
    silver_coin = item.SilverCoin()
    init(medicine)
    init(grass_01)
    init(grass_02)
    init(silver_coin)



def dyna_update(obj):
    obj.x -= obj.velocity * frame_time

def update():
    global frame_time, current_time
    playerchar.update()
    grass_01.update()
    grass_02.update()
    medicine.update()
    silver_coin.update()
    frame_time = time.time() - current_time
    current_time += frame_time

def draw():
    clear_canvas()
    stage1.draw(400, 180)
    grass_01.draw()
    grass_02.draw()
    medicine.draw()
    silver_coin.draw()
    playerchar.draw()
    update_canvas()

def exit():
    global grass_01,grass_02,playerchar,medicine
    del(grass_01)
    del(grass_02)
    del(playerchar)
    del(medicine)
    del(silver_coin)
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