import func
func.my_sum(1, 2)

from func import my_sum
my_sum(1, 2)

from func import *
my_sum(1, 2)

from func import my_sum as m
m(1, 2)
