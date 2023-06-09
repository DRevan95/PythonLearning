# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

# *Пример:*

# 5
#     1 2 3 4 5
#     6
#     -> 5

import random
from random import randint

N = int(input("Сколько элементов будет в массиве? "))
firstList = []
for i in range(N):
    firstList.append(randint(1, 9))
print(firstList)


nearestNumber = firstList[0]
x = int(input("Введите число: "))
for el in firstList:
    if el == (x-1):
        nearestNumber = x-1
print(f"Ближайшее значение к числу {x}: {nearestNumber}")
