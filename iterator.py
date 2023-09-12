# 所有生成器都是迭代器, 因为生成器完全实现了迭代器接口
# 迭代器用于从集合中取出元素;而生成器用于“凭空”生成元素
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
        # 默认情况下，reprlib.repr 函数生成的字符串最多有 30 个字符
        return 'Sentence(%s)' % reprlib.repr(self.text)


s = Sentence('hello world !')
print(s.words)  # ['hello', 'world']

# 解释器需要迭代对象 x 时, 会自动调用 iter(x)
# (1) 检查对象是否实现了 __iter__ 方法, 如果实现了就调用它, 获取一个迭代器
# (2) 如果没有实现 __iter__ 方法, 但是实现了 __getitem__ 方法, Python会创建一个迭代器, 尝试按顺序(从索引 0 开始)获取元素
# (3) 如果尝试失败, Python 抛出 TypeError 异常, 通常会提示“C object is not iterable”
import collections.abc

print(isinstance(s, collections.abc.Iterable))  # False


class Foo:
    def __iter__(self):
        pass


print(issubclass(Foo, collections.abc.Iterable))  # True <=> '__iter__' in Foo.__dict__

for w in s:
    print(w, end=' ')  # getitem 0 hello getitem 1 world getitem 2

# for w in s 的等价写法
it = iter(s)  # __iter__返回self
while True:
    try:
        print(next(it))  # __next__ 返回下一个可用元素, 如果没有则抛出StopIteration
    except StopIteration:  # StopIteration表明迭代器结束
        del it
        break
'''
# Lib/_collections_abc.py
class Iterator(Iterable):

    __slots__ = ()

    @abstractmethod
    def __next__(self):
        'Return the next item from the iterator. When exhausted, raise StopIteration'
        raise StopIteration

    def __iter__(self):
        return self
'''
