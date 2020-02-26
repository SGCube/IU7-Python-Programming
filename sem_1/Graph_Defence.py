from math import sin

x1 = float(input('Введите начальное значение аргумента: '))
x2 = float(input('Введите конечное значение аргумента: '))
xd = float(input('Введите шаг изменения аргумента: '))
print()
eps = 1e-7
y = []
k = 0
n = 0
x = x1
if xd == 0:
    n = 1
else:
    n = abs((x2-x1)/xd) + eps
    
if (x1 < x2 and xd < 0) or(
    x1 > x2 and xd > 0) or(
    x1 != x2 and xd == 0):
    print('При заданном шаге конечное значение не достигается!')
else:
    while k < n:
        y.append(sin(x) - 5)
        if k == 0:
            ymin = y[0]
            ymax = y[0]
        elif y[k] < ymin:
            ymin = y[k]
        elif y[k] > ymax:
            ymax = y[k]
        k += 1
        x += xd

    n = k
    d = 8
    dk = 7
    s = d*dk

    if ymax == ymin:
        print('  ', end = '')
        print(dk*' ','{:7.3f}'.format(ymin),sep = '')
        print(6*' ','x ',7*'\u2500','\u2534',7*'\u2500',sep = '')
        print('{:8.3f}'.format(x1),7*' ','*',sep = '')
    else:
        k = 0
        yd = (ymax-ymin)/d
        if ymin > 0 or ymax < 0:
            pos0 = -1
            yc = ymin
        else:
            pos0 = round((0-ymin)/(ymax-ymin)*s)
            yc = pos0/dk*yd
        
        print('   ', end = '')
        while k <= s:
            if pos0 >= 0:
                if abs(k-pos0)%dk == 0:
                    if k == pos0:
                        print('      0',end = '')
                    else:
                        print('{:7.3f}'.format(yc),end = '')
                    k += dk
                    yc += yd
                else:
                    print(' ',end = '')
                    k += 1
            else:
                print('{:7.3f}'.format(yc),end = '')
                k += dk
                yc += yd
                
        print('\n',7*' ','x ',sep = '', end = '')
        k = 0
        while k <= s:
            if pos0 >= 0:
                if k == pos0:
                    print('\u253c',end = '')
                elif abs(k-pos0)%dk == 0:
                    print('\u2534',end = '')
                else:
                    print('\u2500',end = '')
            else:
                if k%dk == 0:
                    print('\u2534',end = '')
                else:
                    print('\u2500',end = '')
            k += 1
        print()

        k = 0
        x = x1
        while k < n:
            print('{:8.3f}'.format(x),end='')
            pos = round((y[k]-ymin)/(ymax-ymin)*s)
            if pos0 < 0 or (pos == pos0):
                print(pos*' ','*',sep=' ')
            else:
                if pos < pos0:
                    print(pos*' ','*',(pos0-pos-1)*' ','\u2502',sep=' ')
                else:
                    print(pos0*' ','\u2502',(pos-pos0-1)*' ','*',sep=' ')
            x += xd
            k += 1
