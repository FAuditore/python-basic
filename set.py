# set 集合
# 通过散列表实现,集合里的元素必须是可散列的
# {element} 空集合: set()

s = set('cabbcbcabsbacb')
print(s)  # {'s', 'b', 'a', 'c'}

s2 = {*'abbabababf'}
print(s2)  # {'a', 'f', 'b'}

print(s & s2)  # {'a', 'b'}
print(s - s2)  # {'s', 'c'}
print(s | s2)  # {'a', 's', 'c', 'f', 'b'}
print(s ^ s2)  # {'f', 's', 'c'}

# set comprehension 集合推导
s = {chr(i) for i in range(0, 128)}
print(s)

# s.discard(e)如果集合中有e,则移除
s.discard('a')  # s->{'s', 'b', 'c'}

# s.remove(e) 如果有e则移除 如果没有e,则抛出KeyError
s.remove('a')
