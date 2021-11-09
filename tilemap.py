from picosystem import *


class TileMap:

    def __init__(self, w: int, h: int, ss: Buffer, x: int = 0, y: int = 0, scale: float = 1):
        self.w = w
        self.h = h
        self.ss = ss
        self.x = x
        self.y = y
        self.scale = scale
        self.map = [0] * (w * h)
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
                sprite(self.get(x, y), x * 8, y * 8)

        blend()
        spritesheet()
        target()
        self.dirty = False

    def draw(self):
        if self.dirty:
            self.re_render()

        blit(self.b, 0, 0, self.w * 8, self.h * 8, self.x,
             self.y, round((self.w * 8) * self.scale), round((self.h * 8) * self.scale))
