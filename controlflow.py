# if
x = -5
if x < 0:
    x = 0
    print('<0')
elif x == 0:
    print(0)
else:
    print('no')

seasons = ['Spring', 'Summer', 'Fall', 'Winter']

# range
# class range(start, stop[, step])
# range 类型相比常规 list 或 tuple 的优势在于一个 range 对象总是占用固定数量的（较小）内存
print(list(range(0, 30, 5)))  # [0, 5, 10, 15, 20, 25]
print(11 in range(0, 20, 2))  # False
print(range(0, 20, 2)[-1])  # 18

# loop
# for 或 while 循环可以包括 else 子句
# 在 for 循环中, else 子句会在循环成功结束最后一次迭代之后执行
# 在 while 循环中, 它会在循环条件变为假值后执行
# break 提前终止循环, 不会执行else
for n in range(2, 10):
    if n % 11 == 0:
        print('found')
        break
else:
    print('over')


# yield
# Python函数定义体中有yield关键字, 该函数就是生成器函数
# 调用该函数会返回一个生成器对象
# 每次在生成器上调用next()时, 它会从上次离开的位置恢复执行(它会记住上次执行语句时的所有数据值)
def get_number():
    print('get 1', end=' ')
    yield 1
    print('get 2', end=' ')
    yield 2
    print('get 10', end=' ')
    yield 10
    print('over')


print(type(get_number()))  # <class 'generator'>

for number in get_number():
    print(number)
# get 1 1
# get 2 2
# get 10 10
# over 最后一次调用next, 运行最后的所有代码, 然后抛出StopIteration异常

# (expr) 生成器表达式
# 语法类似列表推导, 外层为圆括号
print(sum(i * i for i in range(10)))  # 285

# enumerate(iterable, start=0)
# 返回一个枚举对象
# iterable必须是一个序列,或 iterator, 或其他支持迭代的对象
# enumerate()返回的迭代器的 __next__()方法返回一个元组, 里面包含一个计数值和通过迭代 iterable 获得的值
print(list(enumerate(seasons, start=5)))  # [(5, 'Spring'), (6, 'Summer'), (7, 'Fall'), (8, 'Winter')]


# pass
# 不执行任何动作
def wait_interrupt():
    while True:
        pass


class MyEmptyClass:
    pass


# match
# 接受一个表达式并把它的值与一个或多个 case 块给出的一系列模式进行比较
# 只有第一个匹配的模式会被执行, 并且它还可以提取值的组成部分（序列的元素或对象的属性）赋给变量
def http_error(status):
    match status:
        case 400:
            print('Bad request')
        case 401 | 402 | 403:
            print('Not allowed')
        case 404:
            print('Not found')
        case _:  # _ 被作为通配符并必定会匹配成功
            print('Other code')


# 属性捕获到变量
def point_match(p):
    match p:
        case (0, 0):
            print('Origin')
        case (0, y):
            print(f'Y={y}')
        case (x, 0):
            print(f'X={x}')
        case (x, y):
            print(f'X={x} Y={y}')
        case _:
            print('Not a point')


point_match((0, 5))  # Y=5
point_match((5, 0))  # X=5
point_match((5, 5))  # X=5 Y=5
point_match(None)  # Not a point


# 类中设置 __match_args__ 特殊属性来为模式中的属性定义一个专门的位置
class Point:
    __match_args__ = ('x', 'y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


def point_match(p):
    match p:
        case Point(0, 0) as p:  # 子模式可使用 as 关键字来捕获
            print(f'Origin {p}')
        case [Point(x, 0), Point(0, y)]:  # 捕获列表
            print(f'i={x} j = {y}')
        case Point(x, y) if x == y:  # 约束项 约束项为假则继续匹配下一个case
            print(f'Y=X={x}')
        case _:
            print("Something else")


point_match(Point(0, 0))  # Origin <__main__.Point object at 0x10079a390>
point_match([Point(1, 0), Point(0, 2)])  # i=1 j = 2
point_match(Point(1, 1))  # Y=X=1
point_match(None)  # Something else
