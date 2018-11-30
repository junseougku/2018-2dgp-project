from pico2d import *
import mygame


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            mygame.loop = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            mygame.loop = False
        elif (event.type ,event.key) == (SDL_KEYDOWN,SDLK_SPACE):
            next_state()
running =True
start_time = get_time()
logo_image = load_image("image\\kpu_credit.png")
def enter():
    pass


def run():
    global  running,logo_image,start_time
    enter()
    while running:
        clear_canvas()
        logo_image.draw(400,300)
        update_canvas()
        handle_events()
        if get_time() - start_time > 1.0:
            next_state()
            del(logo_image)

def next_state():
    global running
    running = False

