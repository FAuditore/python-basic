from datastructures.list import ranks, suits


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
for c in ('%s %s' % (r, s) for r in ranks for s in suits if r < '3'):
    print(c)
# 2 spades
# 2 diamonds
# 2 clubs
# 2 hearts
# 10 spades
# ...

generList = list(i ** 2 for i in range(5))
# [0, 1, 4, 9, 16]
