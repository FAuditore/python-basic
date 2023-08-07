"""
    decorator 装饰器
    本质上是一个以函数为参数的闭包, 为函数添加功能 func = decorate(func)
    装饰器的包装在其他函数之前运行 包括main
    装饰器叠放执行顺序由内到外
        @d1
        @d2
        def f():
            ...
        等价于f = d1(d2(f))
"""
import functools
import time


def ExecTime(func):
    fmt = 'elapse: {:.6f}s func: {}({})'

    @functools.wraps(func)  # functools.wraps(func) 把相关属性复制到timer中, 抵消装饰器的副作用: 防止函数名等被timer覆盖
    def timer(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        print(fmt.format(float(elapsed), func.__name__, ','.join(str(arg) for arg in args)))
        return result

    return timer


@ExecTime
def original():
    for i in range(0, 10 ** 7):
        pass


original()
print(original.__code__.co_freevars)  # fmt func


@ExecTime
def fact(n):
    return 1 if n < 2 else fact(n - 1) + fact(n - 2)


fact(5)


# elapse: 0.000000s func: fact(1)
# elapse: 0.000000s func: fact(0)
# elapse: 0.000008s func: fact(2)
# elapse: 0.000000s func: fact(1)
# elapse: 0.000017s func: fact(3)
# elapse: 0.000000s func: fact(1)
# elapse: 0.000000s func: fact(0)
# elapse: 0.000006s func: fact(2)
# elapse: 0.000027s func: fact(4)
# elapse: 0.000000s func: fact(1)
# elapse: 0.000000s func: fact(0)
# elapse: 0.000005s func: fact(2)
# elapse: 0.000000s func: fact(1)
# elapse: 0.000009s func: fact(3)
# elapse: 0.000042s func: fact(5)


# functools.lru_cache 缓存函数最近运行的结果
# maxsize:缓存容量 typed:区分参数类型
# 需要保证函数参数是可散列值
@functools.lru_cache(maxsize=128, typed=False)
@ExecTime
def lru_fact(n):
    return 1 if n < 2 else lru_fact(n - 1) + lru_fact(n - 2)


lru_fact(5)


# elapse: 0.000000s func: lru_fact(1)
# elapse: 0.000000s func: lru_fact(0)
# elapse: 0.000006s func: lru_fact(2)
# elapse: 0.000009s func: lru_fact(3)
# elapse: 0.000012s func: lru_fact(4)
# elapse: 0.000014s func: lru_fact(5)


# generic function 泛函数
# functools.singledispatch 将一个函数转为泛函数 https://peps.python.org/pep-0443/
# 各个分派函数使用 @«base_function».register(«type») 装饰
# 如果同时有多个可分派函数,将执行分派在顺序上最后定义的函数
@functools.singledispatch
def origin_func(obj):
    print("unknown type: " + obj)


@origin_func.register(str)
def _(text):
    print("str: " + text)


@origin_func.register(int)
def _(n):
    print("int: " + str(n))


@origin_func.register
def _(l: list):
    print("list: " + ','.join(l))


def nothing(arg):
    print("None!")


# functional form 使用函数形式注册
origin_func.register(type(None), nothing)

origin_func(1)  # int: 1
origin_func('abc')  # str: abc
origin_func(None)  # None!
origin_func(['a', 'b', 'c'])  # list: a,b,c
print(origin_func.registry.keys())  # dict_keys([<class 'object'>, <class 'str'>, <class 'int'>, <class 'NoneType'>])


# decorator factory 装饰器工厂
# @factory(param) 等价于 func = factory(params)(func)
def decorator_factory(param='param'):  # 装饰器工厂,根据参数返回一个装饰器
    def gen_decorator(func):
        print(param, func.__name__)
        return func

    return gen_decorator


@decorator_factory('test factory')  # 使用工厂,@句法写为函数调用, 不再是装饰器名
def origin_func2():
    pass
# test factory origin_func2

