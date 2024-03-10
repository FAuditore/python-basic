import numpy as np

# np.random.random->[0.0, 1.0)
np.random.seed(0)
a = np.floor(10 * np.random.random((2, 3)))
print(a)

# [[5. 7. 6.]
#  [5. 4. 6.]]
print(a.shape)  # (2,3)

print(a.flat)  # 返回1维迭代器, 视图
# <numpy.flatiter object at 0x00000200F9CDF3A0>

print(a.ravel())  # 返回1维数组视图 [5. 7. 6. 5. 4. 6.]

print(a.flatten())  # 返回1维数组副本 [5. 7. 6. 5. 4. 6.]

# 修改形状
print(a.reshape(3, 2))
# [[5. 7.]
#  [6. 5.]
#  [4. 6.]]

# 返回转置
print(a.T)
# [[5. 5.]
#  [7. 4.]
#  [6. 6.]]

# 就地修改形状
a.resize(3, 2)
print(a)
# [[5. 7.]
#  [6. 5.]
#  [4. 6.]]

# -1, 自动计算其他维度大小
print(a.reshape((1, 2, -1)))
# [[[5. 7. 6.]
#   [5. 4. 6.]]]
a.shape = 2, -1, 1
print(a)
# [[[5.]
#   [7.]
#   [6.]]
#
#  [[5.]
#   [4.]
#   [6.]]]

# append 将新元素添加到数组末尾
a = np.array([[1, 2, 3]])
# 不指定轴会转为1维数组追加
print(np.append(a, [4, 5, 6]))  # [1 2 3 4 5 6]

# 指定轴必须有正确的形状
print(np.append(a, np.array([[4, 5, 6]]), axis=0))
# [[1 2 3]
#  [4 5 6]]

# Stacking 沿不同轴堆叠
print(a := np.floor(10 * np.random.random((2, 2))))
# [[4. 8.]
#  [9. 3.]]
print(b := np.floor(10 * np.random.random((2, 2))))
# [[7. 5.]
#  [5. 9.]]

# 沿第一轴堆叠 axis=0
print(np.vstack((a, b)))
# [[4. 8.]
#  [9. 3.]
#  [7. 5.]
#  [5. 9.]]

# 沿第二轴堆叠 axis=1
print(np.hstack((a, b)))
# [[4. 8. 7. 5.]
#  [9. 3. 5. 9.]]

# 沿指定轴连接
print(np.concatenate((a[:, :, np.newaxis], b[:, :, np.newaxis]), axis=2))
# [[[4. 7.]
#   [8. 5.]]
#
#  [[9. 5.]
#   [3. 9.]]]

# r_,c_ 使用切片沿指定轴堆叠数组
# 第一个元素使用'r'或'c'创建矩阵
# 与数组一起用作参数时r_和c_在默认行为上类似于vstack和hstack,但允许使用可选参数给出要连接的轴的编号
print(np.r_['r', 2:5, [1, 2, 3], 4:7])  # [[2 3 4 1 2 3 4 5 6]]
print(np.c_[2:5, 1:4, 4:7])
# [[2 1 4]
#  [3 2 5]
#  [4 3 6]]


# hsplit水平分拆数组 vsplit 垂直分拆
a = np.floor(10 * np.random.random((2, 12)))
print(a)
# [[0. 0. 0. 8. 7. 8. 9. 7. 4. 7. 1. 6.]
# [1. 9. 5. 4. 2. 7. 4. 5. 0. 6. 6. 6.]]
print(np.hsplit(a, 3))
# [array([[0., 0., 0., 8.],
#        [1., 9., 5., 4.]]),
#  array([[7., 8., 9., 7.],
#        [2., 7., 4., 5.]]),
#  array([[4., 7., 1., 6.],
#        [0., 6., 6., 6.]])]
print(np.hsplit(a, (3,)))  # 沿指定列分割
# [array([[0., 0., 0.],
#        [1., 9., 5.]]),
#  array([[8.],
#        [4.]]),
#  array([[7., 8., 9., 7., 4., 7., 1., 6.],
#        [2., 7., 4., 5., 0., 6., 6., 6.]])]
