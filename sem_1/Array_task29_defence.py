x = list(map(int,input('Введите исходный массив: ').split()))

correct_data = True
if len(x) % 2 != 0:
    correct_data = False
else:
    for i in range(1,len(x),2):
        if x[i] < 0:
            correct_data = False

if correct_data:
    i = 0
    while i < len(x):
        a = x[i]
        k = x[i+1]
        x.pop(i+1)
        x.pop(i)
        for j in range(k):
            x.insert(i,a)
            i += 1

    print('Новый массив:',x)
else:
    print('Некорректные данные')
