import os
import pickle

data = []
data_list = []
fname = ''

while True:
    print('====')
    print('МЕНЮ')
    print('====')
    print('1 - создать базу данных')
    print('2 - открыть базу данных')
    if fname != '':
        print('3 - добавить запись')
        print('4 - удалить запись по имени')
        print('5 - вывести всех сотрудников')
        print('6 - вывести всех сотрудников с соответствующими должностями: ')
        print('7 - вывести всех сотрудников, имеющих зарплату ниже '
              'определённого числа')
    print('0 - завершить выполнение')
    n = input('Введите команду: ')
    if n == '0':
        break
    elif n == '1':
        data = []
        fname = input('Введите имя базы данных: ')
        f = open(fname+'.pickle','wb')
        pickle.dump(data,f)
        f.close()
    elif n == '2':
        data_list = os.listdir(os.getcwd())
        i = 0
        while i < len(data_list):
            if data_list[i][len(data_list)-9:] == '.pickle':
                data_list[i] = data_list[i][:len(data_list)-9]
                i += 1
            else:
                data_list.pop(i)
        if len(data_list) > 0:
            print('Доступные базы данных:')
            for a in data_list:
                print(a)
            fname = input('Введите имя базы данных: ')
            f = open(fname+'.pickle','rb')
            data = pickle.load(f)
            f.close()
        else:
            print('Доступных баз данных нет!')
    elif n == '3':
        data_cur = {'name':'','job':'','salary':0}
        data_cur['name'] = input('Введите имя сотрудника: ')
        data_cur['job'] = input('Введите должность сотрудника: ')
        while True:
            data_cur['salary'] = float(input('Введите зарплату сотрудника: '))
            if data_cur['salary'] >= 0:
                break
            print('Некорректные данные!')
        data.append(data_cur)
        f = open(fname+'.pickle','wb')
        pickle.dump(data,f)
        f.close()
    elif n == '4':
        s = input('Введите имя: ')
        i = 0
        while i < len(data):
            if data[i]['name'] == s:
                data.pop(i)
            else:
                i += 1
        f = open(fname+'.pickle','wb')
        pickle.dump(data,f)
        f.close()
    elif n == '5':
        print('Имя'+17*' '+' '+'Должность'+11*' '+' '+'  Зарплата')
        for i in range(len(data)):
            if len(data[i]['name']) > 20:
                print(data[i]['name'][:17] + '...',end = ' ')
            else:
                print(data[i]['name'] + (
                    (20-len(data[i]['name']))*' '), end = ' ')
            if len(data[i]['job']) > 20:
                print(data[i]['job'][:17] + '...',end = ' ')
            else:
                print(data[i]['job'] + (
                    (20-len(data[i]['job']))*' '), end = ' ')
            print('{:10.2f}'.format(data[i]['salary']))
    elif n == '6':
        jobs = input('Введите должности через запятую: ')
        jobs = jobs.split(',')
        for i in range(len(jobs)):
            jobs[i] = jobs[i].strip()
        data_temp = []
        for i in range(len(data)):
            if data[i]['job'] in jobs:
                data_temp.append(data[i])
        if len(data_temp) == 0:
            print('Таких сотрудников нет!')
        else:
            print('Имя'+17*' '+' '+'Должность'+11*' '+' '+'  Зарплата')
            for i in range(len(data_temp)):
                if len(data_temp[i]['name']) > 20:
                    print(data_temp[i]['name'][:17] + '...',end = ' ')
                else:
                    print(data_temp[i]['name'] + (
                        (20-len(data_temp[i]['name']))*' '), end = ' ')
                if len(data_temp[i]['job']) > 20:
                    print(data_temp[i]['job'][:17] + '...',end = ' ')
                else:
                    print(data_temp[i]['job'] + (
                        (20-len(data_temp[i]['job']))*' '), end = ' ')
                print('{:10.2f}'.format(data_temp[i]['salary']))
    elif n == '7':
        max_salary = float(input('Введите величину зарплаты: '))
        data_temp = []
        for i in range(len(data)):
            if data[i]['salary'] < max_salary:
                data_temp.append(data[i])
        if len(data_temp) == 0:
            print('Таких сотрудников нет!')
        else:
            print('Имя'+17*' '+' '+'Должность'+11*' '+' '+'  Зарплата')
            for i in range(len(data_temp)):
                if len(data_temp[i]['name']) > 20:
                    print(data_temp[i]['name'][:17] + '...',end = ' ')
                else:
                    print(data_temp[i]['name'] + (
                        (20-len(data_temp[i]['name']))*' '), end = ' ')
                if len(data_temp[i]['job']) > 20:
                    print(data_temp[i]['job'][:17] + '...',end = ' ')
                else:
                    print(data_temp[i]['job'] + (
                        (20-len(data_temp[i]['job']))*' '), end = ' ')
                print('{:10.2f}'.format(data_temp[i]['salary']))
                
