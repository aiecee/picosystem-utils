from picosystem import *
import time

LOOP = 0
ONCE = 1


class Animation:

    def __init__(self, ss: Buffer, frames: list[tuple[int, int]]):
        self.ss = ss
        self.frames = frames
        self.last_ticks = 0
        self.state = -1
        self.current_frame = 0

    def play(self, state: int):
        self.last_ticks = time.ticks_ms()
        self.current_frame = 1
        self.state = state

    def stop(self):
        self.last_ticks = 0
        self.current_frame = 0
        self.state = -1

    def __idle(self, x: int, y: int):
        (frame, _) = self.frames[0]
        sprite(frame, x, y)

    def __loop(self, x: int, y: int):
        current_ticks = time.ticks_ms()
        elapsed_ticks = current_ticks - self.last_ticks
        (_, ticks) = self.frames[self.current_frame]
        if elapsed_ticks >= ticks:
            if self.current_frame + 1 == len(self.frames):
                self.current_frame = 1
            else:
                self.current_frame += 1
            self.last_ticks = current_ticks
        (frame, _) = self.frames[self.current_frame]
        sprite(frame, x, y)

    def __once(self, x: int, y: int):
        current_ticks = time.ticks_ms()
        elapsed_ticks = current_ticks - self.last_ticks
        (_, ticks) = self.frames[self.current_frame]
        if elapsed_ticks >= ticks:
            if self.current_frame + 1 == len(self.frames):
                self.stop()
                return
            else:
                self.current_frame += 1
            self.last_ticks = current_ticks
        (frame, _) = self.frames[self.current_frame]
        sprite(frame, x, y)

    def draw(self, x: int, y: int):
        spritesheet(self.ss)
        if self.state == -1:
            self.__idle(x, y)
        elif self.state == LOOP:
            self.__loop(x, y)
        elif self.state == ONCE:
            self.__once(x, y)
