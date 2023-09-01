# 错误分为句法错误和异常。

# 语法错误
# while True print('Hello world')
#   File "<stdin>", line 1
#     while True print('Hello world')
#                    ^
# SyntaxError: invalid syntax

# 异常
# 10 * (1/0)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# ZeroDivisionError: division by zero

# try
# 首先执行try子句, 如果没有触发异常, 则跳过except子句
# 如果在执行try子句时发生了异常, 则跳过该子句中剩下的部分
# 如果异常的类型与except关键字后指定的异常相匹配, 则会执行except子句, 然后跳到try/except代码块之后继续执行
# 如果发生的异常与except子句中指定的异常不匹配, 则它会被传递到外部的try语句中；
# 如果没有找到处理程序，则它是一个未处理异常且执行将终止

try:
    x = int(input('input a number:'))
except ValueError as v:
    print('That was no valid number')
    print(v)  # invalid literal for int() with base 10: 'a'
    print(v.args)  # ("invalid literal for int() with base 10: 'a'",)
except (RuntimeError, TypeError):
    pass
except Exception as err:  # Exception 可以被用作通配符，捕获（几乎）一切
    print(f"Unexpected {err=}, {type(err)=}")
    # raise 语句支持强制触发指定的异常 raise的参数就是要触发的异常
    # 为了表明一个异常是另一个异常的直接后果, raise语句允许一个可选的from子句
    raise RuntimeError from err
else:  # else 放在所有except子句之后, 它适用于try子句没有引发异常要执行的代码
    print('no exception')
finally:  # 定义在所有情况下都必须要执行的清理操作, 不论try语句是否触发异常, 都会执行finally子句
    x = 0
    print('done')


# 如果异常没有except子句处理, 在finally子句执行后会被重新触发
# except或else子句执行期间也会触发异常, 该异常会在finally子句执行之后被重新触发
# 如果finally子句中包含break、continue或return等语句,异常将不会被重新引发
# 如果执行try语句时遇到break、continue或return语句, 则finally子句在执行break、continue或return语句之前执行
# 如果finally子句中包含return语句, 则返回值来自finally子句的某个return语句的返回值

def bool_return():
    try:
        return True
    finally:
        return False


print(bool_return())  # False
