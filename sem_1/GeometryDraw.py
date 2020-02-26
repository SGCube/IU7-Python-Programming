"""

Автор: Сорокин Антон ИУ7-12Б

Переменные:

"""
from tkinter import *
import matplotlib.pyplot as plt

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

M = []
print('Введите множество точек, построчно вводя координаты каждой точки.')
print('Завершите ввод двумя восклицательными знаками через пробел (! !).')
i = 0
while True:
    x = 0
    y = 0
    print(i+1,'-я точка:',sep='',end = ' ')
    while True:
        x,y = map(str,input().split())
        if (x == '!' and y == '!'):
            break
        if(correct_data(x) and correct_data(y)):
            x = float(x)
            y = float(y)
            M.append([x,y])
            break
        print('Некорректные данные! Введите заново!')
    if x == '!' and y == '!':
        break
    i += 1

if len(M) < 2:
    print('При заданном множестве выполнение задачи невозможно!')
else:
    found = False
    while True:
        r = input('Введите радиус окружности: ')
        if correct_data(r):
            r = float(r)
            break
        print('Некорректные данные! Введите заново!')
        
    i1 = 0
    i2 = 1
    k1 = 0
    k2 = 0
    m1 = 0
    m2 = 0
    while True:
        if i1 != i2:
            for i in range(len(M)):
                if i != i1:
                    if ((M[i1][0]-M[i][0])**2 + (M[i1][1]-M[i][1])**2) <= r:
                        k1 += 1
            for j in range(len(M)):
                if j != i2:
                    if ((M[i2][0]-M[j][0])**2 + (M[i2][1]-M[j][1])**2) <= r:
                        k2 += 1
        if (k1 == k2) and (k1 != 0):
            m1 = i1
            m2 = i2
            found = True
            break
        elif i2 < len(M)-1:
            i2 += 1
        elif i1 < len(M)-1:
            i1 += 1
            i2 = 0
        else:
            break

if found:
    print(i1,i2)
    
        
                
       
