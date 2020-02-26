"""
Проверка строки на формат даты

Автор: Сорокин Антон ИУ7-12Б

Переменные:
s - входная строка
"""
import re
s = input('Введите строку: ')
res = re.search("[0-3]{1}[0-9]{1}[-./][0-1]{1}[0-9]{1}[-./][0-9]{4}",s)
ressep = False
resd = False
resm = False
if res:
    d = s[:2]
    sep1 = s[2]
    sep2 = s[5]
    m = s[3:5]
    y = s[6:]
    print(d,sep1,m,sep2,y)
    ressep = re.search("[-./]",s)
    ressep = ressep and (sep1 == sep2)
    resd = re.search("[0]{1}[1-9]{1}",d
            ) or re.search("[1-2]{1}[0-9]{1}",d
            ) or re.search("[3]{1}[0-1]{1}",d)
    resm = re.search("[0]{1}[1-9]{1}",m) or re.search("[1]{1}[1-2]{1}",m)
if ressep and resd and resm:
    print('Данная строка написана в формате даты.')
else:
    print('Данная строка не является датой.')
