from math import sin

def f(x):
    return sin(x)

def fi(x):
    return x + f(x)

def fir(x):
    return x - f(x)

def simp_it_clockwise(x0,x1,eps,n,ib):
    for i in range(ib,n+1):
        if abs(x0 - x1) < eps:
            return x1, i,0
        if a <= x1 <= b:
            x0, x1 = x1, fi(x1)
        else:
            x0, x1 = x1, fir(x1)
    else:
        return '-',n,1

def simp_it_counterclockwise(x0,x1,eps,n,ib):
    for i in range(ib,n+1):
        if abs(x0 - x1) < eps:
            return x1, i,0
        if a <= x1 <= b:
            x0, x1 = x1, fir(x1)
        else:
            x0, x1 = x1, fi(x1)
    else:
        return '-',n,1

def root_search(a,b,eps,n):
    if f(a) == 0:
        return a,1,0
    if f(b) == 0:
        return b,1,0
    
    x0 = a
    x1 = fi(x0)
    # 1-я итерация
    x0, x1 = x1, fi(x1)

    if a <= x1 <= b:
        return simp_it_clockwise(x0,x1,eps,n,1)
    else:
        x0 = b
        x1 = fi(x0)
        x0, x1 = x1, fi(x1)

    if a <= x1 <= b:
        return simp_it_clockwise(x0,x1,eps,n,2)
    else:
        x0 = b
        x1 = fir(x0)
        x0, x1 = x1, fir(x1)

    if a <= x1 <= b:
        return simp_it_counterclockwise(x0,x1,eps,n,3)
    else:
        x0 = a
        x1 = fir(x0)
        x0, x1 = x1, fir(x1)

    if a <= x1 <= b:
        return simp_it_counterclockwise(x0,x1,eps,n,4)
    else:
        return '-',0,2

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
            print("выход за границу интервала")
    print("Выполнено итераций:",root[1])
