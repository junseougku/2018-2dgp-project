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

title_image = load_image("image\\title.png")
def enter():
    pass

def run():
    global  running,title_image
    enter()
    while running:
        clear_canvas()
        title_image.draw(400,300)
        update_canvas()
        handle_events()
        if mygame.loop == False:
            running = False
            del(title_image)
def next_state():
    global space_down
    space_down = get_time()
    mygame.main()

space_down = get_time()