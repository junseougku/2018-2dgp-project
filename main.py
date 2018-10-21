from pico2d import *

open_canvas()

running = True

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
            close_canvas()

while running:
    handle_events()
    delay(0.05)
