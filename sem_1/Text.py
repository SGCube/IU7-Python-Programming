"""
Текстовый мини-редактор
Автор: Сорокин Антон ИУ7-12Б

Переменные функций описаны перед описанием функций.
Переменные основной программы:
text - исходный текст
textN - изменённый текстэ
word1 - слово, которое заменяется
word2 - слово, на которое заменяется word1
sen - список предложений
smax - самое длинное предложение
word_rotate - слово с чередованием гласных и согласных
n - номер команды
vowel - набор гласных
cons - набора согласных
separ - набора разделителей/знаков препинания
endmark - набор знаков завершения
"""
vowel = 'аеёиоуыэюяaeiouy'
vowel += vowel.upper()
cons = 'бвгджзклмнпрстфхцчшщbcdfghjklmnpqrstvwxz'
cons += cons.upper()
alpha = vowel + cons + 'ЪЬъь' + '0123456789'
separ = ',-:;"^*+=/\\(){}[]<>`~' + "' "
endmark = '.!?'

#Вывод текста
#====================================================================#
def text_print(t):
    for s in t:
        print(s)
#====================================================================#

#Поиск индекса самой длинной строки в списке/в тексте
#===================================================================#
"""
Аргументы:
 t - текст
Переменные:
 lmax - индекс самой длинной строки
 i - итератор
"""
def list_strlenmax(t):
    lmax = 0
    for i in range(len(t)):
        if len(t[i]) > len(t[lmax]):
            lmax = i
    return lmax
#====================================================================#

#Удаление лишних пробелов между словами (для выравнивания по краям)
#====================================================================#
def text_extra_space_del(s):
    isspace = False
    i = 0
    while i < len(s):
        if s[i] == ' ':
            if isspace:
                s = s[:i]+s[i+1:]
            else:
                isspace = True
                i += 1
        else:
            isspace = False
            i += 1
    return s
#====================================================================#

#Выравнивание текста по левому краю
#====================================================================#
def text_align_left(t):
    for i in range(len(t)):
        t[i] = t[i].lstrip(' ')
        t[i] = text_extra_space_del(t[i])
    return t
#====================================================================#

#Выравнивание текста по правому краю
#====================================================================#
def text_align_right(t):    
    lmax = list_strlenmax(t)
    for i in range(len(t)):
        t[i] = t[i].rstrip(' ')
        t[i] = text_extra_space_del(t[i])
        while len(t[i]) < len(t[lmax]):
            t[i] = ' ' + t[i]  
    return t
#====================================================================#

#Выравнивание текста по ширине
#===================================================================#
"""
Аргументы:
 t - текст
Переменные:
 lmax - индекс самой длинной строки
 i - итератор
 sp_dif - разница длин текущей строки и самой длинной
 sp_add - во сколько раз увеличить количество пробелов между словами
 sp_extra - сколько останется добавить пробелов
"""
def text_align_width(t):
    t = text_align_right(t)
    t = text_align_left(t)
    lmax = list_strlenmax(t)
    for i in range(len(t)):
        sp_dif = len(t[lmax]) - len(t[i])
        if sp_dif > 0:
            kspace = t[i].count(' ')
            sp_add = sp_dif // kspace + 1
            sp_extra = sp_dif % kspace
            t[i] = t[i].replace(' ',sp_add*' ')
            t[i] = t[i].replace(sp_add*' ',(sp_add+1)*' ',sp_extra)
    return t
#====================================================================#

#Создание списка предложений текста
#====================================================================#
"""
Аргументы:
 t - текст
Переменные:
 s - текст в виде одной строки
 x - список предложений
 sent - текущее предложение
 a - текущий символ текста
"""
def sentence_list(t):
    s = ' '.join(t)
    x = []
    sent = ''
    for a in s:
        if not (sent == '' and a == ' '):
            sent += a
            if a in endmark:
                x.append(sent)
                sent = ''
    return x
#====================================================================#

#Создание списка слов в предложении/в строке
#====================================================================#
"""
Аргументы:
 s - строка
Переменные:
 w - список слов
 i,j - итераторы
 extra_word - новое слово, если внутри исходного находится знак
              препинания, не выделенный пробелами
"""
def word_list(s):
    w = s.split()
    i = 0
    while i < len(w):
        w[i] = w[i].strip(separ+endmark)
        j = 0
        while j < len(w[i]):
            if w[i][j] in (separ):
                extra_word = w[i][j+1:]
                w[i] = w[i][:j]
                w.insert(i+1,extra_word)
            j += 1
        i += 1
    return w
#====================================================================#

#Замена в тексте одного слова на другое
#====================================================================#
"""
Аргументы:
 t - текст
 w1 - слово, которое заменяется
 w2 - слово, на которое заменяется w1
Переменные:
 i, j - итераторы
 word - текущее слово
"""
def word_replace(t,w1,w2):
    t_temp = t[:]
    w1 = w1.strip()
    w2 = w2.strip()
    separ_have = False
    endmark_have = False
    alpha_have = False
    found = True
    for i in range(len(w1)):
        if w1[i] in separ:
            separ_have = True
        if w1[i] in endmark:
            endmark_have = True
        if w1[i] in alpha:
            alpha_have = True
    for i in range(len(t)):
        t[i] = t[i].split(' ')
        for j in range(len(t[i])):
            if separ_have and endmark_have:
                word = t[i][j].strip()
                if not alpha_have:
                    t[i][j] = t[i][j].replace(w1,w2)
            elif separ_have:
                word = t[i][j].strip(endmark)
                if not alpha_have:
                    t[i][j] = t[i][j].replace(w1,w2)
            elif endmark_have:
                word = t[i][j].strip(separ)
                if not alpha_have:
                    t[i][j] = t[i][j].replace(w1,w2)
            else:
                word = t[i][j].strip(separ+endmark)
            if word == w1:
                t[i][j] = t[i][j].replace(w1,w2)
        t[i] = ' '.join(t[i])
    if t_temp == t:
        found = False
        print('Слово "',w1,'" не найдено в тексте!',sep='')
    return t
#====================================================================#

#Поиск слова с чередованием гласных и согласных в строке
#====================================================================#
"""
Аргументы:
 s - строка
Переменные:
 w - список слов
 rotate - происходит ли чередование
 i, j - итераторы
 letter_type - тип текущей буквы (гласная, согласная, иные)
 letter_prev - тип предыдущей буквы
"""
def soundrotate_word(s):
    w = word_list(s)
    rotate = False
    i = 0
    while not rotate and i < len(w):
        rotate = True
        letter_type = 2
        if w[i][0] in vowel:
            letter_type = 0
        elif w[i][0] in cons:
            letter_type = 1
        letter_prev = letter_type
        j = 1
        if len(w[i]) > 1:
            while rotate and j < len(w[i]):
                if w[i][j] in vowel:
                    letter_type = 0
                elif w[i][j] in cons:
                    letter_type = 1
                rotate = (letter_type == 1 and letter_prev == 0) or(
                    letter_type == 0 and letter_prev == 1)
                letter_prev = letter_type
                j += 1
        else:
            rotate = False
        i += 1
    if rotate:
        return w[i-1]
    else:
        return -1
#====================================================================#
        
#Основная программа
#=====================================================================
text = []
f = open("text.txt","r")
text = f.readlines()
for i in range(len(text)-1):
    text[i] = text[i][:len(text[i])-1]
f.close()

n = '0'
while True:
    print(78*'=')
    print('Текст:')
    text_print(text)
    print(78*'=')
    print(29*' '+'Меню мини-редактора:')
    print(78*'=')
    print('1 - Удаление слова из текста')
    print('2 - Замена одного слова из текста на другое')
    print('3 - Выравнивание по левому краю')
    print('4 - Выравнивание по правому краю')
    print('5 - Выравнивание по ширине')
    print('6 - Найти самое длинное предложение в тексте')
    print('    и найти в нём слово с чередованием гласных и согласных')
    print('0 - Завершить выполнение программы')
    print(78*'=')
    print('Введите номер команды, которую хотите выполнить:',end = ' ')
    while True:
        n = input()
        if n == '0' or n == '1' or n == '2' or n == '3' or (
            n == '4' or n == '5' or n == '6'):
            break
        else:
            print('Введите корректный номер:',end = ' ')
    print()
    
    if n == '0':
        break
    elif n == '1':
        word1 = input('Введите слово, которое хотите удалить: ')
        text = word_replace(text,word1,'')
    elif n == '2':
        word1 = input('Введите слово, которое хотите заменить: ')
        word2 = input('Введите слово, на которое хотите заменить: ')
        text = word_replace(text,word1,word2)
    elif n == '3':
        text = text_align_left(text[:])
    elif n == '4':
        text = text_align_right(text[:])
    elif n == '5':
        text = text_align_width(text[:])
    elif n == '6':
        sen = sentence_list(text)
        s_temp = sen[:]
        for i in range(len(s_temp)):
            s_temp[i] = text_extra_space_del(s_temp[i])
        smax = s_temp[list_strlenmax(s_temp)]
        print('Самое длинное преложение текста:')
        print(smax,end='\n\n')
        word_rotate = soundrotate_word(smax)
        if word_rotate == -1:
            print('Слов с чередованием гласных и согласных нет в предложении')
        else:
            print('Слово с чередованием гласных и согласных:')
            print(word_rotate)




