# interning 驻留
# 对于字符串和小整数返回相同的引用
# 对于元组,str,bytes等,使用[:]或tuple()返回的其实是同一个对象的引用而不是副本
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False

a = 1000
b = 1000
print(a is b)  # True

a = 'abc'
b = 'abc'
print(a is b)  # True

# 复制列表默认做前浅拷贝
# 列表中如果有可变对象, 复制的是同一个引用
l1 = [1, [2, 3], (4, 5)]
l2 = l1[:]  # 创建副本
l3 = list(l1)  # 创建副本
print(l1 is l2, l1 is l3)  # False False
l1[1].append(8)
print(l1, l2, l3)  # [1, [2, 3, 8], (4, 5)] [1, [2, 3, 8], (4, 5)] [1, [2, 3, 8], (4, 5)]
# 列表复制的是[2,3]的同一个引用

l1[1] = 100
l3[2] += (6, 7)  # 修改复制的元组
print(l1, l2, l3)  # [100, [2, 3, 8], (4, 5)] [1, [2, 3, 8], (4, 5)] [1, [2, 3, 8], (4, 5, 6, 7)]
print(l1[2] is l2[2], l1[2] is l3[2])  # True False
# 复制不可变对象时不会有问题
# 因为不可变对象修改值会产生新的引用 参看copy.png

# 为任意对象做深拷贝和浅拷贝
from copy import copy, deepcopy

a = [1, 2, 3]
b = [4, 5, a]
c = copy(b)  # 浅拷贝 遇到引用时直接复制引用
c[2].append(4)
c[0] = 100
print(a, b, c)  # [1, 2, 3, 4] [4, 5, [1, 2, 3, 4]] [100, 5, [1, 2, 3, 4]]
c[2].remove(4)

d = deepcopy(b)  # 深拷贝 遇到引用时创建新对象
print(a, b, d)  # [1, 2, 3] [4, 5, [1, 2, 3]] [4, 5, [1, 2, 3]]
d[2].append(4)
print(a, b, d)  # [1, 2, 3] [4, 5, [1, 2, 3]] [4, 5, [1, 2, 3, 4]]
