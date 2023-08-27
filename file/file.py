# with .. as <==> try .. except .. finally ..
# returned value assigned to the variable after as
with open('1.txt', 'w') as f:
    f.write('abc\ndef')

with open('1.txt', 'r') as f:
    for line in f.readlines():
        print(line)
