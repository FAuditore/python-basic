import datetime
import string

"""
    format(value, format_spec='') 将value格式化成format_spec指定的格式
    =>type(value).__format__(value, format_spec)
    若format_spec为空 则等价于str(value)
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

# string.Formatter 自定义字符串格式化
# format(format_string, /, *args, **kwargs)
print(string.Formatter().format('{}', a))  # 1.2345

"""
    str.format() 字符串格式化
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
print('{1} {a} {d[k]} {l[2]} {2.__name__} {2!s}'.format(0, 1, f, a=2, d=d, l=l))
# 1 2 v 3 <lambda> <function <lambda> at 0x000001DE9EC640E0>
