# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета.

number = int(input('Введите номер билета: '))
sum1 = 0
sum2 = 0
if 99999 < number < 1000000:
    firstNumber = number // 1000
    secondNumber = number % 1000

    while firstNumber > 0:
        sum1 += firstNumber % 10
        firstNumber = firstNumber // 10

    while secondNumber > 0:
        sum2 += secondNumber % 10
        secondNumber = secondNumber // 10
    print(sum1)
    print(sum2)
    if sum1 == sum2:
        print('Ваш билет счастливый!')
    else:
        print('Увы(((')
else:
    print('Неверное число. Номер билета состоит из 6 цифр.')
