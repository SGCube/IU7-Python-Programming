x = float(input('Введите аргумент x: '))
eps = float(input('Введите точность eps: '))
nmax = int(input('Введите максимальное количество итераций: '))
step = int(input('Введите шаг: '))
print()

print(4*' ','k',4*' ','\u2502',7*' ','x',7*' ','\u2502',
      7*' ','a',7*' ','\u2502',7*' ','s',7*' ',sep = '')
print(9*'\u2500','\u253c',15*'\u2500','\u253c',
      15*'\u2500','\u253c',15*'\u2500',sep = '')

k = 1
a = 1
s = a

print('{:9d}'.format(k),end = '\u2502')
if 10**(-4) < abs(x) < 10**8:
    print('{:15.4f}'.format(x),end = '\u2502')
else:
    print('{:15.4e}'.format(x),end = '\u2502')
if 10**(-4) < abs(a) < 10**8:
    print('{:15.4f}'.format(a),end = '\u2502')
else:
    print('{:15.4e}'.format(a),end = '\u2502')
if 10**(-4) < abs(s) < 10**8:
    print('{:15.4f}'.format(s))
else:
    print('{:15.4e}'.format(s))

f = -1

while (abs(a) >= eps) and (k < nmax):
    
    a *= -f*x/(2*k)
    f += 2
    k += 1
    s += a
    
    if (k-1) % step == 0:
        print('{:9d}'.format(k),end = '\u2502')
        if 10**(-4) < abs(x) < 10**8:
            print('{:15.4f}'.format(x),end = '\u2502')
        else:
            print('{:15.4e}'.format(x),end = '\u2502')
        if 10**(-4) < abs(a) < 10**8:
            print('{:15.4f}'.format(a),end = '\u2502')
        else:
            print('{:15.4e}'.format(a),end = '\u2502')
        if 10**(-4) < abs(s) < 10**8:
            print('{:15.4f}'.format(s))
        else:
            print('{:15.4e}'.format(s))

print('\n')
if (abs(a) >= eps):
    print('Ряд не сошёлся за {:d} итераций.'.format(nmax))
else:
    iter_str = 'итераций.'
    if not(10 < k%100 < 20):
        if k%10 == 1:
            iter_str = 'итерацию.'
        elif 1 < k%10 < 5:
            iter_str = 'итераций.'
    print('Ряд сошёлся за {:d}'.format(k),iter_str)
    print('Сумма ряда: ',s)
