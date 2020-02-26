from math import sin

def f(x):
    return sin(x)

def root_search(a,b,eps,n):
    if f(a) == 0:
        return a,1,0
    if f(b) == 0:
        return b,1,0
    
    # 1-я итерация
    x1 = a
    i = 1
    while i <= n:
        x = (a + b)/2
        if abs(x - a) < eps or abs(x - b) < eps:
            return x, i, 0
        if f(a)*f(x) > 0:
            a = x
        else:
            b = x
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
    print("Выполнено итераций:",root[1])
