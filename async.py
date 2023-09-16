import asyncio

import itertools
import random
import sys
import time


class Signal:
    signal = True


@asyncio.coroutine
def spin(msg):
    write, flush = sys.stdout.write, sys.stdout.flush
    for char in itertools.cycle('|/-\\'):
        status = char + ' ' + msg
        write(status)
        flush()
        write('\x08' * len(status))  # 退格符移回光标
        try:
            yield from asyncio.sleep(.1)
        except asyncio.CancelledError:
            break
    write(' ' * len(status) + '\x08' * len(status))


@asyncio.coroutine
def slow_job():
    t = random.randrange(1, 5) / 2
    yield from asyncio.sleep(t)
    return t


@asyncio.coroutine
def supervisor():
    spinner = asyncio.as(spin('thinking!'))


supervisor()
