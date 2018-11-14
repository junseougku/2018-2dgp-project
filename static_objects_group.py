from pico2d import *
import HP
import score
static_objects = [ [],[]]       #ui 배경등 의미가없는 객체들
sky_stage1 = None
background = None
background2 =None
stage1 = None
count_pause_time_image = None
hp_ui = None
score_ui = None

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

def enter():
    global sky_stage1, stage1,background2,background1,count_pause_time_image,hp_ui,score_ui
    stage1 = load_image("image\\stage_1.png")
    sky_stage1 = load_image("image\\stage_sky_1.png")
    background1 = load_image("image\\stage_background_1.png")
    background2 = load_image("image\\stage_background_2.png")
    count_pause_time_image = load_image("image\\count_pause_time_.png")
    static_object_init(stage1, 0)
    static_object_init(background1, 0)
    static_object_init(background2, 0)
    static_object_init(count_pause_time_image, 1)
    hp_ui = HP.HP()
    score_ui = score.score()
    static_object_init(hp_ui,1)
    static_object_init(score_ui,1)

def draw():
    global hp_ui,score_ui
    static_object_draw(sky_stage1, 400, 270)
    static_object_draw(stage1, 400, 180)
    static_object_draw(background2, 400, 450)
    hp_ui.draw()
    score_ui.draw()

def change_score(_point):
    score_ui.update(_point)