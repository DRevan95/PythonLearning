# Задача 2: Найдите сумму цифр трехзначного числа.

number = int(input('Введите трёхзначное число: '))
sum = 0
if 99 < number < 1000:
    while number > 1:
        sum += number % 10
        number = number // 10
else:
    print('Неверное число.')
print(sum)
