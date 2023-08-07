import pickle
import time


class Car:
    # 类属性, 所有实例共有
    author = 'zcx'

    def __init__(self, name, model):
        self.name = name
        self.model = model

    def show(self):
        print(self.name, self.model)


# inherit 继承Car
class ECar(Car):
    def __init__(self, name, model, battery):
        super().__init__(name, model)
        self.battery = battery
        # 双下划线代表私有属性
        # 自动名称改写(name mangling) 替换为_[类名]__[属性名]  _ECar__id
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
