# asyncio 提供一组 高层级 API 用于:
#     并发地 运行 Python 协程并对其执行过程实现完全控制
#     执行 网络 IO 和 IPC
#     控制 子进程
#     通过队列 实现分布式任务
#     同步 并发代码

# 还有一些 低层级 API 以支持库和框架的开发者实现
#     创建和管理事件循环，以提供异步 API 用于网络化, 运行子进程，处理OS信号等等
#     使用 transports 实现高效率协议
#     通过 async/await 语法桥接基于回调的库和代码

import asyncio

import itertools
import random
import sys


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

# TODO not finish
