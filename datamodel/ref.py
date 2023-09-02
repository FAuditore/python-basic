# 弱引用: https://docs.python.org/3/library/weakref.html
#     对对象的弱引用不能保证对象存活: 当对像的引用只剩弱引用时可能被销毁
#     garbage collection 可以销毁引用并将其内存重用于其他内容
#     但是, 在实际销毁对象之前, 即使没有强引用, 弱引用也一直能返回该对象
#     多应用用途是实现保存大对象的高速缓存或映射, 但又不希望大对象仅仅因为它出现在高速缓存或映射中而保持存活
#     list和dict不能作为弱引用指向的对象, 子类可以
# for循环中的变量是全局变量, 除非显式删除, 否则不会消失
# 为现有的变量赋予新值, 不会修改之前绑定的变量。这叫重新绑定: 现在变量绑定了其
# 他对象。如果变量是之前那个对象的最后一个引用, 对象会被当作垃圾回收
import weakref

s1 = {1, 2, 3}
s2 = s1

ender = weakref.finalize(s1, lambda: print('bye'))
wrf = weakref.ref(s1)

print(wrf(), ender.alive)  # {1, 2, 3} True
del s1  # del 不删除对象,只删除引用
print(wrf(), ender.alive)  # {1, 2, 3} True
s2 = 1  # bye
print(wrf(), ender.alive)  # None False


class T:
    def __init__(self, s):
        self.s = s

    def __repr__(self):
        return self.s


# WeakKeyDictionary 键是弱引用,引用对象删除后条目会自动删除
# 键要求是可散列类型
wkd = weakref.WeakKeyDictionary()
t1 = T('a')
t2 = t1
wkd[t1] = 1  # {a: 1}
del t1  # {a: 1}
del t2  # {}

# WeakValueDictionary 值是弱引用,被引用对象删除后条目会自动删除
wvd = weakref.WeakValueDictionary()
s1 = {1, 2, 3}
wvd['a'] = s1  # {'a': {1, 2, 3}}
del s1  # {}
