"""
Интегрирование функции
Автор: Сорокин Антон ИУ7-12Б

Переменные:
a - левый предел интегрирования
b - правый предел интегрирования
n - количество делений
h - шаг по x
I - значение интеграла
I1 - значение интеграла, посчитанного методом левых прямоугольников
I2 - значение интеграла, посчитанного методом парабол
i,j - итераторы
x - строка, подаваемая на проверку корректности данных
y - входная строка
c - элемент на удаление
x_temp - рабочая переменная 
fin - результат проверки на корректность
"""
from math import sin

def f(x):
    return x

def integ_lrect(a,b,n):
    h = (b-a)/n
    I = 0
    for j in range(n-1):
        I += f(a+j*h)
    I *= h
    return I

def integ_parabol(a,b,n):
    if n % 2 == 1:
        return -1
    h = (b-a)/n
    I = f(a)+f(b)
    for j in range(1,n,1):
        I += (2 + 2*(j%2)) * f(a+j*h)
    I *= h/3
    return I
    
def correct_data(x):
    def pop_first(y,c):
        i = y.find(c)
        if i != -1:
            y = y[:i] + y[(i+len(c)):]
        return y
    
    fin = True
    if x[0] == '-':
        x = x[1::1]
    x = pop_first(x,'.')
    x_temp = pop_first(x,'e-')
    if x_temp == x:
        x = pop_first(x,'e+')
    else:
        x = x_temp
    if not x.isdigit():
        fin = False
    return fin

while True:
    a,b = map(str,input('Введите через пробел пределы интегрирования: ').split())
    if correct_data(a) and correct_data(b):
        break
    print('Введите корректные пределы!')
while True:
    n = input('Введите количество разбиений: ')
    if n.isdigit():
        if int(n) > 0:    
            break
    print('Введите корректное количество делений!')
              
n = int(n)
a = float(a)
b = float(b)
I1 = integ_lrect(a,b,n)
I2 = integ_parabol(a,b,n)
print('\nf(x) = x*x+sin(x)')
print('Интеграл функции, посчитанный методом:')
print(' * левых прямоугольников: {:7.5f}'.format(I1))
if I2 == -1:
    print(' * методом парабол не вычисляется (n не кратно 2)')
else:
    print(' * парабол: {:7.5f}'.format(I2))
