import contextlib
import functools
import inspect


def simple_coroutine():
    print('start')
    x = yield
    print('received:', x)


m = simple_coroutine()
next(m)  # start 启动协程

# send 方法的参数会成为暂停的 yield 表达式的值
# send之后协程恢复, 运行至下一个yield或终止抛出StopIteration
with contextlib.suppress(StopIteration):
    m.send(123)  # received: 123


# 协程可以身处四个状态中的一个, 当前状态可以使用 inspect.getgeneratorstate(...)函数确定
# 'GEN_CREATED' 等待开始执行
# 'GEN_RUNNING' 解释器正在执行
# 'GEN_SUSPENDED' 在 yield 表达式处暂停
# 'GEN_CLOSED' 执行结束
# yield右边的值会在next时产出, 左边会在收到值后赋值
def co2():
    a = 14
    b = yield a  # 产出a 等待接收b
    c = yield a + b  # 产出a+b 等待接收c
    print(f'receive c: {c}')


m = co2()

print(inspect.getgeneratorstate(m))  # GEN_CREATED

print(next(m))  # 14
print(inspect.getgeneratorstate(m))  # GEN_SUSPENDED

print(m.send(123))  # 137
print(inspect.getgeneratorstate(m))  # GEN_SUSPENDED

with contextlib.suppress(StopIteration):
    m.send(1)  # receive c: 1
print(inspect.getgeneratorstate(m))  # GEN_CLOSED


# 预激活装饰器 相当于创建完后调用了一次next
def auto_active(func):
    @functools.wraps(func)
    def primer(*args, **kwargs):
        gen = func(*args, **kwargs)
        next(gen)
        return gen

    return primer


@auto_active
def auto_coroutine():
    yield 1
    yield 2
    yield 3


a = auto_coroutine()
print(inspect.getgeneratorstate(a))  # GEN_SUSPENDED
print(next(a))  # 2
print(next(a))  # 3


# 终止协程
# 显式把异常发给协程
# 如果生成器处理了抛出的异常,  代码会向前执行到下一个 yield 表达式, 而产出的值会成为调用 generator.throw 方法得到的返回值
# 如果生成器没有处理抛出的异常, 异常会向上冒泡, 传到调用方的上下文中

class MyExc(Exception): ...


def exc_handling():
    try:
        while True:
            try:
                x = yield
            except MyExc:
                print('MyExc handled, continuing...')
            else:
                print('received x: {!r}'.format(x))
    finally:
        print('coroutine ending')
        return 99999


e = exc_handling()
next(e)
e.send(11)  # received x: 11

# generator.throw(exc_type[, exc_value[, traceback]])
# 致使生成器在暂停的 yield 表达式处抛出指定的异常
e.throw(MyExc)  # MyExc handled, continuing...
# e.throw(ZeroDivisionError) 如果无法处理传入异常, 协程会终止 coroutine ending

# generator.close()
# 致使生成器在暂停的 yield 表达式处抛出 GeneratorExit 异常
e.close()  # coroutine ending
print(inspect.getgeneratorstate(e))  # GEN_CLOSED


# 如果协程有return语句返回值, 生成器抛出StopIteration异常, 异常对象的value属性保存着返回的值
def return_coroutine():
    x = yield
    return x + 1


r = return_coroutine()
try:
    next(r)
    r.send(123)
except StopIteration as e:
    print(e.value)  # 124


# 委派生成器 yield from

# 子生成器, 收到空时退出
def coroutine_worker():
    ans = 0
    while True:
        x = yield
        if not x:
            break
        ans += x
    return ans


# 一个委派生成器使用yield from调用一个子生成器
# 子生成器可以执行 return 语句, 返回一个值, 而返回的值会成为 yield from 表达式的值
def appoint(result):
    while True:
        # 每次循环新建一个worker实例,发送的每个值都会由yield from处理,传给该实例
        ans = yield from coroutine_worker()
        result.append(ans)


# 任何yield from链条都必须由客户驱动, 在最外层委派生成器上调用next(...)函数或.send(...)方法
# 可以隐式调用, 例如使用 for 循环
def client():
    a = appoint(l := [])
    next(a)
    # 会直接把值传给子生成器
    a.send(1)
    a.send(3)
    a.send(None)
    a.send(5)
    a.send(5)
    a.send(None)
    print(l)


client()  # [4,10]
