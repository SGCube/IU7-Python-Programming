"""
Сортировка массива
Автор: Сорокин Антон ИУ7-12Б

Переменные:
s - строка входных данных (массива)
x - массив чисел

Функции, их аргументы и переменные

Функция sort - функция сортировки массива метода Хоара:
аргумент c - массив, который нужно отсортировать
lenc - длина массива
ibase,i - рабочая переменная
a - массив чисел больших, чем c[ibase] (рабочий массив)
b - массив чисел меньших, чем c[ibase] (рабочий массив)
d - отсортированый массив c

Функция correct_data - функция проверки строки на численный массив
аргумент a - входная строка
fin - является ли численным массив (boolean)
k,k_temp - рабочие переменные

Функция pop_first - функция удаления из строки первого вхождения символа
аргумент b - входная строка
аргумент c - символ на удаление
i - рабочая переменная
"""
from random import randint

def sort(c):
    lenc = len(c)
    ibase = randint(0,lenc-1)
    a = []
    b = []
    for i in range(lenc):
        if i != ibase:
            if c[i] <= c[ibase]:
                a.append(c[i])
            else:
                b.append(c[i])
    if len(a) > 0:
        a = sort(a)
    if len(b) > 0:
        b = sort(b)
    d = []
    for i in range(len(a)):
        d.append(a[i])
    d.append(c[ibase])
    for i in range(len(b)):
        d.append(b[i])
    return d

def correct_data(a):
    def pop_first(b,c):
        i = b.find(c)
        if i != -1:
            b = b[:i] + b[(i+len(c)):]
        return b
    
    fin = True
    for k in a:
        if k[0] == '-':
            k = k[1::1]
        k = pop_first(k,'.')
        k_temp = pop_first(k,'e-')
        if k_temp == k:
            k = pop_first(k,'e+')
        else:
            k = k_temp
        if not k.isdigit():
            fin = False
    return fin

s = list(map(str,input('Введите массив через пробел: ').split()))
if correct_data(s):
    x = [float(i) for i in s]
    x = sort(x)
    print(x)
else:
    print('Некорректные данные!')
