from math import sin

def f(x):
    return sin(x)

def root_search(a,b,eps,n):
    if f(a) == 0:
        return a,1,0
    if f(b) == 0:
        return b,1,0
    
    # 1-я итерация
    i = 1
    while i <= n:
        if f(b) - f(a) == 0:
            return '-', i, 2
        x = a - (b - a) * f(a) / (f(b) - f(a))
        if abs(x - b) < eps or abs(a - x) < eps:
            return x, i, 0
        if f(a)*f(x) < 0:  
            b = x
        else:
            a = x
        i += 1

    return '-', i, 1

a = float(input("Введите a: "))
b = float(input("Введите b: "))
eps = float(input("Введите точность: "))
n = int(input("Введите кол-во итераций: "))

if f(a)*f(b) > 0:
    print("Нет решений на данном интервале!")
else:
    root = root_search(a,b,eps,n)
        
    if root[0] != '-':
        print("x = {:.4f}".format(root[0]),
              "y = {:.3e}".format(f(root[0])),
              sep = '\t')
    else:
        print('Решение не найдено:', end = ' ')
        if root[2] == 1:
            print("превышено максимальное количество итераций")
        if root[2] == 2:
            print("деление на 0")
    print("Выполнено итераций:",root[1])
