from picosystem import *
from tilemap import TileMap

sprite_sheet = Buffer(128, 128)
open("pirate-tilemap.16bpp", "rb").readinto(sprite_sheet)

tile_map = TileMap(15, 15, sprite_sheet)
tile_map.set(0, 0, 0)
tile_map.set(1, 1, 1)
tile_map.set(2, 2, 2)


def update(tick: int):
    pass


def draw(tick: int):
    global tile_map
    tile_map.draw(0, 0)


start()
