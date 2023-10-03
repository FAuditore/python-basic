# asyncio 提供一组 高层级 API 用于:
#     并发地 运行 Python 协程并对其执行过程实现完全控制
#     执行 网络 IO 和 IPC
#     控制 子进程
#     通过队列 实现分布式任务
#     同步 并发代码
# 还有一些 低层级 API 以支持库和框架的开发者实现
#     创建和管理事件循环, 以提供异步 API 用于网络化, 运行子进程, 处理OS信号等等
#     使用 transports 实现高效率协议
#     通过 async/await 语法桥接基于回调的库和代码

import asyncio
import time


# 通过 async/await 语法来声明协程
# 调用一个协程不会使其被调度执行
async def hello(t=1):
    print('Hello ...', end=' ')

    # 可等待对象: 可以在await语句中使用的对象
    # 可等待对象有三种主要类型: 协程,任务和Future
    #     协程函数: 定义形式为 async def 的函数
    #     协程对象: 调用 协程函数 所返回的对象
    #     任务: 被用来“并行的”调度协程 通过 asyncio.create_task() 等函数封装为一个任务
    #     Futures: 一种特殊的低层级可等待对象, 表示一个异步操作的最终结果
    # asyncio.sleep(delay, result=None) 阻塞 delay 指定的秒数
    # sleep总是会挂起当前任务, delay设置为0可以允许其他任务执行
    await asyncio.sleep(t)
    print('... World!')
    return t


# asyncio.run(coro, *, debug=None)
# 执行coroutine并返回结果
# 此函数会运行传入的协程, 负责管理 asyncio 事件循环, 终结异步生成器, 并关闭线程池
asyncio.run(hello())


# started at 09:28:29
# Hello ... ... World!
# finished at 09:28:30


async def create_task():
    # asyncio.create_task(coro, *, name=None, context=None)
    # 创建任务, 用来并发运行作为asyncio任务的多个协程
    # 将 coro 协程 封装为一个 Task 并调度其执行, 返回 Task 对象
    # name 任务名称
    # context 允许指定自定义的 contextvars.Context 供coro运行
    # 该任务会在 get_running_loop() 返回的循环中执行
    task1 = asyncio.create_task(hello(1))
    task2 = asyncio.create_task(hello(2))

    # 重要 保存一个指向此函数的结果的引用, 以避免任务在执行过程中消失
    # 事件循环将只保留对任务的弱引用
    # 未在其他地方被引用的任务可能在任何时候被作为垃圾回收, 即使是在它被完成之前
    # 如果需要可靠的“发射后不用管”后台任务, 请将它们放到一个多项集中
    task_set = {task1, task2}

    # add_done_callback(callback, *, context=None)
    # 添加一个回调, 将在Task对象完成时被运行
    # 完成后移除 callback第一个传入参数是task本身
    task1.add_done_callback(task_set.discard)
    task2.add_done_callback(task_set.discard)

    print(f"started at {time.strftime('%X')}")
    # 等待全部结束
    await task1
    await task2
    print(f"finished at {time.strftime('%X')}")


# asyncio.run(create_task())
# started at 09:31:06
# Hello ... Hello ... ... World!
# ... World!
# finished at 09:31:08


async def task_group():
    # asyncio.TaskGroup 类提供了 create_task() 的更现代化的替代
    # await由上下文管理器提供
    async with asyncio.TaskGroup() as tg:
        task1 = tg.create_task(hello(1))
        task2 = tg.create_task(hello(2))
        print(f"started at {time.strftime('%X')}")
    print(f"finished at {time.strftime('%X')}")


# asyncio.run(task_group())
# started at 10:37:41
# Hello ... Hello ... ... World!
# ... World!
# finished at 10:37:43


async def concurrent():
    # awaitable asyncio.gather(*aws, return_exceptions=False)
    # 并发运行 aws 序列中的可等待对象,返回一个由返回值聚合成的列表, 结果顺序一致
    # return_exceptions False:首个异常会立即传播给等待 gather() 的任务 其他任务继续
    # return_exceptions True:异常和成功结果一样处理, 合并至结果列表
    L = asyncio.gather(
            hello(1),
            hello(2),
            hello(3),
            return_exceptions=True
    )

    # asyncio.shield(aw)
    # 保护一个可等待对象防止其被取消
    # task = asyncio.create_task(something())
    # res = await shield(task)
    # 等价于 await something() 不同之处在于shield不会被取消
    res = await asyncio.shield(L)
    print(res)


# asyncio.run(concurrent())  # [1, 2, 3]


async def timeout():
    try:
        # asyncio.timeout(delay)
        # 返回一个可被用于限制等待某个操作所耗费时间的异步上下文管理器。
        # asyncio.timeout_at(when) when 是停止等待的绝对时间
        async with asyncio.timeout(1):
            await hello()
        # asyncio.wait_for(aw, timeout)
        # 等待aw可等待对象完成, 指定 timeout 秒数后超时
        await asyncio.wait_for(hello(999), 1)
    except TimeoutError:
        print("The long operation timed out, but we've handled it.")


# asyncio.run(timeout())  # The long operation timed out, but we've handled it

# 简单等待

async def simple_wait():
    task1 = asyncio.create_task(hello(1))
    task2 = asyncio.create_task(hello(2))

    # asyncio.wait(aws, *, timeout=None, return_when=ALL_COMPLETED)
    # 并发地运行aws可迭代对象中的Future和Task实例并进入阻塞状态直到满足return_when所指定的条件
    # 返回两个 Task/Future 集合: (done, pending)
    done, pending = await asyncio.wait([task1, task2], return_when=asyncio.FIRST_COMPLETED)
    print(done, pending)
    # {<Task finished name='Task-5' coro=<hello() done, defined at python-basic/async.py:18> result=1>}
    # {<Task pending name='Task-6' coro=<hello() running at python-basic/async.py:29>
    # wait_for=<Future pending cb=[Task.task_wakeup()]>>}

    # asyncio.as_completed(aws, *, timeout=None)
    # 并发地运行可迭代对象 aws 中的可等待对象。
    # 返回一个产生协程的迭代器, 所返回的每个协程可被等待以从剩余的可等待对象的可迭代对象中获得早最的下一个结果
    for coro in asyncio.as_completed([task1, task2]):
        res = await coro
        print(res)  # 1 2


asyncio.run(simple_wait())

# class asyncio.Runner(*, debug=None, loop_factory=None)上下文管理器
# loop_factory 可被用来重载循环的创建
with asyncio.Runner() as runner:
    # run(coro, *, context=None) 运行一个协程
    # context允许指定一个自定义contextvars.Context用作coro运行所在的上下文
    runner.run(hello())
    runner.get_loop()  # 返回嵌入的事件循环
    runner.close()  # 关闭运行器

# TBD
