# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

import random
from random import randint
n = int(input("Введите количество монет: "))
headsCount = 0
tailsCount = 0
for i in range(n):
    x = randint(0, 1)
    print(x)
    if x == 1:
        headsCount += 1
    else:
        tailsCount += 1
if headsCount > tailsCount:
    print(f"Нужно перевернуть: {tailsCount} монет")
else:
    print(f"Нужно перевернуть: {headsCount} монет")
