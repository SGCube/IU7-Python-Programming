"""
Программа работы с базой данных
Автор: Сорокин Антон ИУ7-12Б

Переменные:
attr - имена аттрибутов
attr_keys - имена ключей словаря
fname - имя текущего файла
data - текущая база данных
data_len - длина списка (количество записей)
file - файл на открытие/закрытие
file_list - список доступных баз данных
data_cur - новая запись
n - режим работы
search_attr - фильтр поиска
search_key - название ключа-фильтра поиска
tch - список длин ячеек (рабочая переменная)
a,b,i,s,t,key,found,mode,mode2 - рабочие переменные
x1,x2 - границы поиска по численному фильтру
"""
import pickle
import os
attr = ['Название','Автор','Издательство','Год','Стоимость']
attr_keys = ['title','author','publ','year','cost']
fname = ''
data = []
data_len = 0

def data_read(fname):
    file = open(fname+'.pickle','rb')
    data_len = pickle.load(file)
    data = []
    for i in range(data_len):
        data.append(pickle.load(file))
    file.close()
    return data

def data_save(fname,data):
    file = open(fname+'.pickle','wb')
    pickle.dump(len(data),file)
    for a in data:
        pickle.dump(a,file)
    file.close()

def data_create():
    fname = input('\nВведите название новой базы данных: ')
    data = []
    data_save(fname,data)
    return fname

def data_open():
    fname = ''
    file_list = os.listdir(os.getcwd())
    i = 0
    while i < len(file_list):
        if file_list[i].find('.pickle') != len(file_list[i])-7:
            file_list.pop(i)
        else:
            file_list[i] = file_list[i][:(len(file_list[i])-7)]
            i += 1
    if file_list == []:
        print('\nНет ни одной базы данных!')
    else:
        print('\nДоступные базы данных:')
        for a in file_list:
            print(a)
        while True:
            fname = input('\nВведите название базы данных: ')
            found = False
            for s in file_list:
                if s == fname:
                    found = True
            if found:
                break
            print('Такой базы данных не существует!')
    return fname

def data_newnote(data):
    data_cur = {'title':'','author':'','publ':'','year':'','cost':''}
    s = input('Введите название книги: ')
    data_cur['title'] = s
    s = input('Введите имя автора книги: ')
    data_cur['author'] = s
    s = input('Введите издательство: ')
    data_cur['publ'] = s
    while True:
        s = input('Введите год издания: ')
        if s.isdigit():
            break
        else:
            print('Некорректный год!')
    data_cur['year'] = int(s)
    while True:
        s = input('Введите стоимость книги: ')
        a = s
        for i in range(len(a)):
            if a[i] == '.':
                a = a[:i]+a[i+1:]
                break
        if a.isdigit():
            break
        else:
            print('Некорректная стоимость!')
    data_cur['cost'] = float(s)
    data.append(data_cur)
    return data
    
def data_search_str(data,search_key,mode):      
    print('Выберите режим поиска')
    print('1 - полное совпадение')
    print('2 - наличие подстроки в значении')
    while True:
        mode2 = input()
        if mode2 == '1' or mode2 == '2':
            break
        print('Введите корректный вариант!')
    mode2 = int(mode2)
    s = input('Введите искомое значение: ')

    found = False
    i = 0
    while i < len(data):
        if (data[i][search_key] == s and mode2 == 1) or (
            data[i][search_key].find(s) == 0 and mode2 == 2):
            if mode == 0:
                if not found:
                    found = True
                    print('Результаты поиска:')
                    data_headerprint()
                data_iprint(data,i)
            else:
                found = True
                data.pop(i)
        elif mode == 1:
            i += 1
        if mode == 0:
            i += 1
    if found:
        if mode == 0:
            data_endprint()
    else:
        print('Таких данных нет!')
    if mode == 1:
        return data

def data_search_num(data,search_key,mode):
    print('Выберите режим поиска')
    print('1 - не меньше введённого значения')
    print('2 - не больше введённого значения')
    print('3 - интервал')
    while True:
        mode2 = input()
        if mode2 == '1' or mode2 == '2' or mode2 == '3':
            break
        print('Введите корректный вариант!')
    mode2 = int(mode2)
    while True:
        if mode2 == 1:
            x2 = '0'
            x1 = input('Введите наименьшее значение: ')
        elif mode2 == 2:
            x1 = '0'
            x2 = input('Введите наибольшее значение: ')
        else:
            x1,x2 = map(str,input(
                'Введите диапазон поиска через пробел: ').split())
        if search_key == 'year':
            if x1.isdigit() and x2.isdigit():
                x1 = int(x1)
                x2 = int(x2)
                break       
        else:
            a = x1
            b = x2
            for i in range(len(a)):
                if a[i] == '.':
                    a = a[:i]+a[i+1:]
                    break
            for i in range(len(b)):
                if b[i] == '.':
                    b = b[:i]+b[i+1:]
                    break
            if a.isdigit() and b.isdigit():
                x1 = float(x1)
                x2 = float(x2)
                break
        print('Некорректный ввод!')
    found = False
    i = 0
    while i < len(data):
        if (x1 <= data[i][search_key] and mode2 == 1) or (
            data[i][search_key] <= x2 and mode2 == 2) or (
            x1 <= data[i][search_key] <= x2 and mode2 == 3):
            if mode == 0:
                if not found:
                    found = True
                    print('Результаты поиска:')
                    data_headerprint()
                data_iprint(data,i)
            else:
                found = True
                data.pop(i)
        elif mode == 1:
            i += 1
        if mode == 0:
            i += 1
    if found:
        if mode == 0:
            data_endprint()
    else:
        print('Таких данных нет!')
    if mode == 1:
        return data

tch = [30,16,20,7,9]
def data_headerprint():
    print('\u250c'+tch[0]*'\u2500'+'\u252c'+tch[1]*'\u2500'+'\u252c'+(
        tch[2]*'\u2500'+'\u252c'+tch[3]*'\u2500'+(
            '\u252c'+tch[4]*'\u2500'+'\u2510')))
    print('\u2502           Название           '
          '\u2502     Автор      '
          '\u2502    Издательство    '
          '\u2502  Год  '
          '\u2502Стоимость\u2502')
    print('\u2502             книги            '
          '\u2502     книги      '
          '\u2502                    '
          '\u2502издания'
          '\u2502         \u2502')
    print('\u251c'+tch[0]*'\u2500'+'\u253c'+tch[1]*'\u2500'+'\u253c'+(
        tch[2]*'\u2500'+'\u253c'+tch[3]*'\u2500'+(
            '\u253c'+tch[4]*'\u2500'+'\u2524')))
    
def data_iprint(data,i):
    def data_format(data,i,key):
        if key == 'title':
            t = 0
        elif key == 'author':
            t = 1
        elif key == 'publ':
            t = 2
        elif key == 'year':
            t = 3
        else:
            t = 4
        s = data[i][key]
        if (key == 'title') or (key == 'author') or (key == 'publ'):
            s = s[:tch[t]]
            if len(data[i][key]) > tch[t]:
                s = s[:tch[t]-3]+'...'
        elif key == 'year':
            s = '{:4d}'.format(s)
        else:
            s = '{:9.2f}'.format(s)
        
        i = 0
        while len(s) < tch[t]:
            if i:
                s = ' ' + s
                i = 0
            else:
                s = s + ' '
                i = 1
        print(s,end = '\u2502')          

    print('\u2502',end = '')
    for k in attr_keys:
        data_format(data,i,k)
    print()

def data_endprint():
    print('\u2514'+tch[0]*'\u2500'+'\u2534'+tch[1]*'\u2500'+'\u2534'+(
        tch[2]*'\u2500'+'\u2534'+tch[3]*'\u2500'+'\u2534'+tch[4]*'\u2500'+'\u2518'))

while True:
    if fname != '':
        print(78*'=')
        print('База данных:',fname)
    print(37*'=','МЕНЮ',37*'=',sep='')
    print('1 - Создать новую базу данных')
    print('2 - Открыть базу данных')
    if fname != '':
        print('3 - Просмотреть все записи текущей базы данных')
        print('4 - Добавить новую запись в текущую базу данных')
        print('5 - Поиск элементов по фильтру')
        print('6 - Удаление по фильтру')
        print('7 - Сохранить базу данных')
    print('0 - Закончить выполнение программы')
    print(78*'=')
    print('Введите команду:', end=' ')
    while True:
        n = input()
        if (n == '1' or n == '2' or n == '0') or (
            (n == '3' or n == '4' or n == '5' or n == '6' or n == '7') and (
                fname != '')):
            break
        print('Введите корректную команду:', end=' ')

    if n == '0':
        break
    elif n == '1':
        fname = data_create()
        if fname != '':
            data = data_read(fname)
    elif n == '2':
        fname = data_open()
        if fname != '':
            data = data_read(fname)
    elif n == '3':
        data_headerprint()
        for i in range(len(data)):
            data_iprint(data,i)
        data_endprint()
    elif n == '4':
        data = data_newnote(data)
    elif n == '5':
        print('\nПоля базы данных:')
        for i in range(len(attr)):
            print(i+1,'-',attr[i])
        print()
        search_attr = 0
        while True:
            s = input('Введите номер поля, по которому вести поиск: ')
            if s.isdigit():
                search_attr = int(s) - 1
                if 0 <= search_attr < len(attr):
                    break
            print('Введите корректный номер!')
        if search_attr < 3:
            data_search_str(data,attr_keys[search_attr],0)
        else:
            data_search_num(data,attr_keys[search_attr],0)
    elif n == '6':
        print('\nПоля базы данных:')
        for i in range(len(attr)):
            print(i,'-',attr[i])
        print()
        search_attr = 0
        while True:
            s = input('Введите номер поля, по которому вести удаление: ')
            if s.isdigit():
                search_attr = int(s) - 1
                if 0 <= search_attr < len(attr):
                    break
            print('Введите корректный номер!')
        if search_attr < 3:
            data = data_search_str(data,attr_keys[search_attr],1)
        else:
            data = data_search_num(data,attr_keys[search_attr],1)
    elif n == '7':
        data_save(fname,data)
