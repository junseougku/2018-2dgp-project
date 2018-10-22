from pico2d import *

import player
import grass

playerchar = player.Player()
grass_01 = grass.Grass()

def handle_events():
    global running
    global  jump
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
            close_canvas()

        if (event.type ,event.key) == (SDL_KEYDOWN,SDLK_x):
            jump = True
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_DOWN):
            pass

running = True
jump = False
def run():
    global running
    while running:
        clear_canvas()
        playerchar.update()

        grass_01.update()
        if jump:
            playerchar.jump()
        grass_01.draw()
        playerchar.draw()

        update_canvas()
        handle_events()
        delay(0.05)