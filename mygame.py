from pico2d import *
import time
import player
import grass
import item

playerchar = None
grass_01 = None
medicine = None

frame_time = 0.0
running = True
timestop = False

stage1 = None

def handle_events():
    global timestop
    if timestop == True:
        for event in get_events():
            if event.type == SDL_KEYDOWN and event.key == SDLK_p:
                timestop = False

def enter():
    global  playerchar, grass_01 , medicine , stage1,current_time
    playerchar = player.Player()
    grass_01 = grass.Grass()
    medicine = item.Medicine()
    stage1 = load_image("image\\stage_1.png")
    current_time = time.time()

def update():
    global frame_time, current_time
    playerchar.update()
    grass_01.update()
    medicine.update()
    playerchar.handle_events()
    frame_time = time.time() - current_time
    current_time += frame_time

def draw():
    clear_canvas()
    stage1.draw(400, 180)
    grass_01.draw()
    medicine.draw()
    playerchar.draw()
    update_canvas()

def exit():
    global grass_01,playerchar,medicine
    del(grass_01)
    del(playerchar)
    del(medicine)
    
def main():
    enter()
    while running:
        handle_events()
        if timestop == True:
            current_time = time.time()
            continue
        update()
        draw()
        delay(0.05)
    exit()

if __name__  == '__main__':
    main()