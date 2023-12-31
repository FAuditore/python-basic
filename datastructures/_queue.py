from collections import deque
from queue import LifoQueue, PriorityQueue, Queue

# Queue, LifoQueue, PriorityQueue
q = Queue(maxsize=10)
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
dq.rotate(3)  # deque([7, 8, 9, 0, 1, 2, 3, 4, 5, 6], maxlen=10)
dq.rotate(-3)  # deque([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], maxlen=10)

# len(dq) == maxlen时 头部添加元素会在另一端删除尾部元素
dq.appendleft(100)  # deque([100, 0, 1, 2, 3, 4, 5, 6, 7, 8], maxlen=10)
