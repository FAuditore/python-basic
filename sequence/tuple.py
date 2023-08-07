from collections import namedtuple

# tuple 元组 不可修改的列表
# (element)
t = ('1', '2', '5') + ('3', '4')  # ('1', '2', '5', '3', '4')

# named tuple 具名元组
Stu = namedtuple('Student', 'no name age')  # Stu = namedtuple('Student', ['no', 'name', 'age'])

a = Stu('123', 'liubo', '15')  # Student(no='123', name='liubo', age='15')
print(a.name)  # liubo
print(a._fields)  # ('no', 'name', 'age')
print(a._asdict())  # {'no': '123', 'name': 'liubo', 'age': '15'}
