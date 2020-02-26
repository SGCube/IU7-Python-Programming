"""
Задачи программы:
- вычисление таблицы значений функции и построение его графика
- определить количество перемен знака функции

Автор: Сорокин Антон, ИУ7-12Б

x1 - начальное значение аргумента x
xd - шаг изменения аргумента
x2 - конечное значение аргумента x

p - список значений функции
pmin - минимальное значение функции
pmax - максимальное значение функции
z - количество перемен знака функции
coeff - коэффициенты полинома

Рабочие переменные:
eps - точность при сравнении (рабочая переменная)
m - минимальная величина, отображаемая на графике в формате e
k - счётчик
n - количество точек
d - длина деления на графике в символах
dk - количество делений
s - длина оси p в символах
pc - текущее значение p на оси Y
pd - шаг оси Y
pos0 - позиция нуля (оси X) в строке
pos - позиция точки (*) в строке

"""
x1 = float(input('Введите начальное значение аргумента: '))
xd = float(input('Введите шаг изменения аргумента: '))
x2 = float(input('Введите конечное значение аргумента: '))

coeff = [-1,0,5,0,-400,0,-1120,0,-1280,0,512]
p = []
eps = 1e-7
x = x1
k = 0
z = 0
if xd == 0:
    n = 1
else:
    n = abs((x2-x1)/xd) + eps

if (xd > 0) and (x1 > x2) or (
    xd < 0) and (x1 < x2) or (
    xd == 0) and (x1 != x2):
    print('Конечное значение при данном шаге не будет достигнуто.')
else:
    #нахождение значений функции p, а также её максимума и минимума
    while k < n:
        p.append(coeff[10])
        i = 9
        while i > -1:
            p[k] = p[k]*x + coeff[i]
            i -= 1
        if k == 0:
            pmin = p[0]
            pmax = p[0]
        else:
            if p[k] > pmax:
                pmax = p[k]
            elif p[k] < pmin:
                pmin = p[k]
        if (p[k] < 0 and p[k-1] > 0) or (p[k] > 0 and p[k-1] < 0):
            z += 1
        k += 1
        x += xd

    #"шапка" таблицы
    print('\u250c'+5*'\u2500'+'\u252c'+19*'\u2500'+'\u252c'+\
          19*'\u2500'+'\u2510')
    print('\u2502'+'  N  '+'\u2502'+9*' '+'x'+9*' '+'\u2502'+\
        9*' '+'p'+9*' '+'\u2502')
    print('\u251c'+5*'\u2500'+'\u253c'+19*'\u2500'+'\u253c'+\
          19*'\u2500'+'\u2524')

    #содержимое таблицы
    n = k
    k = 0
    x = x1
    while k < n:
        print('\u2502{:5d}\u007c'.format(k+1),end = '')
        if abs(x) < 1e+14:
            print('{:19.4f}\u007c'.format(x),end = '')
        else:
            print('{:19.4e}\u007c'.format(x),end = '')
        if abs(p[k]) < 1e+14:
            print('{:19.4f}\u2502'.format(p[k]))
        else:
            print('{:19.4e}\u2502'.format(p[k]))
        k += 1
        x += xd

    #нижняя граница таблицы
    print('\u2514'+5*'\u2500'+'\u2500'+19*'\u2500'+'\u2500'+\
          19*'\u2500'+'\u2518')

    print('\nКоличество перемен знака функции p: ',z,end = '\n\n')

    if n > 1:
        #поиск позиции нуля на оси p графика и выбор шага по этой оси
        d = 6
        dk = 10
        s = d*dk
        print(' ',end='')
        if (pmin > 0) or (pmax < 0):
            pos0 = s+1
        else:
            pos0 = round((0 - pmin)/(pmax - pmin)*s)
        pd = (pmax-pmin)/d
        m = 10**4

        #подпись значений на оси p
        if pos0 > s:
            pc = pmin
        else:
            pc = -pos0/dk*pd
        k = 0
        while k <= s:
            if pos0 <= s:
                if abs(k - pos0)%dk == 0:
                    if k == pos0:
                        print('        0',end = '')
                    elif abs(pc) < m:
                        print(' {:9.2f}'.format(pc),end = '')
                    else:
                        print(' {:9.2e}'.format(pc),end = '')
                    pc += pd
                    k += dk
                else:
                    print(' ',end = '')
                    k += 1
            else:
                if abs(pc) < m:
                    print(' {:9.2f}'.format(pc),end = '')
                else:
                    print(' {:9.2e}'.format(pc),end = '')
                pc += pd
                k += dk
        print('\n',7*' ','x ',sep = '', end = '')

        #построение оси p
        k = 0
        while k <= s:
            if pos0 <= s:
                if k == pos0:
                    print('\u253c',end = '')
                elif abs(k - pos0)%dk == 0:
                    print('\u2534',end = '')
                else:
                    print('\u2500',end = '')
            else:
                if abs(k)%dk == 0:
                    print('\u2534',end = '')
                else:
                    print('\u2500',end = '') 
            k += 1
        print(' p')

        #построение графика
        x = x1
        k = 0
        while k < n:
            print('{:8.3f}'.format(x),end = '')
            pos = round(((p[k]-pmin) / (pmax-pmin) * s))
            if pos <= pos0:
                print(pos*' ','*',end = '')
                if (pos < pos0) and (pos0 <= s):
                    print((pos0-1-pos)*' ','\u2502',sep = '', end = '')
            else:
                print((pos0+1)*' ','\u2502',sep = '', end = '')
                print((pos-pos0-1)*' ','*',sep = '', end = '')
            print()
            x += xd
            k += 1
    else:
        #построение одной точки на графике
        x = x1
        m = 10**4
        print(' ',end='')
        if abs(p[0]) < m:
            print(8*' ',' {:9.2f}'.format(p[0]))
        else:
            print(' {:9.2e}'.format(p[0]))
        print(7*' ','x ',sep = '', end = '')
        print(8*'\u2500','\u2534',8*'\u2500',sep = '', end = '')
        print(' p')
        print('{:8.3f}'.format(x),9*' ','*',sep = '')
