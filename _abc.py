import abc
from abc import ABC


class Lottery(abc.ABC):
    """
        Abstract Base Class, ABC抽象基类

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
