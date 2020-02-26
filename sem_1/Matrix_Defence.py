n = int(input('Введите размер квадратной матрицы: '))
if n < 1:
    print('Данный размер матрицы недопустим!')
else:
    a = []
    print('Введите матрицу построчно:')
    for i in range(n):
        a.append([int(j) for j in input().split()])

    positive = False
    negative = False
    pmax = 0
    nmax = 0
    ipos = 0
    ineg = 0

    for i in range(n):
        pk = 0
        nk = 0
        for x in a[i]:
            if x > 0:
                pk += 1
                positive = True
            elif x < 0:
                nk += 1
                negative = True
        if pk > pmax:
            pmax = pk
            ipos = i
        if nk > nmax:
            nmax = nk
            ineg = i

    if positive:
        sp = 0
        for x in a[ipos]:
            if x > 0:
                sp += x
        print('Сумма положительных чисел строки с наибольшим\n',
              'количеством положительных чисел: ',sp,sep = '')
    else:
        print('В матрице нет положительных элементов.')
        
    if negative:
        sn = 0
        for x in a[ineg]:
            if x < 0:
                sn += x
        print('Сумма отрицательных чисел строки с наибольшим\n',
              'количеством отрицательных чисел: ',sn,sep = '')
    else:
        print('В матрице нет отрицательных элементов.')
    
                
                
    
