# 序列类型: 实现 __getitem__(self, item) 方法和 __len__(self) 方法
# 容器序列: 存放不同类型数据
#     list tuple collections.deque
# 扁平序列: 存放相同类型数据
#     str bytes bytearray memoryview array.array
# 可变序列:
#     list bytearray array.array collections.deque
# 不可变序列:
#     tuple str bytes
import random

# 序列拼接 + *
# 不会修改原有序列,生成新的序列返回
# *=和+=遇到不可变序列会生成新序列赋值 遇到可变序列会修改原序列
l = (1, 2)
print(l * 3 + l)  # (1, 2, 1, 2, 1, 2, 1, 2)

b = [['a'] * 3 for _ in range(3)]  # [['a', 'a', 'a'], ['a', 'a', 'a'], ['a', 'a', 'a']]
b[1][0] = 'X'
print(b)  # [['a', 'a', 'a'], ['X', 'a', 'a'], ['a', 'a', 'a']]

# 使用*时会复制引用 使用相同的对象
b = [['a'] * 3] * 3  # [['a', 'a', 'a'], ['a', 'a', 'a'], ['a', 'a', 'a']]
b[1][0] = 'X'
print(b)  # [['X', 'a', 'a'], ['X', 'a', 'a'], ['X', 'a', 'a']]


# 自定义序列
class CustomSeq(object):
    seq = [i for i in range(10, 15)]

    def __getitem__(self, item):
        """
            实现__getitem__(self, item)序列协议
            可以访问元素, 迭代, in
        """
        print(item, end=' ')
        return self.seq[item]

    def __setitem__(self, key, value):
        """
            实现__setitem__(self, key, value)序列协议
            可以赋值
        """
        self.seq[key] = value

    def __len__(self):
        return 4


c = CustomSeq()
print(len(c))  # 4 但是内部列表长度是5

# 访问序列元素
print(c[1::2])  # slice(1, None, 2) [11, 13]

# 使用__getitem__实现__iter__
print([i for i in c])  # 0 1 2 3 4 5 [10, 11, 12, 13, 14]

# 使用__getitem__实现__contains__
print(14 in c)  # 0 1 2 3 4 True

random.shuffle(c)  # 2 3 2 2 1 1
print(c[:])  # slice(None, None, None) [10, 11, 13, 12, 14]

