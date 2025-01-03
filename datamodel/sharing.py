# Python 唯一支持的参数传递模式是共享传参 (call by sharing)
# 在调用函数时会将实际参数(实参)引入到被调用函数的局部符号表中
# 实参是使用按值调用来传递的(其中的值始终是对象的引用而不是对象的值)
# 各个形式参数获得实参中各个引用的副本, 函数内部形参是实参的别名(id相同)

# 这意味着, 函数可能会修改通过参数传入的可变对象
# 这一行为无法避免, 除非在本地创建副本, 或者使用不可变对象（例如传入元组, 而不传入列表）

def f(x):
    return id(x)


a = 100.0
print(id(a) == f(a))  # True


def modify(x):
    x[0] = 8
    return x


t = [1, 2, 3]
print(t, modify(t))  # [8, 2, 3] [8, 2, 3]


# t = (1, 2, 3)
# print(t, modify(t)) # TypeError: 'tuple' object does not support item assignment

def modify2(x):
    x = (4, 5)  # x指向新的对象了
    return x


t = (1, 2, 3)
print(t, modify2(t))  # (4, 5) (1, 2, 3)
t = [1, 2, 3]
print(t, modify2(t))  # (4, 5) [1, 2, 3]


def make_copy(m):
    print(id(m), end=' ')
    m = list(m)  # 使用构造方法创建副本
    print(id(m))


l = [1, 2, 3]
print(id(l))  # 4367786816
make_copy(l)  # 4367786816 4367978176


# 不要使用可变类型做默认值
# 默认值在函数定义时计算(加载模块时), 默认值变成了函数对象的属性
# 默认值只计算一次. 默认值为列表、字典或类实例等可变对象时, 会产生与该规则不同的结果
def h(l1=[]):
    l1.append(3)
    print(l1)


h()  # [3]
h()  # [3, 3] 累积了后续调用时传递的参数


# 正确方式
def h(l1=None):
    if l1 is None:
        l1 = []
    l1.append(3)
    print(l1)


h()  # [3]
h()  # [3]
