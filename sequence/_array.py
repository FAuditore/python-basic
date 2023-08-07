"""
    Type code   C Type             Minimum size in bytes
    'b'         signed integer     1
    'B'         unsigned integer   1
    'u'         Unicode character  2 (see note)
    'h'         signed integer     2
    'H'         unsigned integer   2
    'i'         signed integer     2
    'I'         unsigned integer   2
    'l'         signed integer     4
    'L'         unsigned integer   4
    'q'         signed integer     8 (see note)
    'Q'         unsigned integer   8 (see note)
    'f'         floating point     4
    'd'         floating point     8
"""
from array import array
from random import random

floats = array('d', (random() for _ in range(100)))
print(floats[-5:])

# fp = open('floats.txt', 'rb')
# floats.tofile(fp)
# floats.fromfile(fp, 100)
