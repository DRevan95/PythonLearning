# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек, если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника). Числа вводятся построчно.

length = int(input('Введите длину шоколадной плитки(в дольках): '))
width = int(input('Введите ширину шоколадной плитки(в дольках): '))
k = int(input('Сколько долек вы хотите отломить? '))
if k == length*width:
    print('Хотите забрать всю шоколадку?')
elif k % length == 0 or k % width == 0:
    print('Верно')
else:
    print('Неверно')
