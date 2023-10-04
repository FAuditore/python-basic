# 实现了 __get__、__set__ 或 __delete__ 方法的类是描述符
# 描述符的主要目的是提供一个挂钩，允许存储在类变量中的对象控制在属性查找期间发生的情况
# 托管类 把描述符实例声明为类属性的类

# 描述符类
class NonNegative:
    # 使用类变量统计实例数量
    __counter = 0

    def __init__(self):
        cls = self.__class__
        self.storage_name = f'_{cls.__name__}#{cls.__counter}'
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

    # self是描述符实例, instance是托管实例, owner是托管类的引用
    def __get__(self, instance, owner):
        # 如果不是实例调用, 返回描述符自身
        if instance is None:
            return self
        return getattr(instance, self.storage_name)


class Item:
    # 描述符仅在用作类变量时起作用。放入实例时，它们将失效
    weight = NonNegative()
    price = NonNegative()

    def __init__(self, w, p):
        self.weight = w
        self.price = p


i = Item(10, 5)
print(i.weight, i.price)  # 10,5
print(Item.weight.storage_name, Item.price.storage_name)  # _NonNegative#0 _NonNegative#1
