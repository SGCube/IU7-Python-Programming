"""
Программа, изкучающая время сортировки различных массивов

Основные переменные:
arr_n - массив значений полей для размерностей массивов
sort_time - матрица значений полей для вывода времён работы
arr_check - строка с массивом на проверку работы сортировки
arr_result - строка с отсортированным массивом

Автор: Сорокин Антон ИУ7-22Б
"""
from random import randint
from tkinter import *
import time

#функция, проверяющая входные данные (количество элементов)
def correct_data():
    #инициализация рабочих переменных
    arr_new_n = []  #массив количеств элементов
    ok = [1,1,1]    #статус каждого введённого значения
    ok_sum = True   #общий статус ввода

    #обработка входных данных
    for i in range(3):
        x = arr_n[i].get()
        if x.isdigit():
            x = int(x)
            if x > 0:
                arr_new_n.append(int(x))
            else:
                ok[i] = 0
        else:
            ok[i] = -1

    #вывод информации в случае ошибки
    text_info.config(state = NORMAL)
    text_info.delete(1.0,END)
    for i in range(3):
        if ok[i] == -1:
            s = "Некорректный ввод числа №" + str(i+1) + "\n"
            text_info.insert(END, s)
            ok_sum = False
        elif ok[i] == 0:
            s = "Количество элементов массива должно быть больше 0"
            s += " (число №" + str(i+1) + ")\n"
            text_info.insert(END, s)
            ok_sum = False
    text_info.config(state = DISABLED)
    
    if ok_sum:
        return arr_new_n
    else:
        return [0,0,0]

#функция, проверяющая входной массив в виде строки
def array_check(s_arr):
    ok = True
    arr_x = s_arr.split()
    for i in range(len(arr_x)):
        #проверка на наличие ЕДИНСТВЕННОГО минуса впереди
        if arr_x[i][0] == '-':
            arr_x[i] = arr_x[i][1:]
        #проверка на наличие ЕДИНСТВЕННОЙ десятичной точки
        dot_pos = arr_x[i].find('.')
        if dot_pos >= 0:
            arr_x[i] = arr_x[i][:dot_pos] + arr_x[i][dot_pos + 1:]
        #проверка на цифры
        if not arr_x[i].isdigit():
            ok = False
            break
    return ok

#функция сортировки методом пузырьком с флагом
def sort(arr):
    n = len(arr)
    for i in range(n):
        ok = True
        for j in range(n - 1 - i):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                ok = False
        if ok:
            break
    return arr

#функция проверки работы сортировки
def sort_check():
    #очистка полей
    arr_result.set('')
    text_info.config(state = NORMAL)
    text_info.delete(1.0,END)
    
    s = arr_check.get() #строка, содеражащая массив
    if s == '':
        text_info.insert(END, "Массив для сортировки не введён!")
    elif array_check(s):
        #создание массива из строки
        arr_c = s.split()
        for i in range(len(arr_c)):
            arr_c[i] = float(arr_c[i])

        arr_c = sort(arr_c)

        #запись отсортированного массива в строку
        for i in range(len(arr_c)):
            s = arr_result.get() + str(arr_c[i])
            if i < len(arr_c) - 1:
                s += " "
            arr_result.set(s)
    else:
        text_info.insert(END, "Некорректный ввод проверочного массива.")
    text_info.config(state = DISABLED)
        

#функция запуска сортировки и расчёта её времени для каждого массива
def time_calculate():
    #очистка полей
    for i in range(3):
        for j in range(3):
            sort_time[i][j].set('')
    #проверка и обновление массива входных размерностей
    arr_kol = correct_data() #в случае корректного ввода: обработанный массив
    if arr_kol[0] != 0:
        arr = [] #рабочий массив
        for i in range(3):
            for j in range(3):
                arr.clear()
                """
                if i == 0:
                    #создание отсортированного массива
                    arr = [k for k in range(arr_kol[j])]
                elif i == 1:
                    #генерация случайного массива (значения от -20 до 20)
                    arr = [randint(0,arr_kol[j]) for k in range(arr_kol[j])]
                else:
                    #создание отсортированного наоборот массива
                    arr = [k for k in range(arr_kol[j]-1, -1, -1)]
                """

                #ПРОВЕРКА ИЗМЕРЕНИЯ ВРЕМЕНИ НА ОДНОМ И ТОМ ЖЕ МАССИВЕ
                arr = [k for k in range(arr_kol[j])]
                
                time_start = time.clock() #текущее время перед сортировкой
                sort(arr)
                time_action = time.clock() - time_start #время выполнения
                time_action = '{:11.9f}'.format(time_action)
                sort_time[i][j].set(time_action)

##
#инициализация окна
##
root = Tk()
root.title('Сортировка пузырьком с флагом')
root.resizable(False, False)
root.config(background = 'grey')
time.clock()

#инициализация переменных для записи времени
sort_time = []
for i in range(3):
    sort_time.append([StringVar(),StringVar(),StringVar()])
    
#инициализация размерностей массивов
arr_n = []
for i in range(3):
    arr_n.append(StringVar())
    arr_n[i].set(str((i+1)*50))

Label(root, text = "Анализ времени работы сортировки (в сек)", font = 16,
      bg = 'gray', fg = 'white').grid(row = 1, column = 1, padx = 8,
                                    pady = 8)
##
#создание таблицы
##
table = Frame(root)
table.grid(row = 2, column = 1, padx = 8, pady = 8)

#заголовок таблицы
table_head = []
table_head.append(Label(table, text = "количество элементов",
                        width = 24, relief = RIDGE))
table_head[0].grid(row = 1, column = 1)

#строка количества элементов
for i in range(3):
    label_temp = Entry(table, textvariable = arr_n[i], width = 18,
                       justify = CENTER, relief = SUNKEN)
    table_head.append(label_temp)
    table_head[i + 1].grid(row = 1, column = i + 2)

#столбец типов массивов
Label(table, text = "отсортированный массив",
      width = 24, relief = RIDGE).grid(row = 2, column = 1)
Label(table, text = "случайный массив",
      width = 24, relief = RIDGE).grid(row = 3, column = 1)
Label(table, text = "отсортированный наоборот",
      width = 24, relief = RIDGE).grid(row = 4, column = 1)

#ячейки таблицы со временем
table_time = []
for i in range(3):
    table_time.append([])
    for j in range(3):
        label_temp = Label(table, textvariable = sort_time[i][j],
                           justify = CENTER, width = 16,
                           background = 'white', relief = RIDGE)
        table_time[i].append(label_temp)
        table_time[i][j].grid(row = i + 2, column = j + 2)

#кнопка запуска расчёта времени сортировки и выполнения сортировки
btn_start = Button(root, text = "Запустить расчёт времени", width = 72,
                   command = time_calculate)
btn_start.grid(row = 3, column = 1, padx = 8, pady = 8)

Label(root, text = "Проверка работы сортировки", font = 16,
      bg = 'grey', fg = 'white').grid(row = 1, column = 2, padx = 8,
                                    pady = 8)
##
#панель проверки сортировки на малоразмерном массиве
##
check_frame = Frame(root)
check_frame.config(bg = 'grey')
check_frame.grid(row = 2, column = 2, padx = 4, pady = 4)

Label(check_frame, text = "Введите массив через пробел", width = 32,
      relief = SUNKEN).grid(row = 1, column = 1)

#окно ввода проверочного массива
arr_check = StringVar()
arr_input = Entry(check_frame, textvariable = arr_check, width = 38)
arr_input.grid(row = 2, column = 1)

Label(check_frame, text = "Результат сортировки", width = 32,
      relief = SUNKEN).grid(row = 3, column = 1)

#окно вывода отсортированного массива
arr_result = StringVar()
arr_output = Entry(check_frame, textvariable = arr_result, width = 38,
                   relief = SUNKEN, state = DISABLED,
                   disabledbackground = 'white',
                   disabledforeground = 'black')
arr_output.grid(row = 4, column = 1)

#кнопка запуска проверки сортировки
btn_check = Button(root, text = "Отсортировать", width = 32,
                   command = sort_check)
btn_check.grid(row = 3, column = 2, padx = 8, pady = 8)

#окно дополнительной информации
text_info = Text(root, width = 96, height = 6,
                 relief = RIDGE, state = DISABLED,
                 background = 'white', foreground = 'red')
text_info.grid(row = 4, column = 1, columnspan = 2, padx = 4, pady = 4)

root.mainloop()
