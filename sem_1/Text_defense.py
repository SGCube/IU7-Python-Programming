t = []
f = open("text_defense.txt","r")
for s in f:
    t.append(s)

for i in range(len(t)-1):
    t[i] = t[i][:len(t[i])-1]

separ = " ,:;(){}[]<>/\\'-=+"+ "'"
endmark = '.?!'

sen = []
a = ''
for i in range(len(t)):
    for j in range(len(t[i])):
        if t[i][j] in endmark:
            a += t[i][j]
            sen.append(a)
            a = ''
        elif not (t[i][j] == ' ' and a ==''):
            a += t[i][j]
    if a != '':
        a += ' '
            
print('Исходный текст:')
for i in range(len(t)):
    print(t[i])
print()

k = []
for i in range(len(sen)):
    w = sen[i].split()
    k.append(len(w))

mark = -1
for i in range(len(k)):
    found = False
    for j in range(i+1,len(k)):
        if k[j] == k[i]:
            if not found:
                print('Предложения с количеством слов, равным {:d}:'.format(k[i]))
                print(sen[i])
                found = True
                k[i] = mark
            print(sen[j])
            k[j] = mark
    mark -= 1
    print()
