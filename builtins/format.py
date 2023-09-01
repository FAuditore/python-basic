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
