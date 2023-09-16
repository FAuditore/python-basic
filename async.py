# asyncio 提供一组 高层级 API 用于:
#     并发地 运行 Python 协程并对其执行过程实现完全控制
#     执行 网络 IO 和 IPC
#     控制 子进程
#     通过队列 实现分布式任务
#     同步 并发代码
import asyncio

# 还有一些 低层级 API 以支持库和框架的开发者实现
#     创建和管理事件循环，以提供异步 API 用于网络化, 运行子进程，处理OS信号等等
#     使用 transports 实现高效率协议
#     通过 async/await 语法桥接基于回调的库和代码

async def main():
    print('Hello ...')
    await asyncio.sleep(0.5)
    print('... World!')


# asyncio.run(coro, *, debug=None) 执行coroutine并返回结果
# 此函数会运行传入的协程, 负责管理 asyncio 事件循环, 终结异步生成器, 并关闭线程池
asyncio.run(main())
# Hello ...
# ... World!


# class asyncio.Runner(*, debug=None, loop_factory=None)上下文管理器
# loop_factory 可被用来重载循环的创建
# with asyncio.Runner() as runner:

# TBD
