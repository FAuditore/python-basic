import numpy as np

# view 视图
# 仅通过修改特定元数据(strides, dtype)而不修改数据缓冲区来访问
# 视图的修改会影响源数据
# copy 副本
# 通过复制数据缓冲区中的数据和元数据创建新数组
# 拷贝耗时耗内存但可以防止原数组不被回收导致的内存泄漏

a = np.array([1, 2, 3])
b = a  # 视图
b[1] = 5
print(a, b is a)  # [1 5 3] True

# view 创建视图
c = a.view()
print(c is a)  # False
print(c.base is a)  # True
c[1] = 9
print(a)  # [1 9 3]

# 基础索引总是返回视图
d = a[...]
print(d is a)  # False
print(d.base is a)  # True
d[1] = 99
print(a)  # [ 1 99  3]

# copy 创建副本
e = a.copy()
print(e is a)  # False
print(e.base is a)  # False
e[1] = 888
print(a)  # [ 1 99  3]

# 高级索引总是返回副本
x = np.arange(9).reshape(3, 3)
print(x)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

y = x[[1, ]]  # 整数数组高级索引
print(y, y.base)  # [[3 4 5]] None base为None即为副本

y = y ** 2
print(x, y)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]
# [[ 9 16 25]]

# 就地赋值 既非视图也非副本
x[[1]] = x[[1]] ** 2
print(x)
# [[ 0  1  2]
#  [ 9 16 25]
#  [ 6  7  8]]
