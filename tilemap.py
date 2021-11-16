from picosystem import *


class TileMap:

    def __init__(self, w: int, h: int, ss: Buffer, scale: float = 1):
        self.w = w
        self.h = h
        self.ss = ss
        self.scale = scale
        self.map = [-1] * (w * h)
        self.b = Buffer(w * 8, h * 8)
        self.dirty = True

    def set(self, sprite: int, x: int, y: int):
        self.map[x + self.w * y] = sprite
        self.dirty = True

    def get(self, x: int, y: int) -> int:
        return self.map[x + self.w * y]

    def re_render(self):
        target(self.b)
        spritesheet(self.ss)
        blend(COPY)
        clear()
        for y in range(self.h):
            for x in range(self.w):
                tile_index = self.get(x, y)
                if tile_index != -1:
                    sprite(tile_index, x * 8, y * 8)

        blend()
        spritesheet()
        target()
        self.dirty = False

    def draw(self, x: int, y: int):
        if self.dirty:
            self.re_render()

        blit(self.b, 0, 0, self.w * 8, self.h * 8, x,
             y, round((self.w * 8) * self.scale), round((self.h * 8) * self.scale))
