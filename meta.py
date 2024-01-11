import collections


def record_factory(cls_name, field_names):
    try:
        field_names = field_names.replace(',', ' ').split()
    except AttributeError:
        pass

    # 新建类的__init__方法
    def __init__(self, *args, **kwargs):
        # 设置新建类的__slots__属性
        attrs = dict(zip(self.__slots__, args))
        attrs.update(kwargs)
        for name, value in attrs.items():
            setattr(self, name, value)

    # 新建类的迭代方法
    def __iter__(self):
        for name in self.__slots__:
            yield getattr(self, name)

    # 新建类的格式化方法
    def __repr__(self):
        values = ', '.join('{}={!r}'.format(*i) for i
                           in zip(self.__slots__, self))
        return '{}({})'.format(self.__class__.__name__, values)

    # 组建类属性字典
    cls_attrs = dict(__slots__=field_names,
                     __init__=__init__,
                     __iter__=__iter__,
                     __repr__=__repr__)

    # 调用type方法构建新类
    # 默认情况下, 类是使用 type() 来构建的
    # 类名会被局部绑定到type(name, bases, dict,**kwds)的结果
    # name 字符串即类名并会成为 __name__ 属性
    # bases元组包含基类并会成为 __bases__ 属性
    # dict 字典包含类主体的属性和方法定义, 它在成为 __dict__ 属性之前可能会被拷贝或包装
    # class X:
    #   a = 1
    # 等价于X = type('X', (), dict(a=1))
    return type(cls_name, (object,), cls_attrs)


Dog = record_factory("Dog", "name weight owner")
rex = Dog("Rex", 30, "Bob")
print(rex)  # Dog(name='Rex', weight=30, owner='Bob')


class EntityMeta(type):
    """元类 用于创建带有验证字段的业务实体"""

    # __prepare__方法
    # __prepare__方法要求使用@classmethod装饰器定义并且该方法会在__new__之前被调用
    # 其返回值为一个映射, 该映射用于接受attr_dict
    @classmethod
    def __prepare__(cls, name, bases):
        temp = collections.OrderedDict()
        temp['abc'] = 123
        return temp

    def __init__(cls, name, bases, attr_dict):
        super().__init__(name, bases, attr_dict)


class Entity(metaclass=EntityMeta):
    ...


class Item(Entity):
    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price


for name in Item.__dict__.items():
    print(name)


# ('abc', 123)
# ('__module__', '__main__')
# ('__init__', <function Item.__init__ at 0x104fe2ac0>)
# ('__doc__', None)


