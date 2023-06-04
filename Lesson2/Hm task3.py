# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import random
from random import randint

n = randint(1, 1000)
print(n)
count = 0
while 2**count <= n:
    print(f'2 в степени {count} =', 2**count)
    count += 1
