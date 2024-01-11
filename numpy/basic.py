import numpy as np

# NumPy是Python中科学计算的基础包
# 它是一个Python库，提供多维数组对象，各种派生对象（如掩码数组和矩阵）
# 以及用于数组快速操作的各种API
# 有包括数学、逻辑、形状操作、排序、选择、输入输出、离散傅立叶变换、基本线性代数
# 基本统计运算和随机模拟等等
#
# NumPy包的核心是 ndarray 对象
# 它封装了python原生的同数据类型的 n 维数组，为了保证其性能优良
# 其中有许多操作都是代码在本地进行编译后执行的
#
# NumPy数组 和 原生Python Array（数组）之间有几个重要的区别：
#
# NumPy 数组在创建时具有固定的大小，与Python的原生数组对象（可以动态增长）不同。
#   更改ndarray的大小将创建一个新数组并删除原来的数组。
# NumPy 数组中的元素都需要具有相同的数据类型，因此在内存中的大小相同。
#   例外情况：Python的原生数组里包含了NumPy的对象的时候，这种情况下就允许不同大小元素的数组。
# NumPy 数组有助于对大量数据进行高级数学和其他类型的操作。
#   通常，这些操作的执行效率更高，比使用Python原生数组的代码更少。
# 越来越多的基于Python的科学和数学软件包使用NumPy数组;
# 虽然这些工具通常都支持Python的原生数组作为参数，但它们在处理之前会还是会将输入的数组转换为NumPy的数组，
# 而且也通常输出为NumPy数组。换句话说，为了高效地使用当今科学/数学基于Python的工具（大部分的科学计算工具），
# 你只知道如何使用Python的原生数组类型是不够的 - 还需要知道如何使用 NumPy 数组。

a = np.arange(12).reshape(2, 2, 3)
# 打印数组时，NumPy以与嵌套列表类似的方式显示它，但具有以下布局：
# 最后一个轴从左到右打印，
# 倒数第二个从上到下打印，
# 其余部分也从上到下打印，每个切片用空行分隔。
print(a)
# [[[ 0  1  2]
#   [ 3  4  5]]
#
#  [[ 6  7  8]
#   [ 9 10 11]]]

# ndarray.ndim - 数组的轴（维度）的个数
print(a.ndim)  # 3

# ndarray.shape - 数组的维度
# n行和m列的矩阵，shape将是(n,m)
print(a.shape)  # (2,2,3)

# ndarray.size - 数组元素的总数
print(a.size)  # 12

# ndarray.dtype - 一个描述数组中元素类型的对象
print(a.dtype)  # int32

# ndarray.itemsize - 数组中每个元素的字节大小
print(a.itemsize)  # 4

# 反转元素
print(np.flip(a))
# [[[11 10  9]
#   [ 8  7  6]]
#
#  [[ 5  4  3]
#   [ 2  1  0]]]

# b = np.array(1, 2, 3)  # wrong
b = np.array([1, 2, 3])
print(type(b))  # <class 'numpy.ndarray'>

c = np.array([[1, 2], (3.5, 4)], dtype=complex)
print(c)
# [[1. +0.j 2. +0.j]
#  [3.5+0.j 4. +0.j]]

# 由0组成的数组
# 默认情况的数据类型是float64
print(np.zeros((3, 4)))
# [[0. 0. 0. 0.]
#  [0. 0. 0. 0.]
#  [0. 0. 0. 0.]]

# 由1组成的数组
print(np.ones((2, 2, 3), dtype=np.int16))
# [[[1 1 1]
#   [1 1 1]]
#
#  [[1 1 1]
#   [1 1 1]]]

# 创建一个数组，其初始内容是随机的，取决于内存的状态
print(np.empty((2, 3)))
# [[ 3.75593260e-272  6.80883106e-242 -2.58412764e-192]
#  [-1.24620767e+232  8.67299337e-247 -4.64882666e-211]]

# arange 类似于range,第三个参数为步长,左闭右开
print(np.arange(0, 2, 1 / 3))
# [0.         0.33333333 0.66666667 1.         1.33333333 1.66666667]

# linspace 创建包含指定元素数量的数组,包含端点
print(np.linspace(0, 2, 4))
# [0.         0.66666667 1.33333333 2.        ]

# 算术运算符会应用到[元素]级别, 产生新数组保存结果
a = np.arange(5)
print(a)  # [0 1 2 3 4]

print(a - np.ones((1, 5)))
# [[-1.  0.  1.  2.  3.]]

print(a * np.linspace(1, 5, 5))
# [ 0.  2.  6. 12. 20.] --> a*[1,2,3,4,5]

print(a ** 2)
# [ 0  1  4  9 16]

print(a < 2)
# [ True  True False False False]

# dot @ 矩阵乘法,点乘
A = np.array([[1, 2], [3, 4]])
B = np.array([[2], [1]])
print(A.shape, B.shape)  # (2, 2) (2, 1)
C = A @ B
print(C)
# [[ 4]
#  [10]]
print(C.shape)  # (2, 1)

# 一元操作符
print(C.sum(), C.max(), C.min(), C.mean())  # 14 10 4 7.0

# 规约函数 沿指定轴操作
b = np.arange(12).reshape(3, 4)
print(b)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]
print(b.sum(axis=1))  # 水平方向, 按行求和 [ 6 22 38]
print(b.sum(axis=0))  # 垂直方向, 按列求和 [12 15 18 21]
print(b.cumsum(axis=1))  # 每行累计和
# [[ 0  1  3  6]
#  [ 4  9 15 22]
#  [ 8 17 27 38]]

# 沿哪个轴规约就把哪个维度缩成0
# 可以看成去掉对应层的括号,然后把剩余元素元素规约
b = np.array([[[1, 1, 1], [2, 2, 2]], [[3, 3, 3], [4, 4, 4]]])
print(b)  # (2,2,3)
# [[[1 1 1]
#   [2 2 2]]
#
#  [[3 3 3]
#   [4 4 4]]]
print(b.sum(axis=0))  # (2,3) 去掉最外层的括号,剩余两个ndarray相加
# [[4 4 4]
#  [6 6 6]]
print(b.sum(axis=1))  # (2,3)去掉中间层的括号,每部分两个ndarray相加
# [[3 3 3]
#  [7 7 7]]
print(b.sum(axis=2))  # (2,2) 去掉最里层的括号, 每个部分3个数相加
# [[ 3  6]
#  [ 9 12]]

# Universal Functions
# sin,cos,exp 在数组上的元素进行,产生一个数组
a = np.linspace(0, np.pi, 4)
print(a)  # [0.         1.04719755 2.0943951  3.14159265]
print(np.sin(a))  # [0.00000000e+00 8.66025404e-01 8.66025404e-01 1.22464680e-16]
print(np.cos(a))  # [ 1.   0.5 -0.5 -1. ]
print(np.exp(a))  # [ 1.          2.84965391  8.1205274  23.14069263]

# linalg.py 线性代数
a = np.array([[1.0, 2.0], [3.0, 4.0]])
print(np.linalg.inv(a))
# [[-2.   1. ]
#  [ 1.5 -0.5]]

u = np.eye(2)  # 单位阵 eye->I
print(u)
# [[1. 0.]
#  [0. 1.]]
print(np.trace(u))  # 2.0
print(np.linalg.solve(a, u))  # solve(a, b) ax = b 返回x
# [[-2.   1. ]
#  [ 1.5 -0.5]]
print(np.linalg.eig(a))  # 返回特征值, 特征向量数组
# (array([-0.37228132,  5.37228132]),
# array([[-0.82456484, -0.41597356],[ 0.56576746, -0.90937671]]))
