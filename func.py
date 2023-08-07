from functools import reduce, partial


def my_sum(a, b):
    return a + b


def my_div(a, b):
    return a / b


def f_default(age, name='abc'):
    print('name=' + name + ' age=' + str(age))


def f_keyword_only(*, a, b):
    """
        仅限关键字参数, 可变参后面参数都是关键字参数(无默认值则不可省略)
    """
    pass


def f_pos_only(a, b, /, *args):
    """
        仅限位置参数, /前参数按位置传递
    """
    ...


f_default(15)  # name = 'abc'
f_default(1, name='z')  # name == 'z'
print(f_default.__defaults__)  # ('abc',)
print(f_default.__code__.co_argcount)  # 2
print(f_default.__code__.co_varnames)  # ('age', 'name')

f_keyword_only(a=1, b=2)
# f_keyword_only(1, 2)
# TypeError: f_keyword_only() takes 0 positional arguments but 2 were given

f_pos_only(1, 2, 3)


# f_pos_only(b=1, a=1)
# TypeError: f_pos_only() got some positional-only arguments passed as keyword arguments: 'a, b'


def fact(n):
    return 1 if n <= 1 else n * fact(n - 1)


# lambda 生成匿名函数
# filter(function_or_None, iterable) 对迭代器过滤 返回结果为True的元素的生成器
# map(func, *iterables) 对每个迭代对象func 返回生成器
# sum(*args, **kwargs) 对迭代器求和
sum(map(fact, filter(lambda n: n % 2, range(0, 10))))  # fact(1)+fact(3)+fact(5)+fact(7)+fact(9)

# all(iterable) 迭代器全为真返回True 空集返回True
# any(iterable) 迭代器任一为真返回True 空集返回False
print(all([True, 1, 'a', 0]))  # False
print(any([True, 1, 'a', 0]))  # True

# functools.reduce(function, iterable[, initial]) 将函数作用到序列上
reduce(lambda x, y: x + y, range(0, 100))  # ((...(0+1)+2)+3)...+99)

# partial(func, /, *args, **keywords) 固定函数某些参数
new_div = partial(my_div, 100)
print(list(map(new_div, range(1, 5))))  # [100.0, 50.0, 33.333333333333336, 25.0]

# zip(iterable, ..., strict:bool) 将多个可迭代对象打包成一个个元组 返回一个生成器
# zip(range(3), 'abcdef', strict=True))  # ValueError: zip() argument 2 is longer than argument 1
print(list(zip(range(3), 'abcdef')))  # [(0, 'a'), (1, 'b'), (2, 'c')]


# function object
class FuncObject:
    def __call__(self, a=None, b=None, *args, **kwargs):
        print('I was called', a, b, args, kwargs)


m = FuncObject()
print(callable(m))  # True
m(123)
print(m.__dir__())  # ['__module__', '__call__', '__dict__', '__weakref__', '__doc__', '__new__',...]


# annotations 注解
# 每个参数后增加 :注解表达式(类型或字符串)
# -> 返回值注解
def anno_func(age: 'should more than 0', name: str = 'abc') -> str:
    return str(name) + str(age)


print(anno_func(-1, 2))  # 2-1 类型不匹配仅提示,不强制
print(anno_func.__annotations__)  # {'age': 'should more than 0', 'name': <class 'str'>, 'return': <class 'str'>}
