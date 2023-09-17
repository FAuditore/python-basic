# dict 字典
# {key:value}
# 可散列类型: str bytes 数值
#     要求实现 __hash__(self) 方法和 __eq__(self, other) 方法
#     如果两个可散列对象相等,那么它们散列值相同
#     即 x == y 同时意味着 x is y 且 hash(x) == hash(y)
#     元组所有元素都可散列时元组才可散列
from collections import Counter, UserDict, defaultdict

a = dict(one=1, two=2, three=3)
b = {'one': 1, 'two': 2, 'three': 3}
c = dict(zip(['one', 'two', 'three'], (1, 2, 3)))  # zip 生成元组组合 [('one',1),('two',2)('three',3)]
d = dict([('two', 2), ('one', 1), ('three', 3)])

# dict comprehension 字典推导
d = {k: v for k, v in zip('abc', (1, 2, 3))}
print(d)  # {'a': 1, 'b': 2, 'c': 3}

print(list(d))  # 返回所有键的列表 ['a', 'b', 'c']

# d[k] <==> d.__getitem__(k) 若k不存在,生成KeyError
d.__getitem__('c')  # 3

# d.get(k) 若k存在返回v,若k不存在,返回default值(默认为None)
d.get('d', 10)  # 10

# d[k]=v <==> d.__setitem__(k,v)
d.__setitem__('c', 4)  # d->{'a': 1, 'b': 2, 'c': 4}
d.update(c=5)  # d->{'a': 1, 'b': 2, 'c': 5}
d.update({'a': 10, 'b': 9, 'c': 8})  # d->{'a': 10, 'b': 9, 'c': 8}

# d.setdefault(k,v) 如果k存在,返回v 如果k不存在,设置为v并返回
print(d.setdefault('f', 100))  # 100 d->{'a': 1, 'b': 2, 'c': 4, 'f': 100}

# 字典遍历
for k, v in d.items():
    pass

for k in d.keys():  # keys()可省略 默认按key遍历
    pass

for v in d.values():
    pass

# defaultdict 若k在字典中不存在,会调用default_factory生成v加入字典
dd = defaultdict(list)  # defaultdict(default_factory=list)
print(dd)  # defaultdict(<class 'list'>, {})
print(dd['a'])  # []
print(dd)  # defaultdict(<class 'list'>, {'a': []})


# d.__missing__()
# 仅在d.__getitem__()找不到k时调用 (d[k]) 对get或__contains__ (in)没有影响
class MyDict(UserDict):
    def __missing__(self, key):
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]  # warning: 可能会无限递归


# counter 计数器
c = Counter('hello world')
print(c)  # Counter({'l': 3, 'o': 2, 'h': 1, 'e': 1, ' ': 1, 'w': 1, 'r': 1, 'd': 1})
print(c.most_common(3))  # [('l', 3), ('o', 2), ('h', 1)]
print(sorted(c))  # [' ', 'd', 'e', 'h', 'l', 'o', 'r', 'w'] 展示所有不重复元素 等价于sorted(set('hello world'))
print(c['o'])  # 2

# Python3.9字典合并(|)和更新(|=)运算符
print(d1 := dict(zip('abc', [1, 2, 3])))  # {'a': 1, 'b': 2, 'c': 3}
print(d2 := dict(zip('cde', [3, 4, 5])))  # {'c': 3, 'd': 4, 'e': 5}
print(d1 | d2)  # {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
d2['c'] = 100
d1 |= d2
print(d1)  # {'a': 1, 'b': 2, 'c': 100, 'd': 4, 'e': 5}
