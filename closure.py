from dis import dis

g = 1


def f():
    """
       b = 6
       def f():
           print(b) # UnboundLocalError: cannot access local variable
                    # 'b' where it is not associated with a value
           b = 9
       f()
       默认在函数中的变量为局部变量
    """
    global g  # 声名为全局变量
    print(g)
    g = 5


print(dis(f))


#  15           0 RESUME                   0
#
#  17           2 LOAD_GLOBAL              1 (NULL + print)
#              14 LOAD_GLOBAL              2 (g)
#              26 PRECALL                  1
#              30 CALL                     1
#              40 POP_TOP
#
#  18          42 LOAD_CONST               1 (5)
#              44 STORE_GLOBAL             1 (g)
#              46 LOAD_CONST               0 (None)
#              48 RETURN_VALUE
# None


# closure 闭包
# 自由变量:未在本地作用域绑定的变量
def averager():
    series = []  # 闭包
    total = 0  # 闭包
    count = 0  # 闭包

    def average(new):
        series.append(new)  # series是自由变量
        return sum(series) / len(series)

    def average_v2(new):
        nonlocal total, count  # nonlocal 标记为自由变量
        total += new
        count += 1
        return total / count

    return average


avg = averager()
print(avg(1))  # 1.0
print(avg(2))  # 1.5
print(avg.__code__.co_freevars)  # ('series',)
print(avg.__closure__[0].cell_contents)  # [1, 2]
