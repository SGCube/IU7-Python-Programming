"""
Формирование массива цифр двоичного представления целого десятичного числа

Автор: Сорокин Антон ИУ7-12Б

Переменные:
x - число
digits - массив цифр
m,i - рабочие переменные
"""
from math import log
x = input('Введите целое число: ')

if x.isdigit():
    x = int(x)
    digits = []
    if x != 0:
        x = abs(x)  #если x отрицательное, то вычисляется по его модулю
        m = 2**(int(log(x)/(log(2))))
        
        while m >= 1:
            if x >= m:
                x -= m
                digits.append(1)
            else:
                digits.append(0)
            m /= 2
    else:
        digits.append(0)

    print('\nЦифры двоичной записи числа:')
    for i in range(len(digits)):
        print(digits[i],end = ' ')
else:
    print('Некорректные данные (введено не целое число)!')
