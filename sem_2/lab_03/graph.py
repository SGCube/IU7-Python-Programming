"""
Модуль, выполняющий графическое изображение функции на указанном интервале

Автор: Сорокин Антон ИУ7-22Б
"""
import matplotlib.pyplot as plt
import numpy as np
from math import sin, cos

func_s = 'x*x - 1'
#константы
step_const = 1e-03  #константа шага
eps_const = 1e-09   #константа точности
n_const = 100       #константа максимального количества итераций

#исходная функция
def func(x):
    return x*x - 1

#производная исходной функции
def func1(x):
    return 2*x

#функция, рисующая график
def graph_draw(a,b,h,x_arr,x_extr):
    plt.clf()
    plt.title(func_s)
    n = 100                                 #количество точек
    x = np.linspace(a,b,n)                  #значения х на интервале
    y = [func(xi) for xi in x]              #значения y на интервале
    y_arr = [func(xi) for xi in x_arr]      #значения y в точках корней
    y_extr = [func(xi) for xi in x_extr]    #экстремумы

    #подписи и сетка
    plt.xlabel('x')
    plt.ylabel(func_s)
    plt.grid(True)

    #график функции
    plt.plot(x,y,'r-',color = 'blue',linewidth = 2)
    #корни
    plt.plot(x_arr,y_arr,'rs',color = 'red',linewidth = 1)
    plt.plot(x_extr,y_extr,'ro',color = 'green',linewidth = 1)

    plt.legend(("f(x)","solutions","extremums"))

    plt.show()

if __name__ == '__main__':
    graph_draw(-1,1,0.01,[],[])
