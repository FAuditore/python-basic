# 所有生成器都是迭代器, 因为生成器完全实现了迭代器接口
# 迭代器用于从集合中取出元素;而生成器用于“凭空”生成元素
import itertools
import operator
import random
import re
import reprlib

RE_WORD = re.compile('\w+')


class Sentence:
    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        print(f'getitem {index}', end=' ')
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        # 默认情况下, reprlib.repr 函数生成的字符串最多有 30 个字符
        return 'Sentence(%s)' % reprlib.repr(self.text)


s = Sentence('hello world !')
print(s.words)  # ['hello', 'world']

# 解释器需要迭代对象 x 时, 会自动调用 iter(x)
# (1) 检查对象是否实现了 __iter__ 方法, 如果实现了就调用它, 获取一个迭代器
# (2) 如果没有实现 __iter__ 方法, 但是实现了 __getitem__ 方法, Python会创建一个迭代器, 尝试按顺序(从索引 0 开始)获取元素
# (3) 如果尝试失败, Python 抛出 TypeError 异常, 通常会提示“C object is not iterable”

import collections.abc

print(isinstance(s, collections.abc.Iterable))  # False <==> '__iter__' in Foo.__dict__

for w in s:
    print(w, end=' ')  # getitem 0 hello getitem 1 world getitem 2


class Foo:
    def __iter__(self):
        pass


print(issubclass(Foo, collections.abc.Iterable))  # True

# 【可迭代对象】有__iter__方法, 每次实例化一个新的迭代器
# 【迭代器】要实现 __next__ 方法, 返回单个元素. 此外还要实现__iter__方法, 返回迭代器本身
# 迭代器Iterator是这样的对象:
#     实现了无参数的 __next__ 方法, 返回序列中的下一个元素
#     如果没有元素了, 那么抛出 StopIteration 异常
#     Python中的迭代器还实现了__iter__方法(返回self本身), 因此迭代器也可以迭代

# Lib/_collections_abc.py
# class Iterator(Iterable):
#
#     __slots__ = ()
#
#     @abstractmethod
#     def __next__(self):
#         'Return the next item from the iterator. When exhausted, raise StopIteration'
#         raise StopIteration
#
#     def __iter__(self):
#         return self
print(issubclass(Foo, collections.abc.Iterator))  # False <==> '__next__' in Foo.__dict__

# for w in s 的等价写法
it = iter(s)  # __iter__返回self(获取一个迭代器)
while True:
    try:
        print(next(it))  # __next__ 返回下一个可用元素, 如果没有则抛出StopIteration
    except StopIteration:  # StopIteration表明迭代器结束
        del it
        break

# iter传入两个参数, 第一个参数必须是可调用的对象, 用于不断调用(没有参数)
# 产出各个值第二个值是哨符, 当可调用的对象返回这个值时, 触发迭代器抛出StopIteration异常, 不输出哨符
print(list(iter(lambda: random.randint(1, 6), 2)))  # [6, 1, 5] 随机投骰直到出现2


# 函数中包含关键字yield的函数是生成器函数
# 调用生成器函数返回一个生成器
# 生成器是迭代器, 调用next(g)会获取yield生成的下一个元素
def gen_tuple():
    for i in zip(range(3), 'abc'):
        yield i


g = gen_tuple()  # 返回一个生成器对象
print(g)  # <generator object gen_tuple at 0x10484d0e0>
print(next(g))  # (0, 'a')
print(next(g))  # (1, 'b')
print(next(g))  # (2, 'c'）


# print(next(g))  StopIteration
# 生成器函数执行完毕后生成器对象会抛出StopIteration异常

# yield from it
def gen_args(*args):
    for it in args:
        # yield from 加上可迭代对象会逐个产出元素
        yield from it


g = gen_args([1, 2, 3], range(5))
print(list(g))  # [1, 2, 3, 0, 1, 2, 3, 4]


class LazySentence:
    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return 'Sentence(%s)' % reprlib.repr(self.text)

    def __iter__(self):
        # 惰性版本,不会立刻构建列表
        # finditer 函数构建一个迭代器, 包含self.text中匹配RE_WORD的单词, 产出MatchObject实例
        # match.group()从MatchObject实例中提取匹配正则表达式的具体文本
        # 使用生成器表达式或yield构建生成器, 然后将其返回
        return (match.group() for match in RE_WORD.finditer(self.text))


# itertools模块
# itertools.count函数返回的生成器能生成多个数
# 等价于
# def count(firstval=0, step=1):
#     x = firstval
#     while 1:
#         yield x
#         x += step
g = itertools.count(1, .5)
print(next(g))  # 1
print(next(g))  # 1.5

# itertools.takewhile(predicate, it) 指定条件为False时抛出StopIteration
g = itertools.takewhile(lambda n: n < 3, itertools.count(1, 1))
print(list(g))  # [1, 2]


def vowel(c):
    return c.lower() in 'aeiou'


# 用于过滤的生成器函数
s = 'Aardvark'

# filter(function_or_None, iterable) 对迭代器过滤 返回结果为True的元素的生成器
print(list(filter(vowel, s)))  # ['A', 'a', 'a']

# itertools.filterfalse(predicate, it) predicate 返回假值时产出对应的元素
print(list(itertools.filterfalse(vowel, s)))  # ['r', 'd', 'v', 'r', 'k']

# itertools.compress(it, selector_it)
# 并行处理两个可迭代的对象;如果 selector_it 中的元素是真值, 产出 it 中对应的元素
print(list(itertools.compress(s, [1, 0, 1, 0, 1, 0, 1, 0, 1, 0])))  # ['A', 'r', 'v', 'r']

# itertools.dropwhile(predicate, it) 跳过 predicate 的计算结果为真值的元素, 然后产出剩下的各个元素(不再进一步检查)
print(list(itertools.dropwhile(vowel, s)))  # ['r', 'd', 'v', 'a', 'r', 'k']

# itertools.islice(it, stop)或islice(it, start, stop, step=1)
# 作用类似于s[:stop]或s[start:stop:step], 不过it可以是任何可迭代的对象, 而且这个函数实现的是惰性操作
print(list(itertools.islice(s, 4, 7, 2)))  # ['v', 'r']

# 用于映射的生成器函数
l = [12, 432, 14, 234, 124, 12, 4151]

# enumerate(iterable, start=0)产出由两个元素组成的元组
# 结构是(index, item), 其中 index 从 start 开始计数, item 则从 iterable 中获取
print(list(enumerate(l[:5], start=1)))  # [(1, 12), (2, 432), (3, 14), (4, 234), (5, 124)]

# map(func, it1, [it2, ..., itN])把 it中的各个元素传给func,产出结果
# 如果传入N个可迭代的对象, 那么 func 必须能接受 N 个参数, 而且要并行处理各个可迭代的对象
print(sum(map(abs, [1, -5, 2, -8])))  # 16
print(list(map(operator.mul, range(11), [2, 4, 8])))  # [0, 4, 16]

# itertools.accumulate(it, [func])产出累积的总和
# 如果提供了func, 那么把前两个元素传给它, 然后把计算结果和下一个元素传给它, 以此类推
print(list(itertools.accumulate(l)))  # [12, 444, 458, 692, 816, 828, 4979]
print(list(itertools.accumulate(l, min)))  # [12, 12, 12, 12, 12, 12, 12]
print(list(itertools.accumulate(l, max)))  # [12, 432, 432, 432, 432, 432, 4151]
print(list(itertools.accumulate(l[:5], operator.mul)))  # [12, 5184, 72576, 16982784, 2105865216]

# itertools.starmap(func, it)把 it 中的各个元素传给 func, 产出结果
# 输入的可迭代对象应该产出可迭代的元素iit, 然后对每个迭代元素调用func(*iit)
print(list(itertools.starmap(operator.mul, enumerate(s, 1))))
# ['A', 'aa', 'rrr', 'dddd', 'vvvvv', 'aaaaaa', 'rrrrrrr', 'kkkkkkkk']

# 合并多个可迭代对象的生成器函数

# zip(it1, ..., itN)并行从输入的各个可迭代对象中获取元素,产出由 N 个元素组成的元组
print(list(zip('abc', [1, 2, 3, 4])))  # [('a', 1), ('b', 2), ('c', 3)]

# itertools.zip_longest(it1, ..., itN, fillvalue=None)与zip类似
# 等到最长的可迭代对象到头后才停止, 空缺的值使用 fillvalue 填充
print(list(itertools.zip_longest('abcd', [1, 2], fillvalue='?')))  # [('a', 1), ('b', 2), ('c', '?'), ('d', '?')]

# itertools.chain(it1, ..., itN)先产出 it1 中的所有元素, 然后产出 it2 中的所有元素, 以此类推
print(list(itertools.chain('ABC', range(2))))  # ['A', 'B', 'C', 0, 1]

# itertools.chain.from_iterable(it)产出it生成的各个可迭代对象中的元素, 一个接一个, 无缝连接在一起
print(list(itertools.chain.from_iterable(enumerate(enumerate('ABC')))))
# [0, (0, 'A'), 1, (1, 'B'), 2, (2, 'C')]

# itertools.product(it1, ..., itN, repeat=1)计算笛卡儿积
# 从输入的各个可迭代对象中获取元素, 合并成由 N 个元素组成的元组, 与嵌套的 for 循环效果一样;
# repeat指明重复处理多少次输入的可迭代对象
print(list(itertools.product('abc', [1, 2])))  # [('a', 1), ('a', 2), ('b', 1), ('b', 2), ('c', 1), ('c', 2)]

# 把输入的各个元素扩展成多个输出元素的生成器函数
# itertools.count(start=0, step=1)从 start 开始不断产出数字, 按 step 指定的步幅增加
ct = itertools.count(1, 2)
print(next(ct))  # 1
print(next(ct))  # 3

# itertools.cycle(it)按顺序重复不断地产出各个元素
cy = itertools.cycle('ABC')
print(list(itertools.islice(cy, 5)))  # ['A', 'B', 'C', 'A', 'B']

# itertools.repeat(item, [times])重复不断地产出指定的元素,除非提供 times
print(list(itertools.repeat(1, 2)))  # [1, 1]

# itertools.combinations(it, out_len) 把it产出的out_len个元素组合然后产出
# itertools.combinations_with_re placement 组合包含相同元素
print(list(itertools.combinations('ABC', 2)))  # [('A', 'B'), ('A', 'C'), ('B', 'C')]

# itertools. permutations(it, out_len=None) 把out_len个it产出的元素排列然后产出
print(list(itertools.permutations('ABC', 2)))
# [('A', 'B'), ('A', 'C'), ('B', 'A'), ('B', 'C'), ('C', 'A'), ('C', 'B')]

# 用于重新排列元素的生成器函数
# reversed(seq)从后向前, 倒序产出seq中的元素
# seq必须是序列或者是实现了 __reversed__ 特殊方法的对象
print(list(reversed('abc')))  # ['c', 'b', 'a']

# itertools.groupby(it, key=None)产出由两个元素组成的元素, 形式为(key, group)
# 其中key是分组标准, group 是生成器, 用于产出分组里的元素
for k, g in itertools.groupby('LLLLAAGGG'):
    print(k, g)
# L <itertools._grouper object at 0x102c05900>
# A <itertools._grouper object at 0x102c059f0>
# G <itertools._grouper object at 0x102c05900>

animals = ['rat', 'bat', 'duck', 'bear', 'lion', 'eagle', 'shark', 'giraffe', 'dolphin']
for k, g in itertools.groupby(animals, len):
    print(k, list(g))
# 3 ['rat', 'bat']
# 4 ['duck', 'bear', 'lion']
# 5 ['eagle', 'shark']
# 7 ['giraffe', 'dolphin']


# itertools.tee(it, n=2)产出一个由n个生成器组成的元组, 产生的生成器可单独使用
g1, g2 = itertools.tee('ABC')
print(list(g1))  # ['A', 'B', 'C']
print(list(g2))  # ['A', 'B', 'C']
