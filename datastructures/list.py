# list 列表
# [element]
import random

l = ['2', '1', '3', '4'] + ['5']  # ['2', '1', '3', '4', '5']

del l[0]  # l->['1', '3', '4', '5']
l.reverse()  # l -> ['5', '4', '3', '1']

# 排序
newL = sorted(l)  # newL -> ['1', '3', '4', '5'] sorted可接受任意可迭代对象

# list.sort(*, key=None, reverse=False)
# 就地排序列表中的元素(稳定)
l.sort(reverse=False, key=int)  # l - > ['1', '3', '4', '5'] key=int(element)

l[2:4] = []  # l->['1', '3']

# list.append(x)
# 在列表末尾添加一个元素 a[len(a):] = [x]
l.append('1')  # l->['1', '3', '1']

# list.extend(iterable)
# 用可迭代对象的元素扩展列表 a[len(a):] = iterable
l.extend(range(3))  # l->['1', '3', '1', 0, 1, 2]

# list.remove(x)
# 从列表中删除第一个值为 x 的元素。未找到指定元素时触发 ValueError 异常
l.remove(0)  # l ->['1', '3', '1', 1, 2]

# 浅拷贝列表
l2 = l[:]
l3 = l2.copy()

# 修改不可变对象时会产生新的引用 参看 datamodel/_copy.py
print(l2[0] is l3[0])  # True
l3[0] = '100'
print(l2[0] is l3[0])  # False

suits = 'spades diamonds clubs hearts'.split()
# ['spades', 'diamonds', 'clubs', 'hearts']

# list comprehension 列表推导
# l=[expr] 对序列或可迭代对象中的每个元素应用某种操作, 用生成的结果创建新的列表, 或用满足特定条件的元素创建子序列
ranks = [str(n) for n in range(2, 11)] + list('JQKA')
# ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# [i for i in range(0,10)] 等价于 list(range(0,10))

cards = [(suit, rank) for suit in suits
         for rank in ranks if suit == 'spades']

# 等价形式
cards = []
for suit in suits:
    for rank in ranks:
        if suit == 'spades':
            cards.append((suit, rank))

random.shuffle(cards)
print(cards)
# [('spades', '6'), ('spades', '2'), ('spades', '8')...

# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print([num for elem in vec for num in elem])  # [1, 2, 3, 4, 5, 6, 7, 8, 9]
