import datetime

# format(value, format_spec='') 将value格式化成format_spec指定的格式
# <==>type(value).__format__(value, format_spec)
# 若format_spec为空 则等价于str(value)
"""
    format_spec     ::=  [[fill]align][sign]["z"]["#"]["0"][width][grouping_option]["." precision][type]
    fill            ::=  <any character>
    align           ::=  "<" | ">" | "=" | "^"
    sign            ::=  "+" | "-" | " "
    width           ::=  digit+
    grouping_option ::=  "_" | ","
    precision       ::=  digit+
    type            ::=  "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g" | "G" | "n" | "o" | "s" | "x" | "X" | "%"
"""
a = 1.2345
print(format(a, '.2f'))  # 1.23
print(format(a, '.1%'))  # 123.4%

t = datetime.datetime.now()
print(format(t, '%H:%M:%S'))  # datetime.datetime.__format__(t, '%H:%M:%S')

# str.format() 字符串格式化
"""
    replacement_field ::=  "{" [field_name] ["!" conversion] [":" format_spec] "}"
    field_name        ::=  arg_name ("." attribute_name | "[" element_index "]")*
    arg_name          ::=  [identifier | digit+]  默认以0,1,2...按顺序自动插入 使用标识符必须用关键字参数 
    attribute_name    ::=  identifier
    element_index     ::=  digit+ | index_string
    index_string      ::=  <any source character except "]"> +
    conversion        ::=  "r" | "s" | "a"    !s=>str() !r=>repr() !a=> ascii()
"""
l = [1, 2, 3]
d = {'k': 'v'}
f = lambda n: n
# {arg_name}替换变量 花括号及之内的字符(称为格式字段)被替换为传递给str.format()方法的对象
# {!conversion}表示转换值 !s=>str() !r=>repr() !a=> ascii()
print('{1} {a} {d[k]} {l[2]} {2.__name__} {2!s}'.format(0, 1, f, a=2, d=d, l=l))
# 1 2 v 3 <lambda> <function <lambda> at 0x000001DE9EC640E0>

# :冒号后传递整数表示最小字符宽度
# ^居中 <左对齐 >右对齐 冒号后面填写填充字符 默认为空格
no = 1.2345
print(f'{no:g>10}-->{no:10f}')  # gggg1.2345-->  1.234500

# %百分比表示
print(f'{no:.2%}')  # 123.45%
# e科学计数法
print(f'{no:.2e}')  # 1.23e+00

# :冒号后填写b d o x进制转化
n = 10
print(f'{n:b}')  # 1010
print(f'{n:o}')  # 12
print(f'{n:d}')  # 10
print(f'{n:x}')  # a
print(f'{n:#x}')  # 0xa
print(f'{n:#X}')  # 0xA

# reprlib 用于缩略显示大型或嵌套容器
import reprlib

print(reprlib.repr(list(range(1000))))  # [0, 1, 2, 3, 4, 5, ...]

# pprint 当输出结果过长而需要折行时，“美化输出机制”会添加换行符和缩进
import pprint

pprint.pprint([l, d, f], width=30)
# [[1, 2, 3],
# {'k': 'v'},
# <function <lambda> at 0x102490540>]

# textwrap 格式化文本段落 适应宽度
import textwrap

doc = """The wrap() method is just like fill() except that it returns
a list of strings instead of one big string with newlines to separate
the wrapped lines."""
print(textwrap.fill(doc, width=40))
# The wrap() method is just like fill()
# except that it returns a list of strings
# instead of one big string with newlines
# to separate the wrapped lines.

# locale 模块处理与特定地域文化相关的数据格式
import locale

locale.setlocale(locale.LC_ALL, 'zh_CN')
conv = locale.localeconv()
print(locale.format_string("%d", 1234567.8, grouping=True))  # 1,234,567
print(locale.format_string("%s%.*f", (conv['currency_symbol'],
                                      conv['frac_digits'], 1234567.8), grouping=True))  # ￥1,234,567.80

# 模版
# 占位符由$加上合法的Python标识符(只能包含字母、数字和下划线)构成
# 一旦使用花括号将占位符括起来, 就可以在后面直接跟上更多的字母和数字而无需空格分割 $$将被转义成单个字符$
from string import Template

t = Template('${village}folk send $$10 to $cause.')
print(t.safe_substitute(cause='the ditch fund'))  # ${village} folk send $10 to the ditch fund.
