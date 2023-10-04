# 描述符是实现了 __get__、__set__ 或 __delete__ 方法(任意一个)的对象
# 描述符的主要目的是提供一个挂钩, 允许存储在类变量中的对象控制在属性查找期间发生的情况
# 属性访问的默认行为是从一个对象的字典中获取、设置或删除属性, 对于实例来说
# a.x 的查找顺序会从 a.__dict__['x'] 开始, 然后是 type(a).__dict__['x']
# 接下来依次查找 type(a) 的方法解析顺序（MRO）
# 如果找到的值是定义了某个描述器方法的对象, 则 Python 可能会重写默认行为并转而发起调用描述器方法
# 通过实例调用
#     实例查找通过命名空间链进行扫描，数据描述器的优先级最高，其次是实例变量、非数据描述器、类变量
#     最后是 __getattr__() （如果存在的话）
# 通过类调用
#     像 A.x 这样的点操作符查找的逻辑在 type.__getattribute__() 中
# 通过 super 调用
#     super的点操作符查找的逻辑在 super() 返回的对象的 __getattribute__() 方法中
import abc


# 描述符类
class NonNegative:
    # 使用类变量统计实例数量
    __counter = 0

    # 当一个类使用描述符时, 它可以告知每个描述符使用了什么变量名
    # self是描述符实例, owner是托管实例
    # 这仅在描述符需要知道创建它的类或分配给它的类变量名称时使用
    def __set_name__(self, owner, name):
        cls = self.__class__
        self.storage_name = f'_{cls.__name__}#{cls.__counter}#{name}'
        cls.__counter += 1

    # 尝试为托管属性赋值时, 会调用描述符实例的__set__方法
    # self是描述符实例, instance是托管实例
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError
        else:
            # 管理实例属性的描述符应该把值存储在托管实例中
            # instance.__dict__[self.storage_name] = value
            setattr(instance, self.storage_name, value)

    # 如果 a.x 找到了一个描述符，那么将通过 desc.__get__(a, type(a))
    # 数据描述符始终会覆盖实例字典
    # 仅定义了__get__方法的描述符称为非数据描述符 非数据描述符会被实例字典覆盖(字典优先)
    # self是描述符实例, instance是托管实例, owner是托管类
    def __get__(self, instance, owner):
        # 如果不是实例调用, 返回描述符自身
        if instance is None:
            return self
        return getattr(instance, self.storage_name)

    def __delete__(self, instance):
        print(instance)
        del instance


# 托管类 把描述符实例声明为类属性的类
class Item:
    # 描述符仅在用作类变量时起作用
    weight = NonNegative()
    price = NonNegative()

    def __init__(self, w, p):
        self.weight = w
        self.price = p


i = Item(10, 5)
print(i.weight, i.price)  # 10,5
print(vars(i))  # {'_NonNegative#0#weight': 10, '_NonNegative#1#price': 5}


# 使用描述符实现自定义验证器
class Validator(abc.ABC):
    def __set_name__(self, owner, name):
        self.private_name = '_' + name

    def __get__(self, instance, owner):
        return getattr(instance, self.private_name)

    def __set__(self, instance, value):
        self.validate(value)
        setattr(instance, self.private_name, value)

    @abc.abstractmethod
    def validate(self, value):
        pass


class OneOf(Validator):

    def __init__(self, *options):
        self.options = set(options)

    def validate(self, value):
        if value not in self.options:
            raise ValueError(f'Expected {value!r} to be one of {self.options!r}')


class Number(Validator):
    def __init__(self, minvalue=None, maxvalue=None):
        self.minvalue = minvalue
        self.maxvalue = maxvalue

    def validate(self, value):
        if not isinstance(value, int | float):
            raise TypeError(f'Expected {value!r} to be an int or float')
        if self.minvalue is not None and value < self.minvalue:
            raise ValueError(f'Expected {value!r} to be at least {self.minvalue!r}')
        if self.maxvalue is not None and value > self.maxvalue:
            raise ValueError(f'Expected {value!r} to be no more than {self.maxvalue!r}')


class String(Validator):
    def __init__(self, minsize=None, maxsize=None, predicate=None):
        self.minsize = minsize
        self.maxsize = maxsize
        self.predicate = predicate

    def validate(self, value):
        if not isinstance(value, str):
            raise TypeError(f'Expected {value!r} to be an str')
        if self.minsize is not None and len(value) < self.minsize:
            raise ValueError(f'Expected {value!r} to be no smaller than {self.minsize!r}')
        if self.maxsize is not None and len(value) > self.maxsize:
            raise ValueError(f'Expected {value!r} to be no bigger than {self.maxsize!r}')
        if self.predicate is not None and not self.predicate(value):
            raise ValueError(f'Expected {self.predicate} to be true for {value!r}')


class TestValidator:
    name = String(minsize=3, maxsize=10, predicate=str.istitle)
    kind = OneOf('cat', 'dog', 'fish')
    quantity = Number(minvalue=0)

    def __init__(self, name, kind, quantity):
        self.name = name
        self.kind = kind
        self.quantity = quantity


# TestValidator('abc', 1, 'V')#ValueError: Expected <method 'istitle' of 'str' objects> to be true for 'abc'
# TestValidator('Abc', 1,'V')  # ValueError: Expected 1 to be one of {'dog', 'cat', 'fish'}
# TestValidator('Abc', 'dog', 'V')  # TypeError: Expected 'V' to be an int or float
TestValidator('Abc', 'dog', 1)
