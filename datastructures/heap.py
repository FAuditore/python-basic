# heapq 模块提供了基于常规列表来实现堆的函数
# 最小值的条目总是保持在位置零
from heapq import heapify, heappop, heappush

data = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
heapify(data)  # rearrange the list into heap order
print(data)  # [0, 1, 2, 6, 3, 5, 4, 7, 8, 9]

heappush(data, -5)  # add a new entry
print(data)  # [-5, 0, 2, 6, 1, 5, 4, 7, 8, 9, 3]

print([heappop(data) for i in range(3)])  # fetch the three smallest entries
print(data)  # [2, 3, 4, 6, 9, 5, 8, 7]
