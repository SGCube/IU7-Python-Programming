from random import randint
for j in range(20):
    s = ''
    for i in range(20):
        mode = randint(1,2)
        if mode == 1:
            s += str(randint(0,9))
        else:
            a1 = randint(65,90)
            a2 = randint(97,122)
            mode2 = randint(1,2)
            if mode2 == 1:
                s += chr(a1)
            else:
                s += chr(a2)
    print(s)
