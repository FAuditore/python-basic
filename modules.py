# 模块包含可执行语句及函数定义 这些语句用于初始化模块, 且仅在import语句第一次遇到模块名时执行
# 模块搜索路径:
#     被命令行直接运行的脚本所在的目录（或未指定文件时的当前目录）
#     PYTHONPATH （目录列表，与 shell 变量 PATH 的语法一样）
#     依赖于安装的默认值（按照惯例包括一个 site-packages 目录, 由 site 模块处理）
import builtins

import func

func.my_sum(1, 2)

from func import my_sum

my_sum(1, 2)

# from xxx import *导入所有不以下划线_开头的名称
# 如果包的 __init__.py 代码定义了列表 __all__, 运行 from package import * 时, 它就是被导入的模块名列表
from func import *  # __all__ = ["my_sum", "my_div"]

my_sum(1, 2)

from func import my_sum as m

m(1, 2)

# from. from..  相对导入
from .func import my_div

my_div(1, 2)

# 通过全局变量 __name__ 可以获取模块名
print(__name__)  # __main__
print(func.__name__)  # func

# dir()
# 查找模块定义的名称, 返回结果是经过排序的字符串列表
print(dir(func))  # ['FuncObject', '__builtins__', '__cached__', '__doc__',...]
# dir不会列出内置函数和变量的名称
print(dir(builtins))  # ['ArithmeticError', 'AssertionError',...,'type', 'vars', 'zip']

# __init__.py 将该目录视为一个Python包(module)
# 其中可以定义常量或变量, 初始化命名空间, 设置__all__

# 为了快速加载, Python把模块的编译版本缓存在 __pycache__ 目录中,文件名为 [module].[version].pyc
# __pycache__/func.cpython-311.pyc
# 从 .pyc 文件读取的程序不比从 .py 读取的执行速度快，.pyc文件只是加载速度更快。

# Python 命令中使用 -O 或 -OO 开关, 可以减小编译模块的大小
# -O 去除断言语句, -OO 去除断言语句和 __doc__ 字符串

if __name__ == '__main__':
    import sys

    # >python modules.py -a -b
    print(sys.argv)  # ['modules.py', '-a', '-b']

    # 变量 sys.path 是字符串列表, 用于确定解释器的模块搜索路径
    # 该变量以环境变量 PYTHONPATH 提取的默认路径进行初始化
    sys.path.append('./')
