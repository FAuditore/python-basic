import abc
import random

"""
    abc Abstract Base Class, 抽象基类
    该模块提供了一个元类 ABCMeta, 可以用来定义抽象类 
    另外还提供一个工具类 ABC, 可以用它以继承的方式定义抽象基类 
    class ABCMeta(type)
        Use this metaclass to create an ABC.  An ABC can be subclassed
        directly, and then acts as a mix-in class.  You can also register
        unrelated concrete classes (even built-in classes) and unrelated
        ABCs as 'virtual subclasses' -- these and their descendants will
        be considered subclasses of the registering ABC by the built-in
        issubclass() function, but the registering ABC won't show up in
        their MRO (Method Resolution Order) nor will method
        implementations defined by the registering ABC be callable (not
        even via super()).
"""


class Lottery(abc.ABC):

    # 定义抽象方法 元类必须继承自ABCMeta
    # 子类必须实现所有抽象方法, 否则无法实例化
    # @abstractmethod 抽象方法装饰器 和def语句之间不能有其他装饰器 (其他装饰器只能放在上面)
    @abc.abstractmethod
    def pick(self):
        """抽奖"""

    @abc.abstractmethod
    def set(self, iterable):
        """放置奖品"""

    # 抽象基类可以提供具体方法, 使用接口中的其他方法
    # 子类可以覆盖
    def show(self):
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.set(items)
        return tuple(sorted(items))


class Slot(Lottery):
    def __init__(self, items):
        self._items = []
        self.set(items)

    def pick(self):
        return self._items.pop()

    def set(self, iterable):
        self._items.extend(iterable)

    def __len__(self):
        return len(self._items)


# class collections.abc.Sized 提供了 __len__() 方法的抽象基类
# https://docs.python.org/zh-cn/3.11/library/collections.abc.html
from collections.abc import Sized

print(isinstance(Slot([]), Sized), issubclass(Slot, Sized))  # True


# 虚拟子类
# 注册的类会变成抽象基类的虚拟子类, issubclass 和 isinstance 等函数都能识别
# 但是注册的类不会从抽象基类中继承任何方法或属性
# 虚拟子类不会继承注册的抽象基类, 而且任何时候都不会检查它是否符合抽象基类的接口, 即便在实例化时也不会检查

# 注册成Lottery的虚拟子类 不会继承方法和属性 类型检查会通过
@Lottery.register
class SlotV2(list):
    def pick_v2(self):
        # 从list继承的__bool__ 不为空时为True
        if self:
            return self.pop(random.randrange(len(self)))
        else:
            raise LookupError('empty list')

    # 类属性(方法),与list实现一样
    set_v2 = list.extend


print(issubclass(SlotV2, Lottery))  # True
print(isinstance(SlotV2(), Lottery))  # True
print(SlotV2.__mro__)  # (<class '__main__.SlotV2'>, <class 'list'>, <class 'object'>) mro 方法解析顺序
print(Lottery.__subclasses__())  # [<class '__main__.Slot'>]
