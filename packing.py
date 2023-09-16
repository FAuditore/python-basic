# *args: 无关键字参数 绑定到元组
# **kwargs: 关键字参数 绑定到字典
def f_args(name, *args, **kwargs):
    print('name = ' + str(name))
    print('type = ', type(args), 'args =', args)  # tuple
    print('type = ', type(kwargs), 'kwargs =', kwargs)  # dict


# unpack parameters
f_args('unpack', *['abc', 'bcd'], **{'a': 1, 'b': 2})  # name=unpack args=('abc', 'bcd') kwargs={'a': 1, 'b': 2}
f_args(*('a', 'b', 'c'))  # name='a' args=('b','c') kwargs={}

a, b, *c = range(5)
print(a, b, c)  # 0 1 [2, 3, 4]
a, *b, c = range(5)
print(a, b, c)  # 0 [1, 2, 3] 4

# generator expression 生成器表达式
# (expr)
# 不会一次性产生含所有值的列表,仅在需要时生成新元素,节省内存
for c in ('%s %s' % (r, s) for r in range(1, 10) for s in 'spades diamonds clubs hearts'.split() if r < 3):
    print(c)
# 1 spades
# 1 diamonds
# 1 clubs
# 1 hearts
# 2 spades
# 2 diamonds
# 2 clubs
# 2 hearts

generList = list(i ** 2 for i in range(5))
# [0, 1, 4, 9, 16]

# Python3.8 海象操作符 表达式同时赋值
print(n := list(range(5)))  # [0, 1, 4, 9, 16]
print(n)  # [0, 1, 2, 3, 4]
