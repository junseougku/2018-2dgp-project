from pico2d import *
import time
import player
import grass

playerchar = player.Player()
grass_01 = grass.Grass()

frame_time = 0.0
running = True
timestop = False


def handle_events():
    global timestop
    if timestop == True:
        for event in get_events():
            if event.type == SDL_KEYDOWN and event.key == SDLK_p:
                timestop = False
def run():
    global running
    global frame_time
    global timestop
    current_time = time.time()
    while running:
        handle_events()
        if timestop == True:
            continue
        clear_canvas()
        playerchar.update()
        grass_01.update()


        grass_01.draw()
        playerchar.draw()

        update_canvas()
        playerchar.handle_events()
        frame_time = time.time() - current_time
        current_time += frame_time

        delay(0.05)
