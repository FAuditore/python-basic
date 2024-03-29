import numpy as np

# 广播（Broadcasting）规则
# 广播允许通用功能以有意义的方式处理不具有完全相同形状的输入
# 广播的第一个规则是, 如果所有输入数组不具有相同数量的维度,
# 则将“1”重复地预先添加到较小数组的形状, 直到所有数组具有相同数量的维度
# 广播的第二个规则确保沿特定维度的大小为1的数组表现为具有沿该维度具有最大形状的数组的大小
# 假定数组元素的值沿着“广播”数组的那个维度是相同的
# 应用广播规则后, 所有数组的大小必须匹配

a = np.array([1, 2, 3.0])
print(a * [2, 2, 2])  # [2. 4. 6.]
print(a * 2)  # [2. 4. 6.]

# 广播从最右侧维度开始检查
# 要么维度相同, 要么其中一个是1(被拉伸/复制)到最大值
# Image  (3d array): 256 x 256 x 3
# Scale  (1d array):             3 对每个颜色乘以不同的标量
# Result (3d array): 256 x 256 x 3
#
# A      (4d array):  8 x 1 x 6 x 1
# B      (3d array):      7 x 1 x 5
# Result (4d array):  8 x 7 x 6 x 5

a = np.arange(0, 3, 0.5).reshape(2, 3)
print(a)
# [[0.  0.5 1. ]
#  [1.5 2.  2.5]]
b = np.array([1, 2, 3])
print(b.shape)  # (3,) -> (1,3) ->(2,3)
print(a + b)
# [[1.  2.5 4. ]
#  [2.5 4.  5.5]]
