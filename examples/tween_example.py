from picosystem import *
from tween import Tween, linear
from extras import delta, anon

rd = anon("RenderData", {"x": 8, "y": 8, "w": 8, "h": 8})

tween = (
    Tween(500, rd, {"x": 32, "y": 32, "w": 16, "h": 16}, linear)
    .then(500, rd, {"x": 64, "y": 64, "w": 8, "h": 8}, linear)
    .then(500, rd, {"x": 64, "y": 8, "w": 8, "h": 8}, linear)
    .then(500, rd, {"x": 32, "y": 32, "w": 16, "h": 16}, linear)
    .then(500, rd, {"x": 8, "y": 64, "w": 8, "h": 8}, linear)
    .then(500, rd, {"x": 8, "y": 8, "w": 8, "h": 8}, linear)
    .on_start(lambda: print("Started Tween"))
    .on_finish(lambda: print("Finished Tween"))
)


def update(tick: int):
    global tween
    cur_delta = delta()
    if pressed(A):
        tween.start()

    if not tween is None:
        tween.update(cur_delta)


def draw(tick: int):
    pen(0, 0, 0)
    clear()
    sprite(0, rd.x, rd.y, 1, 1, rd.w, rd.h)


start()
