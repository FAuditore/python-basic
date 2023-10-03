import keyword
from collections import abc


class A:
    def __init__(self, d):
        self.x = 1
        self.data = {}
        for k, v in d.items():
            # 处理关键字和非法标识符
            if keyword.iskeyword(k):
                k += '_'
            if not k.isidentifier():
                k = '_' + k
            self.data[k] = v
        self.data = dict(d)

    # 构造方法 __new__(cls)
    # 该类方法返回一个实例, 作为第一个参数传递给__init__(self)
    # 可以用来实现单例模式
    def __new__(cls, *args):
        if len(args) == 1 and isinstance(args[0], abc.Mapping):
            # super().__new__(cls) 表达式会调用 object.__new__(cls)
            return super().__new__(cls)
        elif isinstance(args, abc.Sequence):
            return (cls(item) for item in args)
        else:
            return args

    # getattr(object, name[, default]) 获取对象的属性值
    # 从对象中获取name字符串对应的属性
    # 获取的属性可能来自对象所属的类或超类
    # 如果没有指定的属性, 抛出 AttributeError 异常, 或者返回 default 参数的值
    def __getattr__(self, item):
        # hasattr(obj,name)查看对象是否有某个属性或方法(包括继承)
        # hasattr函数通过使用getattr()函数来检查对象是否抛出异常来检测
        if hasattr(self.data, item):
            return getattr(self.data, item)
        else:
            # warning: 查看不存在属性时会导致KeyError
            return self.data[item]


a, b = A({'name': 'abc', 'id': 123, 'class': '4', '5score': '5'},
         {"name": 'bcd'})

print(hasattr(a, '__init__'))  # True
print(hasattr(b, 'x'))  # True
print(a.id)  # 123 <=>a.__getattr__('id')


# print(b.id)  # KeyError: 'id'


# property(fget=None, fset=None, fdel=None, doc=None)
# 使用构造方法定义property
# 如果没有传某个函数, 则得到的property对象不允许执行某个操作
def non_negative(name):
    def fget(instance):
        return instance.__dict__[name]

    def fset(instance, value):
        if value >= 0:
            instance.__dict__[name] = value
        else:
            raise ValueError('value must >= 0')

    return property(fget=fget, fset=fset)


class Item:
    # 装饰器等价于构建property对象赋值给公开类属性
    price = non_negative('price')

    def __init__(self, desc, weight, price):
        self.desc = desc
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price

    # 使用property装饰器定义特性
    # 每个对self.weight的引用都会由特性函数处理 只有__dict__可以跳过特性处理逻辑
    @property
    def weight(self):
        # print('@property')
        return i.__weight

    @weight.setter
    def weight(self, value):
        # print('@setter')
        if value >= 0:
            self.__weight = value
        else:
            raise ValueError('weight must >= 0')

    @weight.deleter
    def weight(self):
        # print('@deleter')
        self.__weight = 0


# i = Item('test', -1, 0) #ValueError: weight must >= 0
# i = Item('test', 1, -1) # ValueError: value must >= 0
i = Item('test', 1, 1)
# del i.price #AttributeError: property 'price' of 'Item' object has no deleter
del i.weight
print(i.weight)  # 0
