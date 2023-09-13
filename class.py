import numbers
import pickle
import time
from collections import UserDict


class Car:
    # 类变量, 所有实例共有
    # 如果使用可变对象会导致所有实例互相影响
    author = 'zcx'

    def __init__(self, name, model):
        # 实例变量 每个实例独有
        self.name = name
        self.model = model

    def show(self):
        print(self.name, self.model)


a = Car(1, 2)
Car.show = lambda x: print(123)
a.show()  # 123


# inherit 继承Car
class ECar(Car):
    def __init__(self, name, model, battery):
        super().__init__(name, model)
        self.battery = battery
        # 带有一个下划线的名称 (例如 _spam) 约定当作是API的非公有部分
        # 双下划线私有属性会自动名称改写(name mangling)
        # 替换为_[类名]__[属性名]  _ECar__id
        self.__id = time.time()

    def __iter__(self):
        """
            变为可迭代对象 支持拆包
            *self
            name, model, battery = c
        """
        return (i for i in (self.name, self.model, self.battery))

    # property 实现访问控制 通过getter setter和deleter访问
    # 默认会生成一个getter
    @property
    def id(self):
        ...

    @id.getter
    def id(self):
        return self.__id

    def __bytes__(self):
        return pickle.dumps(self)

    # 类方法
    # 使用类调用(也可以使用实例调用) e.g. C.f() or C().f()
    # 第一个参数永远是类本身(不需要调用者传) cls表示类本身 self表示类的一个实例
    @classmethod
    def from_bytes(cls, bytes):
        return pickle.loads(bytes)

    # 静态方法
    # 使用类调用(也可以使用实例调用) e.g. C.f() or C().f() 本质就是普通函数
    @staticmethod
    def hello_world():
        print("hello world")

    def __hash__(self, h=0):
        for attr in self:
            h ^= hash(attr)
        return h

    def __eq__(self, other):
        for s, o in zip(self, other):
            if s != o:
                return False
        return True

    def show(self):
        print(*self)


c = ECar('byd', 'han', 'kylin')
c.show()
e = ECar.from_bytes(bytes(c))
e.show()
print(e is c)  # False
print(hash(e))

# 名称改写 e.__id AttributeError: 'ECar' object has no attribute '__id'
print(list(filter(lambda x: 'id' in x, dir(e))))  # ['_ECar__id']

# 访问控制 e.id = 5 AttributeError: property 'id' of 'ECar' object has no setter
e._ECar__id = 5

print(e.id is e._ECar__id)  # True
print(e.__dict__)  # {'name': 'byd', 'model': 'han', 'battery': 'kylin', '_ECar__id': 5}


class Student:
    # slots 规约类的所有属性, 值为一个可迭代的字符串对象
    # 实例不能使用 __slots__ 中所列名称之外的其他属性
    # 不再使用 __dict__ 字典保存所有属性, 使用定长列表分配, 节省内存, 加快访问属性速度
    # 子类不会继承 __slots__ 属性, 如果需要作为弱引用的对象, 需要在 __slots__ 中加入 '__weakref__'
    __slots__ = ('id', 'name')

    def __init__(self, id, name):
        self.id = id
        self.name = name
        # self.x = 1 AttributeError: 'Student' object has no attribute 'x'


s = Student(1, 'abc')


# print(s.__dict__) AttributeError: 'Student' object has no attribute '__dict__'.


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
# 因此, 需要定制 list, dict 或 str 类型时, 子类化 UserList, UserDict 或 UserString 更简单
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
        # 通过类调用实例方法,必须显式传入self参数,因为这样访问的是未绑定方法(unbound method)
        Daughter.pong(self)


d = Dog()
d.ping()  # father:  <__main__.Dog object at 0x104bdefd0>
d.pong()  # son:  <__main__.Dog object at 0x104bdefd0> 根据超类声明顺序调用
d.daughter_pong()  # daughter:  <__main__.Dog object at 0x104bdefd0>
print(Dog.__mro__)


# (<class '__main__.Dog'>, <class '__main__.Son'>, <class '__main__.Daughter'>,
# <class '__main__.Father'>, <class 'object'>)
# 方法解析顺序简单来说是深度优先, 从左至右, 不重复搜索
# 实际上动态算法会用一种特殊方式将搜索顺序线性化, 保留每个类所指定的从左至右的顺序,
# 只调用每个父类一次,并且保持单调（即一个类可以被子类化而不影响其父类的优先顺序）


# 查看方法解析顺序
def print_mro(cls):
    print(' '.join(c.__name__ for c in cls.__mro__))  # 生成器对象用空格隔开


print_mro(bool)  # bool int object
print_mro(numbers.Complex)  # Complex Number object
