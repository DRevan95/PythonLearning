# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     3
#     -> 1

import random
from random import randint

N = int(input("Сколько элементов будет в массив? "))
firstList = []
count = 0
for i in range(N):
    firstList.append(randint(1, 9))
print(firstList)

x = int(input("Введите число, которое хотите найти: "))
for element in firstList:
    if element == x:
        count += 1
print(f"Число {x} встречается в массиве {count} раз")
