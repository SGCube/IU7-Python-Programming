"""
Программа поиска корней методом секущих

Исходная функция и константы указаны в подключаемом модуле graph

Переменные окон ввода:
var_a - левая граница интервала
var_b - правая граница интервала
var_h - шаг
var_eps - точность
var_n - максимальное количество итераций
msg - сообщение об ошибке или отсутствии корней

Автор: Сорокин Антон ИУ7-22Б
"""
from tkinter import *
from graph import *

#проверка корректности входных данных
def correct_data(s):
    #проверка на пустую строку
    if len(s) == 0:
        return False
    
    #проверка на знак минуса
    if s[0] == '-':
        s = s[1:]
        
    #наличие десятичной точки
    sym_find = s.find('.')
    if sym_find >= 0:
        s = s[:sym_find] + s[sym_find + 1:]
    
    #наличие символа e (экспоненциальная форма записи)
    sym_find = s.find('e')
    if sym_find >= 0:
        s = s[:sym_find] + s[sym_find + 1:]
        #знаки минуса или плюса в экспоненциальной записи
        sym_find = s.find('-')
        if sym_find >= 0:
            s = s[:sym_find] + s[sym_find + 1:]
        else:
            sym_find = s.find('+')
            if sym_find >= 0:
                s = s[:sym_find] + s[sym_find + 1:]

    return s.isdigit()

#функция поиска корней в интервале [a;b] с шагом step и точностью eps
#n - максимальное количество итераций
#is_output - нужно ли выводить в таблицу
def solution(a,b,step,eps,n,is_output):
    x_arr = []          #массив найденных корней
    x = ""              #корень на текущем интервале
    y = ""              #функция от корня
    a1 = a2 = a         #границы отрезка (в процессе поиска отрезка с корнем)
    k = 0               #количество элементарных отрезков с корнем

    while (a2 < b):
        error_code = 0  #код ошибки
        #переход к следующему элементарному отрезку
        a1 = a2
        a2 += step
        if a2 >= b:
            a2 = b
        
        y1 = func(a1)
        y2 = func(a2)

        #поиск корня на элементарном отрезке
        if y1*y2 <= 0:
            k += 1
            aa = a1     #последнее приближение корня
            bb = a2     #предпоследнее приближение корня
            i = 1       #счётчик проделанных итераций
            
            while (i <= n):
                #значения функции в приближённых значениях корня
                ya = func(aa)
                yb = func(bb)
                if abs(ya - yb) == 0:
                    error_code = 2  #деление на 0
                    break
                
                #новое приближение корня
                x = aa - ya*(bb - aa)/(yb - ya)
                if abs(x - bb) < eps:
                    if not (len(x_arr) > 0 and abs(x - x_arr[-1]) < 1e-20):
                        x_arr.append(x)
                    else:
                        error_code = -1
                        k -= 1
                    break

                #переход к следующей итерации
                bb = x
                i += 1
                    
            if i > n:
                error_code = 1  #превышение количества итераций

            #вывод информации
            if is_output and error_code >= 0:
                table_main[0].insert(END,k)
                table_main[1].insert(END,'{:>f};{:f}'.format(a1,a2))   
                if error_code == 0:
                    y = func(x)
                    table_main[2].insert(END,'{:f}'.format(x))
                    table_main[3].insert(END,'{:f}'.format(y))
                else:
                    table_main[2].insert(END,"---")
                    table_main[3].insert(END,"---")
                table_main[4].insert(END,i)
                table_main[5].insert(END,error_code)
	    	
    if k == 0 and is_output:
        msg.set('Корней на данном интервале нет!')

    return x_arr

#функция поиска экстремумов в интервале [a;b] с шагом step и точностью eps
#n - максимальное количество итераций
def extremum(a,b,step,eps,n):
    x_extr = []         #массив точек экстремумов
    x = ""              #корень на текущем интервале
    y = ""              #функция от корня
    a1 = a2 = a         #границы отрезка (в процессе поиска отрезка с корнем)
    k = 0               #количество элементарных отрезков с корнем

    while (a2 < b):
        #переход к следующему элементарному отрезку
        a1 = a2
        a2 += step
        if a2 > b:
            a2 = b

        y_p1 = func1(a1)
        y_p2 = func1(a2)
        
        #поиск экстремумов
        if y_p1*y_p2 <= 0:
            x1 = a1     #последнее приближение корня
            x2 = a2     #предпоследнее приближение корня
            i = 1       #счётчик проделанных итераций
            while (i <= n):
                #значения функции в приближённых значениях корня
                y_p1 = func1(x1)
                y_p2 = func1(x2)
                if abs(y_p1 - y_p2) == 0:
                    break
                
                #новое приближение корня
                x = x1 - y_p1*(x1 - x2)/(y_p1 - y_p2)
                if abs(x - x1) < eps:
                    x_extr.append(x)
                    break

                #переход к следующей итерации
                x2 = x1
                x1 = x
                i += 1

    return x_extr

#очистка таблицы и сообщений
def text_clear():
    for i in range(6):
        table_main[i].delete(0,END)
    msg.set('')

#подготовка к расчёту
def calculate():
    text_clear()
    
    a = var_a.get()
    b = var_b.get()
    h = var_h.get()
    eps = var_eps.get()
    n = var_n.get()

    if (correct_data(a) and correct_data(b) and correct_data(h)) and (
        correct_data(eps) and correct_data(n)):
        a = float(a)
        b = float(b)
        h = float(h)
        eps = float(eps)
        n = float(n)
        if eps <= 0:
            msg.set('Введена неположительная точность!')
        elif n <= 0:
            msg.set('Введено неположительное количество итераций!')
        elif h <= 0:
            msg.set('Введён неположительный шаг!')
        elif a > b:
            msg.set('Неправильно введён интервал (a > b)!')
        else:
            x_arr = solution(a,b,h,eps,n,True)
    else:
        msg.set('Некорректный ввод!')
        
#функция, запускающая рисование графика
def draw():
    a = var_a.get()
    b = var_b.get()
    if correct_data(a) and correct_data(b):
        a = float(a)
        b = float(b)
        if a <= b:
            x_arr = solution(a,b,step_const,eps_const,n_const, False)
            x_extr = extremum(a,b,step_const,eps_const,n_const)
            graph_draw(a,b,step_const,x_arr,x_extr)
        else:
            msg.set('Неправильно введён интервал (a > b)!')
    else:
        msg.set('Некорректный ввод интервала!')   

#функция, прокручивающая элементы таблицы вверх или вниз
def yview_all(s,arg1,arg2):
    if s == "moveto":
        for i in range(6):
            table_main[i].yview_moveto(arg1)
    else:
        for i in range(6):
            table_main[i].yview_scroll(arg1,arg2)

#создание окна
root = Tk()
root.title("Поиск корней")
root.resizable(False,False)

main_title = Label(root, text = "Поиск корней методом секущих функции " +
                   func_s, font = 16)
main_title.grid(row = 1, column = 1, columnspan = 5, padx = 8, pady = 8)

#поле ввода отрезка
var_a = StringVar()
var_b = StringVar()
ab_text = Label(root, text = "Отрезок")
ab_text.grid(row = 2, column = 1, columnspan = 2, padx = 8)
a_entry = Entry(root, textvariable = var_a, width = 16)
b_entry = Entry(root, textvariable = var_b, width = 16)
a_entry.grid(row = 3, column = 1, padx = 8, pady = 8)
b_entry.grid(row = 3, column = 2, padx = 8, pady = 8)

#поле ввода шага
var_h = StringVar()
h_text = Label(root, text = "Шаг")
h_text.grid(row = 2, column = 3, padx = 8)
h_entry = Entry(root, textvariable = var_h, width = 16)
h_entry.grid(row = 3, column = 3, padx = 8, pady = 8)

#поле ввода точности
var_eps = StringVar()
eps_text = Label(root, text = "Точность")
eps_text.grid(row = 2, column = 4, padx = 8)
eps_entry = Entry(root, textvariable = var_eps, width = 16)
eps_entry.grid(row = 3, column = 4, padx = 8, pady = 8)

#поле ввода количества итераций
var_n = StringVar()
n_text = Label(root, text = "Итерации")
n_text.grid(row = 2, column = 5, padx = 8)
n_entry = Entry(root, textvariable = var_n, width = 16)
n_entry.grid(row = 3, column = 5, padx = 8, pady = 8)

#сообщение (ошибка ввода/отсутствие корней на интервале)
msg = StringVar()
msg_label = Label(root, textvariable = msg, fg = 'red')
msg_label.grid(row = 4, column = 1, columnspan = 6)

#кнопки действий
btn_action = Button(root, text = "Найти корни", width = 24,
                    command = calculate)
btn_action.grid(row = 5, column = 1, columnspan = 3, padx = 8, pady = 8)
#кнопки рисования графика
btn_draw = Button(root, text = "График", width = 24, command = draw)
btn_draw.grid(row = 5, column = 4, columnspan = 3, padx = 8, pady = 8)

#создание таблицы
table = Frame(root)
table.grid(row = 6, column = 1, columnspan = 6, padx = 8, pady = 8)

#заголовок таблицы
table_header = []
table_header.append(Label(table, text = "#", justify = CENTER,
                          width = 4, relief = RIDGE))
table_header.append(Label(table, text = "[x(i);x(i+1)]",justify = CENTER,
                          width = 16, relief = RIDGE))
table_header.append(Label(table, text = "корень x",justify = CENTER,
                          width = 16,relief = RIDGE))
table_header.append(Label(table, text = "f(x)", justify = CENTER,
                          width = 16, relief = RIDGE))
table_header.append(Label(table, text = "кол-во итераций", justify = CENTER,
                          width = 16, relief = RIDGE))
table_header.append(Label(table, text = "код ошибки", justify = CENTER,
                          width = 16, relief = RIDGE))
for i in range(6):
    table_header[i].grid(row = 1, column = i + 1)

#основное содержимое таблицы
table_scroll = Scrollbar(table)

table_main = []
table_main.append(Listbox(table, width = 5, height = 8,
                          yscrollcommand = table_scroll.set))
table_main.append(Listbox(table, width = 19, height = 8,
                          yscrollcommand = table_scroll.set))
table_main.append(Listbox(table, width = 19, height = 8,
                          yscrollcommand = table_scroll.set))
table_main.append(Listbox(table, width = 19, height = 8,
                          yscrollcommand = table_scroll.set))
table_main.append(Listbox(table, width = 19, height = 8,
                          yscrollcommand = table_scroll.set))
table_main.append(Listbox(table, width = 19, height = 8,
                          yscrollcommand = table_scroll.set))

for i in range(6):
    table_main[i].grid(row = 2, column = i + 1)

table_scroll.config(command = yview_all)
table_scroll.grid(row = 2, column = 7)

#информации о кодах ошибки
error_info = Label(root, text = "Расшифровка кодов ошибок:")
error_info.grid(row = 7, column = 1, columnspan = 6)
Label(root, text = "0 - ошибки нет").grid(row = 8, column = 1,
                                          columnspan = 1)
Label(root, text = "1 - превышение количества итераций").grid(row = 8,
                                                              column = 2,
                                                              columnspan = 2)
Label(root, text = "2 - деление на 0 при вычислении").grid(row = 8,
                                                           column = 4,
                                                           columnspan = 2)

root.mainloop()
