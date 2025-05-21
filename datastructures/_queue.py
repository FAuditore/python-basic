from collections import deque
from queue import LifoQueue, PriorityQueue, Queue

# Queue, LifoQueue, PriorityQueue
q = Queue(maxsize=10)  # If maxsize is <= 0, the queue size is infinite
q.put(1)  # put(self, item, block=True, timeout=None)
print(q.full())  # False
print(q.qsize())  # 1
print(q.get())  # 1 get(self, block=True, timeout=None)
print(q.empty())  # True

lq = LifoQueue(10)
pq = PriorityQueue(10)
pq.put([80, 'a'])
pq.put([2, 'b'])
while pq.qsize():
    print(pq.get_nowait())
# [2, 'b']
# [80, 'a']

# deque 线程安全的双向队列
# maxlen 队列容量 不可修改
dq = deque(range(10), maxlen=10)  # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

# 元素旋转 所有元素向右移动指定步数 末尾元素移到开头
# 正数右移, 负数左移
dq.rotate(3)  # deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
dq.rotate(-3)  # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

# 左端添加元素 len(dq) == maxlen时 头部添加元素会在另一端删除尾部元素
dq.appendleft(100)  # deque([0, 1, 2, 3, 4, 5, 6, 7, 8], maxlen=10)

# 右端添加元素
dq.append(101)  # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 101], maxlen=10)

# 从右端弹出元素
print(dq.pop())  # 101 deque([0, 1, 2, 3, 4, 5, 6, 7, 8], maxlen=10)

# 从左端弹出元素
print(dq.popleft())  # 0 deque([1, 2, 3, 4, 5, 6, 7, 8], maxlen=10)

# 删除指定元素
dq.remove(1)  # deque([2, 3, 4, 5, 6, 7, 8], maxlen=10)

# 清空队列
dq.clear()  # deque([], maxlen=10)
