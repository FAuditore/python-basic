import numpy as np

a = np.array([1, 2, 3])
b = a  # 浅拷贝
b[1] = 5
print(a, b is a)  # [1 5 3] True

# view 创建数据相同的新数组
c = a.view()
print(c is a)  # False
print(c.base is a)  # True

# 切片返回视图
d = a[...]
print(d is a)  # False
print(d.base is a)  # True

# 深拷贝 深拷贝可以防止原数组不被回收内存泄漏
e = a.copy()
print(e is a)  # False
print(e.base is a)  # False
