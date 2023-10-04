# set 集合
# 表示由不重复且不可变对象组成的无序且有限的集合
# 不能通过下标来索引, 但是可被迭代和len()返回条目数
# 通过散列表实现, 集合里的元素必须是可散列的
# set([iterable]) 空集合: set()

s = set('cabbcbcabsbacb')
print(s)  # {'s', 'b', 'a', 'c'}

s2 = {*'abbabababf'}
print(s2)  # {'a', 'f', 'b'}

# set comprehension 集合推导
alphabet = {chr(i) for i in range(97, 123)}
print(alphabet)

# s.discard(e)如果集合中有e,则移除
s.discard('a')  # s->{'s', 'b', 'c'}

# s.remove(e) 如果有e则移除 如果没有e,则抛出KeyError
# s.remove('a')

print(s & s2)  # {'a', 'b'}
print(s - s2)  # {'s', 'c'}
print(s | s2)  # {'a', 's', 'c', 'f', 'b'}
print(s ^ s2)  # {'f', 's', 'c'}
print(s.pop(), s)  # b {'a', 's', 'c'} 移除并返回任意一个元素

# frozenset冻结集合
# 集合中不能添加或删除任何元素
# frozenset([iterable])
fs = frozenset([1, 2, 3, 2])
print(fs)  # frozenset({1, 2, 3})
