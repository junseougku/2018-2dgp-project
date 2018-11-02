from pico2d import *
import time
import player
import grass

playerchar = player.Player()
grass_01 = grass.Grass()

frame_time = 0.0
running = True
def run():
    global running
    global frame_time
    current_time = time.time()
    while running:
        clear_canvas()
        playerchar.update()
        grass_01.update()


        grass_01.draw()
        playerchar.draw()

        update_canvas()
        playerchar.handle_events()

        frame_time = time.time() - current_time
        frame_rate = 1.0 / frame_time
        current_time += frame_time
        delay(0.05)