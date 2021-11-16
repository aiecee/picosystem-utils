from picosystem import *
import animation

sprite_sheet = Buffer(128, 128)
open("s4m_ur4i-pirate-characters.16bpp", "rb").readinto(sprite_sheet)

anim = animation.Animation(
    sprite_sheet, [(0, 0), (1, 1000), (2, 1000), (3, 1000), (4, 1000)])

playing = False


def update(tick: int):
    global anim, playing
    if pressed(A):
        if playing:
            anim.stop()
            playing = False
        else:
            anim.play(animation.LOOP)
            playing = True
    elif pressed(B):
        if playing:
            anim.stop()
            playing = False
        else:
            anim.play(animation.ONCE)
            playing = True


def draw(tick: int):
    global anim
    pen(0, 0, 0)
    clear()
    anim.draw(20, 20)


start()
