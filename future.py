# Future类的实例都表示可能已经完成或者尚未完成的延迟计算
# future 封装待完成的操作, 可以放入队列, 完成的状态可以查询, 得到结果(或抛出异常)后可以获取结果(或异常)
# CPython 解释器本身就不是线程安全的, 因此有全局解释器锁(GIL), 一次只允许使用一个线程执行 Python 字节码
# 因此, 一个 Python 进程通常不能同时使用多个 CPU 核心
# 标准库中所有执行阻塞型 I/O 操作的函数, 在等待操作系统返回结果时都会释放 GIL
import time
from concurrent import futures


def long_time_job(t):
    time.sleep(t)
    return t


def do_many():
    # futures.ThreadPoolExecutor(max_workers, thread_name_prefix,initializer, initargs)
    # max_workers: 可用的最大线程数量
    # 使用工作的线程数实例化ThreadPoolExecutor类
    # executor.__exit__方法会调用executor.shutdown(wait=True)在所有线程都执行完毕前阻塞线程
    # ProcessPoolExecutor()默认使用os.cpu_count()返回的CPU数量
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        # map 方法返回一个迭代器
        # 迭代器的 __next__ 方 法调用各个 future 的 result 方法
        # 返回结果的顺序与调用顺序一致
        res = executor.map(long_time_job, reversed(list(range(5))))
        l = []
        for t in range(0, 5):
            # executor.submit(fn, /, *args, **kwargs))创建future
            future = executor.submit(long_time_job, t / 10)
            l.append(future)
            print(future)
            # <Future at 0x104828b10 state=finished returned float>
            # <Future at 0x104829410 state=pending> pending:等待有线程可用
            # <Future at 0x104828c10 state=pending>
            # <Future at 0x104829610 state=pending>
            # <Future at 0x104829750 state=pending>

        # futures.as_completed((fs, timeout=None))等待一批future结束的迭代器
        for future in futures.as_completed(l):
            # future.result返回future的结果, 会阻塞, 可设置超时
            print(future.result(), end=', ')  # 0.0, 0.1, 0.2, 0.3, 0.4,
    return list(res)


def main(do_many):
    t0 = time.time()
    res = do_many()
    elapsed = time.time() - t0
    msg = '\n{} in {:.2f}s'
    print(msg.format(res, elapsed))


main(do_many)  # [4, 3, 2, 1, 0] in 4.01s
