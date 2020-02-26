"""
Программа, переводящая десятичные числа в троичную симметричную систему
счисления и наоборот

Основные переменные:
en_var - входное число
res_var - результат перевода
numsys - система счисления исходного числа
         (True - троичная симметричная, False - десятичная)

Автор: Сорокин А. П. ИУ7-22Б
"""
from tkinter import *

#проверка ввода на десятичное число
def correct_data10(s):
    if s == "":
        return False
    s_temp = s
    if s_temp[0] == '-':
        s_temp = s[1:]
        
    j = s_temp.find('.')
    if j != -1:
        s_temp = s_temp[:j] + s_temp[j+1:]
    return s_temp.isdigit()

#проверка ввода на число троичной симметричной системы
def correct_data3s(s):
    if s == "":
        return False
    ok = True
    dot_found = False #найдена ли точка
    for i in range(len(s)):
        if not (s[i] == '-' or s[i] == '0' or s[i] == '+'):
            if s[i] == '.' and (not dot_found):
                dot_found = True
            else:
                ok = False
                break
    return ok

#функция ввода символа с кнопки (цифры или десятичной точки)
def key_input(k):
    s = en_var.get()
    if k != '.' or k == '.' and s.find('.') == -1:
        s += k
    en_var.set(s)

#функция перстановки кнопок при смене системы счисления
def button_change():
    if numsys.get():
        #переход к кнопкам для троичной симметричной системы
        btn7.grid_remove()
        btn8.grid_remove()
        btn9.grid_remove()
        btn4.grid_remove()
        btn5.grid_remove()
        btn6.grid_remove()
        btn1.grid_remove()
        btn2.grid_remove()
        btn3.grid_remove()
        btn0.grid_remove()
        btn_sign.grid_remove()
        btn_decimal.grid_remove()
        btn_minus.grid(row = 5, column = 1, padx = 8, pady = 8)
        btn0.grid(row = 5, column = 2, padx = 8, pady = 8)
        btn_plus.grid(row = 5, column = 3, padx = 8, pady = 8)
        btn_sign.grid(row = 6, column = 1, padx = 8, pady = 8)
        btn_decimal.grid(row = 6, column = 3, padx = 8, pady = 8)
    else:
        #переход к кнопкам для десятичной системы
        btn_plus.grid_remove()
        btn_minus.grid_remove()
        btn7.grid(row = 5, column = 1, padx = 8, pady = 8)
        btn8.grid(row = 5, column = 2, padx = 8, pady = 8)
        btn9.grid(row = 5, column = 3, padx = 8, pady = 8)
        btn4.grid(row = 6, column = 1, padx = 8, pady = 8)
        btn5.grid(row = 6, column = 2, padx = 8, pady = 8)
        btn6.grid(row = 6, column = 3, padx = 8, pady = 8)
        btn1.grid(row = 7, column = 1, padx = 8, pady = 8)
        btn2.grid(row = 7, column = 2, padx = 8, pady = 8)
        btn3.grid(row = 7, column = 3, padx = 8, pady = 8)
        btn0.grid(row = 8, column = 2, padx = 8, pady = 8)
        btn_sign.grid(row = 8, column = 1, padx = 8, pady = 8)
        btn_decimal.grid(row = 8, column = 3, padx = 8, pady = 8)

#функция смены знака числа
def negate(s, nums):
    ok = False
    if nums:
        #для числа в троичной симметричной системе счисления
        ok = correct_data3s(s)
        if ok:
            s_temp = s
            s = ""
            for i in range(len(s_temp)):
                if s_temp[i] == '-':
                    s += '+'
                elif s_temp[i] == '+':
                    s += '-'
                else:
                    s += s_temp[i]
    else:
        #для числа в десятичной системе счисления
        ok = correct_data10(s)
        if ok:
            if s[0] == '-':
                s = s[1:]
            else:
                s = '-' + s

    if ok:
        return s
    else:
        return "ERROR!"

#функция вызова смены знака вводимого числа
def negate_button():
    x = en_var.get()
    s = negate(x, numsys.get())
    
    if s == "ERROR!":
        res.config(state = NORMAL)
        if x == "":
            res_var.set("Число не введено!")
        else:
            res_var.set("Некорректный ввод!")
        res.config(state = "readonly")
    else:
        en_var.set(s)

#функция перевода числа из одной системы в другую
def calculate():
    x = en_var.get()
    
    ok = True
    if numsys.get():
        #перевод из троичной симметричной в десятичную
        y = 0
        ok = correct_data3s(x)
        if ok:
            j = x.find('.')
            if j == -1:
                j = len(x)
            #перевод целой части числа
            k = 1
            for i in range(j - 1, -1, -1):
                if x[i] == '-':
                    y += -k
                elif x[i] == '+':
                    y += k
                k *= 3
            k = 1/3
            #перевод дробной части числа
            if 0 <= j < len(x):
                for i in range(j + 1, len(x)):
                    if x[i] == '-':
                        y += -k
                    elif x[i] == '+':
                        y += k
                    k /= 3
                
    else:
        #перевод из десятичной в троичную симметричную
        y = ""
        is_negative = False
        ok = correct_data10(x)
        if ok:
            #разбиение числа на целую и дробную части
            if x[0] == '-':
                is_negative = True
                
            dot_i = x.find('.')
            x_fract = "0.0"
            if dot_i >= 0:
                x_fract = '0' + x[dot_i:]
                x = x[:dot_i]
            x_fract = float(x_fract)
            x = abs(int(x))
                
            #перевод целой части числа
            while x > 2:
                r = x % 3
                if r == 2:
                    y = '-' + y
                elif r == 1:
                    y = '+' + y
                else:
                    y = '0' + y
                x //= 3
                if r == 2:
                    x += 1
            if x == 2:
                y = '+-' + y
            elif x == 1:
                y = '+' + y
            else:
                y += '0'
                

            #перевод дробной части числа
            if dot_i >= 0:
                y += '.'
                cur_pos = len(y)
                if x_fract == 0:
                    y += '0'
                else:
                    for i in range(7):
                        x_fract *= 3
                        temp_int = int(x_fract)
                        if temp_int == 0:
                            y += '0'
                        elif temp_int == 1:
                            y += '+'
                        else:
                            y += '-'
                            #алгоритм прибавления '+' к предыдущему разряду
                            plus = 1
                            i = cur_pos - 1
                            while i >= 0 and plus == 1:
                                if y[i] == '-':
                                    y = y[:i] + '0' + y[i+1:]
                                    plus = 0
                                elif y[i] == '0':
                                    y = y[:i] + '+' + y[i+1:]
                                    plus = 0
                                elif y[i] == '+':
                                     y = y[:i] + '-' + y[i+1:]
                                i -= 1
                            if plus == 1:
                                y = '+' + y
                        x_fract -= temp_int
                        cur_pos += 1
                   
            if is_negative:
                y = negate(y, True)

    res.config(state = NORMAL)
    if ok:
        #вывод результата
        res_var.set(y)
    else:
        if x == "":
            res_var.set("Число не введено!")
        else:
            res_var.set("Некорректный ввод!")
    res.config(state = "readonly")

#удаление символа с конца
def backspace_input():
    s = en_var.get()
    s = s[:-1]
    en_var.set(s)

#очистка ввода
def clear_input():
    en_var.set("")

#очистка вывода
def clear_output():
    res.config(state = NORMAL)
    res_var.set("")
    res.config(state = "readonly")

#очистка всех полей
def clear_all():
    clear_input()
    clear_output()

#функция вывода информации о программе
def info():
    info_window = Toplevel(root)
    info_window.title("О программе")
    info_window.resizable(False, False)
    task_header = Label(info_window, text = "Задача программы", font = 16)
    task_info = Label(info_window, text = "Данная программа позволяет "
                      "переводить\nчисла десятичной системе счисления в "
                      "числа троичной\nсимметричной системы счисления"
                      " и наоброт.")
    instruct_header = Label(info_window, text = "Инструкция", font = 16)
    instruct_info = Label(info_window, text = "В верхнее окошко вводится "
                        "число, которое следует перевести.\nДробные "
                        "числа вводятся с использованием точки "
                        "(не запятой!).\n Выберите систему счисления "
                        "исходного числа и нажмите кнопку 'Перевести'.\n"
                        "Также для ввода можно использовать кнопки на экране.")
    task_header.grid(row = 1, column = 1, padx = 8, pady = 8)
    task_info.grid(row = 2, column = 1, padx = 8, pady = 8)
    instruct_header.grid(row = 3, column = 1, padx = 8, pady = 8)
    instruct_info.grid(row = 4, column = 1, padx = 8, pady = 8)

#функция вывода информации об авторе
def author():
    info_window = Toplevel(root)
    info_window.title("Об авторе")
    info_window.resizable(False, False)
    author_info = Label(info_window, text = "Автор программы: Сорокин А. П.\n"
                        "Студент кафедры ИУ7 МГТУ им. Баумана "
                        "\n(группа ИУ7-22Б)", font = 16)
    author_info.grid(row = 1, column = 1, padx = 8, pady = 8)

#инициализация окна
root = Tk()
root.title("Калькулятор")
root.resizable(False, False)

#инициализация переменных
en_var = StringVar()
res_var = StringVar()
numsys = BooleanVar()
numsys.set(False)

#создание меню окна
menubar = Menu(root)
menu1 = Menu(menubar)
menu2 = Menu(menubar)
menu3 = Menu(menubar)

menu1.add_command(label = "Система счилсения исходного числа")
menu1.add_radiobutton(label = "десятичная", variable = numsys, value = False)
menu1.add_radiobutton(label = "троичная симметричная", variable = numsys,
                      value = True)
menu1.add_separator()
menu1.add_command(label = "Перевести число в другую систему",
                  command = calculate)
menubar.add_cascade(label = "Вычисления", menu = menu1)

menu2.add_command(label = "Очистить поле ввода", command = clear_input)
menu2.add_command(label = "Очистить поле результата", command = clear_output)
menu2.add_command(label = "Очистить все поля", command = clear_all)
menubar.add_cascade(label = "Очистка", menu = menu2)

menu3.add_command(label = "О программе", command = info)
menu3.add_command(label = "Об авторе", command = author)
menubar.add_cascade(label = "Справка", menu = menu3)

root.config(menu = menubar)

#окно ввода
en = Entry(root, textvariable = en_var, width = 24, font = 'Arial 24',
           justify = RIGHT)
en.grid(row = 1, column = 1, columnspan = 3, padx = 8, pady = 8)
#окно вывода
res = Entry(root, textvariable = res_var, width = 24, font = 'Arial 24',
           justify = RIGHT, state = "readonly")
res.grid(row = 4, column = 1, columnspan = 3, padx = 8, pady = 8)

#кнопки выбора системы счисления
numsys_label = Label(root, text = "Система счисления исходного числа")
numsys_label.grid(row = 2, column = 2, columnspan = 2, padx = 8, pady = 8)
radio_btn10 = Radiobutton(root, text = "десятичная",
                          variable = numsys, value = False,
                          command = button_change)
radio_btn3 = Radiobutton(root, text = "троичная симметричная",
                         variable = numsys, value = True,
                         command = button_change)
radio_btn10.grid(row = 3, column = 2, padx = 8, pady = 8)
radio_btn3.grid(row = 3, column = 3, padx = 8, pady = 8)

#кнопка перевода числа
btn_calc = Button(root, text = "Перевести", width = 20,
                  command = calculate)
btn_calc.grid(row = 2, column = 1, rowspan = 2, padx = 8, pady = 8)

#кнопки ввода
btn_num = []
for i in range(10):
    btn_num.append(Button(root, text = str(i), width = 8, font = 24,
                          command = lambda: key_input(str(i))))
    if i > 0:
        btn_num[i].grid(row = 7 - (i - 1)// 3, column = (i - 1) % 3 + 1,
                        padx = 8, pady = 8)
btn1 = Button(root, text = "1", width = 8, font = 24,
              command = lambda: key_input('1'))
btn2 = Button(root, text = "2", width = 8, font = 24,
              command = lambda: key_input('2'))
btn3 = Button(root, text = "3", width = 8, font = 24,
              command = lambda: key_input('3'))
btn4 = Button(root, text = "4", width = 8, font = 24,
              command = lambda: key_input('4'))
btn5 = Button(root, text = "5", width = 8, font = 24,
              command = lambda: key_input('5'))
btn6 = Button(root, text = "6", width = 8, font = 24,
              command = lambda: key_input('6'))
btn7 = Button(root, text = "7", width = 8, font = 24,
              command = lambda: key_input('7'))
btn8 = Button(root, text = "8", width = 8, font = 24,
              command = lambda: key_input('8'))
btn9 = Button(root, text = "9", width = 8, font = 24,
              command = lambda: key_input('9'))
btn0 = Button(root, text = "0", width = 8, font = 24,
              command = lambda: key_input('0'))
btn_decimal = Button(root, text = ".", width = 8, font = 24,
              command = lambda: key_input('.'))
btn_plus = Button(root, text = "+", width = 8, font = 24,
              command = lambda: key_input('+'))
btn_minus = Button(root, text = "-", width = 8, font = 24,
              command = lambda: key_input('-'))
#кнопка смены знака
btn_sign = Button(root, text = "+/-", width = 8, font = 24,
                  command = negate_button)

btn7.grid(row = 5, column = 1, padx = 8, pady = 8)
btn8.grid(row = 5, column = 2, padx = 8, pady = 8)
btn9.grid(row = 5, column = 3, padx = 8, pady = 8)
btn4.grid(row = 6, column = 1, padx = 8, pady = 8)
btn5.grid(row = 6, column = 2, padx = 8, pady = 8)
btn6.grid(row = 6, column = 3, padx = 8, pady = 8)
btn1.grid(row = 7, column = 1, padx = 8, pady = 8)
btn2.grid(row = 7, column = 2, padx = 8, pady = 8)
btn3.grid(row = 7, column = 3, padx = 8, pady = 8)
btn0.grid(row = 8, column = 2, padx = 8, pady = 8)
btn_sign.grid(row = 8, column = 1, padx = 8, pady = 8)
btn_decimal.grid(row = 8, column = 3, padx = 8, pady = 8)

root.mainloop()
