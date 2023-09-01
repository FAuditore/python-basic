import numbers
from collections import UserDict


class MyDict(dict):
    # 内置类型的子类覆盖方法不会隐式调用
    def __setitem__(self, key, value):
        print('no set', self)
        return


d = MyDict(a=1, b=2, c=3)
print(d)  # {'a': 1, 'b': 2, 'c': 3}
d['c'] = 4  # no set {'a': 1, 'b': 2, 'c': 3}
d.update(c=5)
print(d)  # {'a': 1, 'b': 2, 'c': 5}


# __init__和update时忽略了覆盖的__setitem__ 没有在子类中搜索该方法

# 内置类型的原生方法使用 C 语言实现, 不会调用子类中覆盖的方法, 不过有极少数例外
# 因此，需要定制 list, dict 或 str 类型时, 子类化 UserList, UserDict 或 UserString 更简单
class MyDictV2(UserDict):
    def __setitem__(self, key, value):
        print('no set')


d = MyDictV2(a=1, b=2, c=3)  # no set no set no set
print(d)  # {}


class Father():
    def ping(self):
        print('father: ', self)


class Son(Father):
    def pong(self):
        print('son: ', self)


class Daughter(Father):
    def pong(self):
        print('daughter: ', self)


class Dog(Son, Daughter):

    def daughter_pong(self):
        # 通过类调用实例方法,必须显式传入self参数,因为这样访问的是未绑定方法(unbound method)。
        Daughter.pong(self)


d = Dog()
d.ping()  # father:  <__main__.Dog object at 0x104bdefd0>
d.pong()  # son:  <__main__.Dog object at 0x104bdefd0> 根据超类声明顺序调用
d.daughter_pong()  # daughter:  <__main__.Dog object at 0x104bdefd0>
print(Dog.__mro__)


# (<class '__main__.Dog'>, <class '__main__.Son'>, <class '__main__.Daughter'>,
# <class '__main__.Father'>, <class 'object'>)
# 子类在调用某个方法或变量的时候, 首先在自己内部查找, 如果没有找到, 开始根据继承机制在父类里查找


# 查看方法解析顺序
def print_mro(cls):
    print(' '.join(c.__name__ for c in cls.__mro__))  # 生成器对象用空格隔开


print_mro(bool)  # bool int object
print_mro(numbers.Complex)  # Complex Number object
