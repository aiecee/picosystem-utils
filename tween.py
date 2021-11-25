import math


def linear(x: float) -> float:
    return x


def quad_in(x: float) -> float:
    return x * x


def quad_out(x: float) -> float:
    return 1 - (1 - x) * (1 - x)


def cubic_in(x: float) -> float:
    return x * x * x


def cubic_out(x: float) -> float:
    return 1 - math.pow(1 - x, 3)


def quart_in(x: float) -> float:
    return x * x * x * x


def quart_out(x: float) -> float:
    return 1 - math.pow(1 - x, 4)


def sine_in(x: float) -> float:
    return 1 - math.cos((x * math.pi) / 2)


def sine_out(x: float) -> float:
    return -(math.cos(math.pi * x) - 1) / 2


def circ_in(x: float) -> float:
    return 1 - math.sqrt(1 - math.pow(x, 2))


def circ_out(x: float) -> float:
    return math.sqrt(1 - math.pow(x - 1, 2))


class __MorphData:
    def __init__(self, start, diff):
        self.start = start
        self.diff = diff


class Morph:

    def __init__(self, time: int, obj: object, variables: dict[str, int], easing):
        self.rate = time > 0 and 1 / time or 0
        self.progress = 0
        self.obj = obj
        self.delay = 0
        self.easing = easing
        self.variables = variables
        self.data: dict[str, __MorphData] = {}
        self.started = False
        self.completed = False

    def update(self, delta: int):
        if self.completed:
            return

        if self.delay > 0:
            self.delay -= delta
            return

        if not self.started:
            self.started = True
            for item in self.variables.items():
                start: int = getattr(self.obj, item[0])
                self.data[item[0]] = __MorphData(start, item[1] - start)

        self.progress = self.progress + self.rate * delta
        x = self.progress > 1 and 1 or self.easing(self.progress)
        for item in self.variables.items():
            target = item[0]
            prog = self.data[target]
            setattr(self.obj, target, round(prog.start + x * prog.diff))

        if self.progress > 1:
            self.completed = True


class Tween:

    def __init__(self, time: int, obj: object, variables: dict[str, int], easing):
        self.morphs: list[Morph] = [Morph(time, obj, variables, easing)]
        self.started = False
        self.completed = False

    def update(self, delta: int):
        if self.completed:
            return

        if not self.started:
            self.started = True

        if len(self.morphs) > 0:
            current = self.morphs[0]
            current.update(delta)
            if current.completed:
                self.morphs.remove(current)
        else:
            self.completed = True

    def then(self,  time: int, obj: object, variables: dict[str, int], easing):
        self.morphs.append(Morph(time, obj, variables, easing))
        return self
