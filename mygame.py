from pico2d import *

import player
import grass

playerchar = player.Player()
grass_01 = grass.Grass()


running = True
jumpheight = 0
def run():
    global running
    global  jumpheight
    while running:
        clear_canvas()
        playerchar.update()

        grass_01.update()
        if player.jump:
            playerchar.jump(jumpheight)
            jumpheight += 2
        grass_01.draw()
        playerchar.draw()

        update_canvas()
        playerchar.handle_events()
        delay(0.05)