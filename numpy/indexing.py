import numpy as np

a = np.arange(5) ** 2
print(a)  # [ 0  1  4  9 16]

# 使用数组索引
print(a[[0, 2, 3, 0]])  # [0 4 9 0]
a[[0, 2]] = (10, 11)
print(a[np.arange(0, 4)])  # [10  1 11  9]
print(a[np.arange(0, 4).reshape(2, 2)])  # [[10  1] [11  9]]


def f(x, y):
    return 10 * x + y


# ndarray每个轴有一个索引,以逗号分割,左闭右开
# 使用元组索引 a[i,j]等价于a[(i,j)]
b = np.fromfunction(f, (5, 4), dtype=int)
print(b)
# [[ 0  1  2  3]
#  [10 11 12 13]
#  [20 21 22 23]
#  [30 31 32 33]
#  [40 41 42 43]]
print(b[2, 3])  # 23
print(b[:, -1])  # [ 3 13 23 33 43]
print(b[-1])  # [40 41 42 43] -->b[-1,:] 缺失的轴默认为完整的切片
print(b[1:2, ...])  # [[10 11 12 13]] --> b[1:2, :] ...代表剩余所有轴完整索引

a = np.arange(12).reshape(3, 4)
i = np.array([[0, 1],  # indices for the first dim of `a`
              [1, 2]])
j = np.array([[2, 1],  # indices for the second dim
              [3, 3]])
print(a[i, j])
# [[ 2  5]
#  [ 7 11]]
print(a[i, 2])
# [[ 2  6]
#  [ 6 10]]

# Boolean数组索引
print(a > 4)
# [[False  True  True  True]
#  [False False False  True]
#  [ True  True False False]
#  [False  True  True  True]
#  [False False False  True]]
print(a[a > 4])  # 返回一维数组 [ 5  6  7  8  9 10 11]
print(a[[True, False, False]])  # [[0 1 2 3]]

data = np.sin(np.arange(20)).reshape(5, 4)  # 4 time-dependent series
print(data)
# [[ 0.          0.84147098  0.90929743  0.14112001]
#  [-0.7568025  -0.95892427 -0.2794155   0.6569866 ]
#  [ 0.98935825  0.41211849 -0.54402111 -0.99999021]
#  [-0.53657292  0.42016704  0.99060736  0.65028784]
#  [-0.28790332 -0.96139749 -0.75098725  0.14987721]]
print(data.argmax(axis=0))  # [2 0 3 1]
print(data[data.argmax(axis=0), range(4)])  # [0.98935825 0.84147098 0.99060736 0.6569866 ]

# 迭代 以第一个轴开始
for row in b:
    print(row)
# [0 1 2 3]
# [10 11 12 13]
# [20 21 22 23]
# [30 31 32 33]
# [40 41 42 43]

# 迭代所有元素
for x in b.flat:
    print(x, end='')
# 012310111213202122233031323340414243
