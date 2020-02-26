s = input()
w = s.split()
lmax = len(max(w,key=len))
print(lmax)
for i in range(lmax):
    for j in range(len(w)):
        if i < len(w[j]):
            print(w[j][i],end = ' ')
        else:
            print(' ', end = ' ')
    print()
