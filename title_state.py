from pico2d import *
import mygame


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            close_canvas()
        if (event.type ,event.key) == (SDL_KEYDOWN,SDLK_SPACE):
            next_state()
running =True

def enter():
    global  title_image
    title_image = load_image("image\\title.png")

def run():
    enter()
    while running:
        clear_canvas()
        handle_events()
        title_image.draw(400,300)
        update_canvas()

def next_state():
    mygame.main()