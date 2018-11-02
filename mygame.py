from pico2d import *

import player
import grass

playerchar = player.Player()
grass_01 = grass.Grass()


running = True
def run():
    global running
    while running:
        clear_canvas()
        playerchar.update()
        grass_01.update()


        grass_01.draw()
        playerchar.draw()

        update_canvas()
        playerchar.handle_events()
        delay(0.05)