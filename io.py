# mode值包括 'r' ,表示文件只能读取; 'w' 表示只能写入, 现有同名文件会被覆盖
# 'r+' 表示打开文件进行读写 省略时为'r'
# 在模式后面加上一个 'b', 可以用 binary mode 打开文件。以bytes对象的形式读写

# 如果没有使用with关键字, 则应调用f.close()关闭文件
# 没有with和close调用f.write()时可能程序正常退出, 但未完全写入磁盘
f = open('1.txt', 'w', encoding="utf-8")
f.write('abc\ndef')
f.close()

# with .. as <==> try .. except .. finally .. 返回值最后会赋值给as后的变量
with open('1.txt', 'r', encoding='utf-8') as f:
    # f.read(size) 读取文件内容
    # 它会读取一些数据, 并返回字符串(文本模式), 或字节串对象(二进制模式)
    # size省略时或为负读取整个文件
    print(f.read(1))  # a

    # f.tell()返回文件对象f在文件中的位置
    print(f.tell())  # 1

    # f.seek(offset, whence) 可以改变文件对象的位置
    # whence值为0时,表示从文件开头计算 1 表示使用当前文件位置, 2 表示使用文件末尾作为参考点
    # 文本文件中只允许从开头进行搜索 seek(0,2)例外
    f.seek(0, 2)
    print(f.tell())  # 7
    f.seek(0, 0)

    for line in f:
        print(line, end='')
        # abc
        # def

