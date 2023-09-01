# list 列表
# [element]
import random

l = ['2', '1', '3', '4'] + ['5']  # ['2', '1', '3', '4', '5']

del l[0]  # ['1', '3', '4', '5']
l.reverse()  # l -> ['5', '4', '3', '1']
newL = sorted(l)  # newL -> ['1', '3', '4', '5']
l.sort(reverse=False, key=int)  # l - > ['1', '3', '4', '5'] key=int(element)
l[2:4] = []  # l->['1', '3']

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
# l=[expr]
ranks = [str(n) for n in range(2, 11)] + list('JQKA')
# ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# [i for i in range(0,10)] 等价于 list(range(0,10))

cards = [(suit, rank) for suit in suits
         for rank in ranks]
random.shuffle(cards)
print(cards)
# [('clubs', '4'), ('hearts', '10'), ('diamonds', '9'),...
