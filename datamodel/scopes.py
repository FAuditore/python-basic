from dis import dis

# 函数在执行时使用函数局部变量符号表, 所有函数变量赋值都存在局部符号表中
# 引用变量时, 首先在局部符号表里查找变量, 然后是外层函数局部符号表, 再是全局符号表, 最后是内置名称符号表

# global 语句用于表明特定变量在全局作用域里, 并应在全局作用域中重新绑定
# nonlocal 语句表明特定变量在外层作用域中, 并应在外层作用域中重新绑定
g = 1


# 默认在函数中的变量为局部变量
# def f():
#   print(g) # UnboundLocalError: cannot access local variable
#            # 'g' where it is not associated with a value
# f()


def f():
    global g  # 声名为全局变量
    print(g)
    g = 5


f()  # 1
f()  # 5
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

# 局部赋值（这是默认状态）不会改变scope_test对spam的绑定
# nonlocal赋值会改变scope_test对spam的绑定
# global赋值会改变模块层级的绑定 global赋值前没有spam的绑定
def scope_test():
    def do_local():
        spam = "local spam"

    def do_nonlocal():
        nonlocal spam
        spam = "nonlocal spam"

    def do_global():
        global spam
        spam = "global spam"

    spam = "test spam"
    do_local()
    print("After local assignment:", spam)  # test spam
    do_nonlocal()
    print("After nonlocal assignment:", spam)  # nonlocal spam
    do_global()
    print("After global assignment:", spam)  # nonlocal spam 声明了全局变量, 但是print优先使用局部spam


scope_test()
print("In global scope:", spam)  # global spam


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
