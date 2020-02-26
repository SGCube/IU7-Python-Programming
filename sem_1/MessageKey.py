"""
Шифрование сообщения с использованием ключа
Автор: Сорокин Антон ИУ7-12Б

Переменные:
a - алфавит
s - сообщение
key - ключ
sh - шифр сообщения
d - массив кодов символов ключа относительно алфавита
correct_data - соответствует ли ключ алфавиту
ii - текущий элемент ключа
i,x - рабочие переменные
low - нужно ли после преобразования перевести в нижний регистр
с - текущий символ
c_ord - код символа строки относительно алфавита

"""
a = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

s = input('Введите сообщение: ')
key = input('Введите ключ: ')
key = key.upper()
sh = ""
ii = -1
d = []

#Проверка ключа на корректность и создание массива сдвигов
correct_data = True
for x in key:
    key_ord = 0
    j = a.find(x)
    if j > -1:
        d.append(j)
    else:
        correct_data = False
        
if correct_data:
    for i in range(len(s)):
        low = False
        c = s[i]
        c = c.upper()
        c_ord = a.find(c)
        if s[i] != c:
            low = True
        
        ii += 1
        if ii >= len(d):
            ii -= len(d)

        #Сдвиг
        if c_ord > -1:
            if c_ord + d[ii] < len(a):
                c = a[c_ord + d[ii]]
            else:
                c = a[c_ord + d[ii] - len(a)]
        
        if low:
            sh += c.lower()
        else:
            sh += c

    print('Шифр:',sh)
else:
    print('Шифр не соответствует алфавиту.')
