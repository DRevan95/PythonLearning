# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

sum = int(input('Введите общее количество журавликов: '))
if sum % 6 == 0:
    n = sum // 6
    m = (n+n)*2  # или n*4
    print(f'Петя и Серёжа сделали по {n} журавликов, а Маша {m} журавликов')
else:
    print('Невозможно посчитать...')
