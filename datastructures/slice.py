# slice 切片
# slice(start, stop, step)
# 左闭右开 切片长度 stop-start
l = ['1', '2', '3', '4', '5']
print(l[:3])  # ['1', '2', '3'] l[0:3] l[0] l[1] l[2]
print(l[1::2])  # ['2', '4']  步长为2
print(l[-1::-1])  # ['5', '4', '3', '2', '1'] step<0时反向取值

print(l.__getitem__(slice(None, None, 2)))  # ['1', '3', '5'] l[::2]

# s.indices(len) -> tuple[int, int, int] 根据长度计算切片索引
# slice(None           ).indices(10) (0, 10,  1))
# slice(None,  None,  2).indices(10) (0, 10,  2))
# slice(1,     None,  2).indices(10) (1, 10,  2))
# slice(None,  None, -1).indices(10) (9, -1, -1))
# slice(None,  None, -2).indices(10) (9, -1, -2))
# slice(3,     None, -2).indices(10) (3, -1, -2))
# slice(None,  8,    -1).indices(10) (9, 8, -1))
# slice(None,  9,    -1).indices(10) (9, 9, -1))
# slice(None,  10,   -1).indices(10) (9, 9, -1))
