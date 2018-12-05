from pico2d import *
import HP
import score
import background
static_objects = [ [],[]]       #ui 배경등 의미가없는 객체들
sky_stage1 = None

stage1 = None
count_pause_time_image = None
hp_ui = None
score_ui = None
first_background1 =None
first_background2 = None
first_background3 = None
def add_static_object(o,layer):
    static_objects[layer].append(o)

def all_static_objects():
    for i in range(len(static_objects)):
        for o in static_objects[i]:
            yield o

def clear():
    for o in all_static_objects():
        del o
    static_objects.clear()

def static_object_init(obj,layer):
    add_static_object(obj,layer)

def static_object_draw(obj,_x,_y):
    obj.draw(_x,_y)

def static_object_draw_noneposition(obj):
    obj.draw()

def init():
    score_ui.enter()
def enter():
    global sky_stage1, stage1,background1,count_pause_time_image,hp_ui,score_ui,first_background1,first_background2,first_background3
    stage1 = load_image("image\\stage_1.png")
    sky_stage1 = load_image("image\\stage_sky_1.png")
    background1 = load_image("image\\stage_background_1.png")

    count_pause_time_image = load_image("image\\count_pause_time_.png")
    first_background1 = background.Background(350)
    first_background2 = background.Background(1100)
    first_background3 = background.Background(1850)
    static_object_init(first_background1,0)
    static_object_init(first_background2, 0)
    static_object_init(first_background3, 0)
    static_object_init(stage1, 0)
    static_object_init(background1, 0)

    static_object_init(count_pause_time_image, 1)
    hp_ui = HP.HP()
    score_ui = score.score()
    static_object_init(hp_ui,1)
    static_object_init(score_ui,1)


def enter2():
    first_background1.init()
    first_background2.init()
    first_background3.init()
def draw():
    global hp_ui,score_ui
    static_object_draw(sky_stage1, 400, 270)
    static_object_draw(stage1, 400, 180)

    static_object_draw_noneposition(first_background1)
    static_object_draw_noneposition(first_background2)
    static_object_draw_noneposition(first_background3)
    hp_ui.draw()
    score_ui.draw()

def draw_2():
    global hp_ui, score_ui
    static_object_draw_noneposition(first_background1)
    static_object_draw_noneposition(first_background2)
    static_object_draw_noneposition(first_background3)
    hp_ui.draw()
    score_ui.draw()
def change_score(_point):
    score_ui.update(_point)

def update():
    static_object_update(first_background1)
    static_object_update(first_background2)
    static_object_update(first_background3)

def static_object_update(obj):
    obj.update()