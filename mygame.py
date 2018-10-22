from pico2d import *

import player
import grass

playerchar = player.Player()
grass_01 = grass.Grass()

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
            close_canvas()
        if (event.type ,event.key) == (SDL_KEYDOWN,SDLK_x):
            playerchar.jump()
        elif (event.type,event.key) == (SDL_KEYDOWN,SDLK_DOWN):
            pass

running = True
def run():
    while running:
        clear_canvas()
        handle_events()
        playerchar.update()

        grass_01.update()
        grass_01.draw()
        playerchar.draw()

        update_canvas()
        delay(0.05)
