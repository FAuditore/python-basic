import os
import timeit

# 一定要使用 import os 而不是 from os import *
# 这将避免内建的open()函数被os.open()隐式替换, 因为它们的使用方式大不相同
os.system('ls')

# 高阶文件操作 主要是文件拷贝和删除
# shutil.rmtree(): 删除目录和它里面的所有内容。
# shutil.copytree(): 复制整个目录树
import shutil

shutil.copyfile('../main.py', 'a.py')
print(shutil.disk_usage('../'))  # usage(total=994662584320, used=118440652800, free=876221931520)
os.remove('a.py')

# 文件通配符 使用通配符搜索创建文件列表
import glob

# *匹配任意数量的字符，?匹配单个字符，[a-z]匹配范围内的字
print(glob.glob('s*.py'))  # ['_string.py', 'stdlib.py']

# 命令行参数
import sys, argparse

# >python stdlib.py -l 5 main.py
print(sys.argv)  # ['stdlib.py', '-l', '5', 'main.py']
parser = argparse.ArgumentParser(
    prog='stdlib',
    description='Show top lines from each file'
)
parser.add_argument('filenames', nargs='+')
parser.add_argument('-l', '--lines', type=int, default=10)

args = parser.parse_args()
print(args)  # Namespace(filenames=['main.py'], lines=5)
print(args.filenames)  # ['main.py']

# 字符串模式匹配
# https://docs.python.org/zh-cn/3/library/re.html
import re

print(re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest'))  # ['foot', 'fell', 'fastest']

# 数学
import math

print(math.cos(math.pi / 4))  # 0.7071067811865476
print(math.log(16, 2))  # 4.0

import random

print(random.sample(range(10), 5))  # [3, 1, 8, 9, 6]

import statistics

data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
print(statistics.mean(data))  # 1.6071428571428572
print(statistics.median(data))  # 1.25
print(statistics.variance(data))  # 1.3720238095238095

# 互联网访问
from urllib.request import urlopen

with urlopen('http://worldtimeapi.org/api/timezone/etc/UTC.txt') as response:
    for line in response:
        line = line.decode()  # Convert bytes to a str
        if line.startswith('datetime'):
            print(line.rstrip())  # Remove trailing newline

# 日期和时间
from datetime import date

now = date.today()
print(now)  # 2023-09-02
print(now.strftime(
    '%m-%d-%y. %d %b %Y is a %A on the %d day of %B.'))
# 09-02-23. 02 Sep 2023 is a Saturday on the 02 day of September.

print(now - date(1970, 1, 1))  # 19602 days 0:00:00

# 数据压缩
import zlib

s = b'witch which has which witches wrist watch'
t = zlib.compress(s)
print(len(s), len(t), zlib.crc32(s))  # 41 37 226805979

# 性能测量
# timeit 模块可以快速演示在运行效率方面一定的优势
from timeit import Timer

# __init__(self, stmt="pass", setup="pass", timer=default_timer,globals=None)
print(Timer('t=a; a=b; b=t', 'a=1; b=2').timeit())  # 0.016142499996931292
print(Timer('a,b = b,a', 'a=1; b=2').timeit())  # 0.009712083003250882
print(timeit.timeit('1+1', number=1000))  # 6.041699816705659e-05

# 浮点运算
# decimal模块提供了一种Decimal数据类型用于十进制浮点运算
# 相比内置的float二进制浮点实现, 该类特别适用于
#     财务应用和其他需要精确十进制表示的用途
#     控制精度
#     控制四舍五入以满足法律或监管要求
#     跟踪有效小数位，或用户期望结果与手工完成的计算相匹配的应用程序
from decimal import *

print(round(Decimal('0.70') * Decimal('1.05'), 2))  # 0.74

# Decimal 可以模拟手工运算来避免当二进制浮点数无法精确表示十进制数时会导致的问题。
print(Decimal('1.00') % Decimal('.10'))  # 0.00
print(1.00 % 0.10)  # 0.09999999999999995
print(Decimal(1) / Decimal(7))  # 0.1428571428571428571428571429
