from collections import namedtuple

# tuple 元组 不可修改的列表
# (element)
t = ('1', '2', '5') + ('3', '4')  # ('1', '2', '5', '3', '4')

# 元组由多个用逗号隔开的值组成
t = 123, 'aaa', t  # (123, 'aaa', ('1', '2', '5', '3', '4'))

# 只有一个元素的元组可以用逗号构建
singleton = 'abc',  # ('abc',)

# t[0]=100
# TypeError: 'tuple' object does not support item assignment

# named tuple 具名元组
Stu = namedtuple('Student', 'no name age')  # Stu = namedtuple('Student', ['no', 'name', 'age'])

a = Stu('123', 'liubo', '15')  # Student(no='123', name='liubo', age='15')
print(a.name)  # liubo
print(a._fields)  # ('no', 'name', 'age')
print(a._asdict())  # {'no': '123', 'name': 'liubo', 'age': '15'}
