# 字符串用成对的单引号 ('...') 或双引号 ("...") 来标示, 结果完全相同
print('doesn\'t')  # doesn't
print("doesn't")  # doesn't

# Python没有char类型, 而是将字符串中的每个码位表示为一个长度为 1 的字符串对象
# 内置函数 ord() 可将一个码位由字符串形式转换为取值范围在 0 - 10FFFF 之内的整数
# chr() 可将一个取值范围在 0 - 10FFFF 之内的整数转换为长度为 1 的对应字符串对象
print(ord('abc'[-1]))  # 99
print(chr(97))  # a

# 原始字符串
print(r'a\b\c')  # a\b\c

# 字符串字面值可以包含多行 一种实现方式是使用三重引号："""...""" 或 '''...'''
# 字符串中将自动包括行结束符, 但也可以在换行的地方添加一个\来避免此情况
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

# 字符串用+合并 用*重复
print('abc' + 'd' * 5)  # abcddddd
# 相邻字面值自动合并 仅用于字面值, 不可用于表达式和变量
print('abc''efg'
      'hij')  # abcefghij

# 索引
word = 'Python'
print(word[0], word[5])  # P y n
print(word[-1], word[-2])  # n o
print(word[2:5])  # tho

word = 'abcabc'
# str.count(sub[, start[, end]])
# 返回子字符串 sub 在 [start, end] 范围内非重叠出现的次数
print(word.count('c'))  # 2

# str.find(sub[, start[, end]])
# 返回子字符串 sub 在 s[start:end] 切片内被找到的最小索引
# 如果 sub 未被找到则返回 -1
print(word.find('b', 2))  # 4

# str.index(sub[, start[, end]]) 类似于find, 但在找不到子字符串时会引发 ValueError

# str.format(*args, **kwargs)
# 执行字符串格式化操作 调用此方法的字符串可以包含字符串字面值或者以花括号 {} 括起来的替换域
# 每个替换域可以包含一个位置参数的数字索引, 或者一个关键字参数的名称
# 返回的字符串副本中每个替换域都会被替换为对应参数的字符串值
print("The sum of 1 + 2 is {0}".format(1 + 2))  # The sum of 1 + 2 is 3

# str.join(iterable)
# 返回一个由 iterable 中的字符串拼接而成的字符串
# 如果 iterable 中存在任何非字符串值包括 bytes 对象则会引发 TypeError
# 调用该方法的字符串将作为元素之间的分隔
print(','.join(str(i) for i in range(5)))  # 0,1,2,3,4

# str.replace(old, new[, count])
# 返回字符串的副本, 其中出现的所有子字符串 old 都将被替换为 new
# 如果给出了可选参数 count, 则只替换前 count 次出现
print(word.replace('c', 'f', -1))  # abfabf
