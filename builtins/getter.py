from operator import attrgetter, itemgetter

students = [
    ('bef', 1),
    ('abc', 3),
    ('qeq', 5),
    ('bda', 2),
]

# itemgetter
# Return a callable object that fetches the given item(s) from its operand
# f = itemgetter(2), the call f(r) returns r[2].
# g = itemgetter(2, 5, 3), the call g(r) returns (r[2], r[5], r[3])
# h = itemgetter('key'), the call h(r) returns r[key]
for stu in sorted(students, key=itemgetter(1)):
    print(itemgetter(0)(stu))
# bef bda abc qeq

print(itemgetter('name')({'name': 'aaa', 'age': 1}))  # aaa


class Student:
    def __init__(self, name, no):
        self.name = name
        self.no = no


students = [
    Student('bef', 1),
    Student('abc', 3),
    Student('qeq', 5),
    Student('bda', 2),
]

# attrgetter
# Return a callable object that fetches the given attribute(s) from its operand.
#  f = attrgetter('name'), the call f(r) returns r.name.
#  g = attrgetter('name', 'date'), the call g(r) returns (r.name, r.date).
#  h = attrgetter('name.first', 'name.last'), the call h(r) returns(r.name.first, r.name.last).
for stu in sorted(students, key=attrgetter('no')):
    print(attrgetter('name')(stu))
# bef bda abc qeq
