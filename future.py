# CPython 解释器本身就不是线程安全的, 因此有全局解释器锁(GIL), 一次只允许使用一个线程执行 Python 字节码
# 因此, 一个 Python 进程通常不能同时使用多个 CPU 核心
# 标准库中所有执行阻塞型 I/O 操作的函数, 在等待操作系统返回结果时都会释放 GIL
import contextlib
import math
import time

# Future类的实例都表示可能已经完成或者尚未完成的延迟计算
# concurrent.futures 模块提供异步执行可调用对象高层接口
from concurrent import futures


# class concurrent.futures.Executor 抽象类提供异步执行调用方法, 通过子类调用
# 异步执行可以由 ThreadPoolExecutor 使用线程或由 ProcessPoolExecutor 使用单独的进程来实现
def do_many():
    # futures.ThreadPoolExecutor(max_workers, thread_name_prefix, initializer, initargs)
    # 使用线程池异步执行调用
    # max_workers: 可用的最大线程数量, 使用工作的线程数实例化ThreadPoolExecutor类
    # 3.8 版更改: max_workers 的默认值已改为 min(32, os.cpu_count() + 4)
    # initializer: 每个工作者线程开始处调用的一个可选可调用对象
    # initargs: 传递给initializer的元组参数
    # executor.__exit__方法会调用executor.shutdown(wait=True)在所有线程都执行完毕前阻塞线程
    with futures.ThreadPoolExecutor(max_workers=3) as executor:
        future_list = []
        for t in range(0, 5):
            # executor.submit(fn, /, *args, **kwargs))
            # 以 fn(*args, **kwargs) 方式执行并返回一个代表该可调用对象的执行的 Future 对象
            future = executor.submit(long_time_job, t / 10)
            future_list.append(future)
            print(future)
            # <Future at 0x104828b10 state=finished returned float>
            # <Future at 0x104829410 state=pending> pending:等待有线程可用
            # <Future at 0x104828c10 state=pending>
            # <Future at 0x104829610 state=pending>
            # <Future at 0x104829750 state=pending>

        # futures.as_completed(fs, timeout=None)
        # 返回一个在一批future结束时产生的future对象的迭代器, 阻塞
        for future in futures.as_completed(future_list):
            # future.result(timeout=None)
            # 返回future的结果, 阻塞
            print(future.result(), end=', ')  # 0.0, 0.1, 0.2, 0.3, 0.4,

        # concurrent.futures.wait(fs, timeout=None, return_when=ALL_COMPLETED)
        # 等待fs指定的future对象返回
        # 常量
        # FIRST_COMPLETED 函数将在任意可等待对象结束或取消时返回
        # FIRST_EXCEPTION 函数将在任意可等待对象因引发异常而结束时返回, 当没有引发任何异常时它就相当于 ALL_COMPLETED
        # ALL_COMPLETED 函数将在所有可等待对象结束或取消时返回
        # 返回一个由集合组成的具名 2 元组
        # 第一个集合的名称为 done, 第二个集合的名称为 not_done
        done, not_done = futures.wait(future_list, return_when=futures.ALL_COMPLETED)
        print(done, not_done)
        # {<Future at 0x10440e050 state=finished returned float>,
        # <Future at 0x10440e4d0 state=finished returned float>,
        # <Future at 0x104297550 state=finished returned float>,
        # <Future at 0x10440e350 state=finished returned float>,
        # <Future at 0x10440e790 state=finished returned float>}
        # set()

        # map 类似于 map(func, *iterables) 函数
        # iterables 是立即执行而不是延迟执行的
        # func 是异步执行的，对 func 的多个调用可以并发执行
        # 迭代器的 __next__ 方 法调用各个 future 的 result 方法
        # 返回结果的顺序与调用顺序一致
        res = executor.map(long_time_job, reversed(list(range(5))))

    return list(res)


def long_time_job(t):
    time.sleep(t)
    return t


# ProcessPoolExecutor 会使用 multiprocessing 模块
# 这允许它绕过全局解释器锁GIL但也意味着只可以处理和返回可封存的对象
# ProcessPoolExecutor 不可以工作在交互式解释器中
def do_by_processes():
    # futures.ProcessPoolExecutor(max_workers, mp_context, initializer, initargs, max_tasks_per_child)
    # 使用进程池异步执行调用
    # max_workers: 进程池中进程数量
    # max_workers是 None 或未给出, 则默认为机器上的处理器数量
    # initializer: 是一个可选的可调用对象, 它会在每个工作进程启动时被调用
    # initargs是传给initializer的参数元组
    # max_tasks_per_child: 是指定单个进程在其退出并替换为新工作进程之前可以执行的最大任务数量
    with futures.ProcessPoolExecutor(max_workers=3) as executor:
        for n, res in zip(PRIMES, executor.map(is_prime, PRIMES)):
            print('%d is prime: %s' % (n, res))
            # 112272535095293 is prime: True
            # 112582705942171 is prime: True
            # 112272535095293 is prime: True
            # 115280095190773 is prime: True
            # 115797848077099 is prime: True
            # 1099726899285419 is prime: False


PRIMES = [
    112272535095293,
    112582705942171,
    112272535095293,
    115280095190773,
    115797848077099,
    1099726899285419]


def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    sqrt_n = int(math.floor(math.sqrt(n)))
    for i in range(3, sqrt_n + 1, 2):
        if n % i == 0:
            return False
    return True


# class concurrent.futures.Future 将可调用对象封装为异步执行
def future_object():
    executor = futures.ThreadPoolExecutor(max_workers=1)

    # Future 实例由 Executor.submit() 创建
    future = executor.submit(long_time_job, 3)

    # cancel() 尝试取消调用
    # 如果调用正在执行或已结束运行返回False, 否则调用会被取消并且该方法将返回True
    print(future.cancel())  # False

    # running() 如果调用正在执行而且不能被取消那么返回
    print(future.running())  # True

    # done() 如果调用已被取消或正常结束那么返回
    print(future.done())  # False

    # result(timeout=None)返回调用所返回的值
    # 如果调用尚未完成则此方法将等待至多timeout秒
    # 如果调用在 timeout 秒内仍未完成，则将引发TimeoutError
    with contextlib.suppress(TimeoutError):
        print(future.result(timeout=0.5))

    # exception(timeout=None) 返回调用所引发的异常
    # 如果调用尚未完成则此方法将等待至多timeout秒
    print(future.exception())  # None

    # add_done_callback(fn) 附加可调用fn到future对象
    # 当future对象被取消或完成运行时, 将会调用fn, 而这个future对象将作为它唯一的参数
    future.add_done_callback(lambda x: print(x))
    # <Future at 0x102ef33d0 state=finished returned int>


def main(f):
    t0 = time.time()
    res = f()
    elapsed = time.time() - t0
    msg = '\n{} return {} in {:.2f}s'
    print(msg.format(f.__name__, res, elapsed))


if __name__ == '__main__':
    main(do_many)  # do_many return [4, 3, 2, 1, 0] in 4.51s
    main(do_by_processes)  # do_by_processes return None in 0.38s
    main(future_object)  # future_object return None in 3.01s
