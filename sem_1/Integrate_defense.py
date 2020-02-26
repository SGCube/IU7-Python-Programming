from math import sin
def f(x):
    # return x*x + sin(x)
    return x

def integrate_divide(a,b,n):
    I = 0
    h = (b-a)/n
    for j in range(0,n-2,3):
        I += f(a+h*j) + 3*f(a+h*(j+1)) + 3*f(a+h*(j+2)) + f(a+h*(j+3))
    I *= h*3/8
    return I

def integrate_eps(a,b,eps):
    n = 3
    I2 = integrate_divide(a,b,n)
    if I2 > eps:
        while True:
            I1 = I2
            n *= 2
            I2 = integrate_divide(a,b,n)
            if abs(I2 - I1) < eps:
                break
    return I2

a = float(input('Введите нижний предел интегрирования: '))
b = float(input('Введите верхний предел интегрирования: '))
n = int(input('Введите число разбиений n: '))
eps = float(input('Введите точность вычислений eps: '))

if n % 3 != 0:
    print('\nПри заданном количестве разбиений вычислить интеграл')
    print('методом 3/8 невозможно.')
else:
    I1 = integrate_divide(a,b,n)
    print('\nИнтеграл, вычисленный с количеством разбиений n: ','{:9.7f}'.format(I1))
I2 = integrate_eps(a,b,eps)
print('Интеграл, вычисленный с точностью eps: ','{:9.7f}'.format(I2))
