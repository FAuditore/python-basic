# list 列表
# [element]
l = ['2', '1', '3', '4', '5']

del l[0]
l.reverse()  # l -> ['5', '4', '3', '1']
newL = sorted(l)  # newL -> ['1', '3', '4', '5'] l不变
l.sort(reverse=False, key=int)  # l - > ['1', '3', '4', '5'] key=int(element)

suits = 'spades diamonds clubs hearts'.split()
# ['spades', 'diamonds', 'clubs', 'hearts']

# list comprehension 列表推导
# l=[expr]
ranks = [str(n) for n in range(2, 11)] + list('JQKA')
# ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
# [i for i in range(0,10)] 等价于 list(range(0,10))

cards = [(suit, rank) for suit in suits
         for rank in ranks]
# [('spades', '2'), ('spades', '3'), ('spades', '4'),...
