import time


def anon(name: str, data):
    return type(name, (object,), data)


__last_delta = 0


def delta() -> int:
    global __last_delta
    current_time = time.ticks_ms()
    old_time = __last_delta
    delta = current_time - __last_delta
    if old_time == 0:
        __last_delta = current_time
        return 1
    __last_delta = current_time
    return delta
