from math import sqrt

xa,ya = map(float,input('Введите координаты точки A треугольника: ').split(' '))
xb,yb = map(float,input('Введите координаты точки B треугольника: ').split(' '))
xc,yc = map(float,input('Введите координаты точки C треугольника: ').split(' '))
x,y = map(float,input('Введите координаты внутренней точки: ').split(' '))

ma = sqrt((x-xa)**2 + (y-ya)**2)
mb = sqrt((xb-x)**2 + (yb-y)**2)
mc = sqrt((x-xc)**2 + (y-yc)**2)

ab = sqrt((xb-xa)**2 + (yb-ya)**2)
ac = sqrt((xc-xa)**2 + (yc-ya)**2)
bc = sqrt((xb-xc)**2 + (yb-yc)**2)

p = (ma+mc+ac)/2
h1 = 2*sqrt(p*(p-ma)*(p-mc)*(p-ac))/ac

p = (mb+mc+bc)/2
h2 = 2*sqrt(p*(p-mc)*(p-mb)*(p-bc))/bc

p = (ab+ma+mb)/2
h3 = 2*sqrt(p*(p-ma)*(p-mb)*(p-ab))/ab

if h1 < h2:
    if h1 < h3:
        print('\nБлижайшая сторона: AC')
        print('Расстояние до стороны: {:7.4f}'.format(h1))
    elif h1 == h3:
        print('\nБлижайшие стороны: AC и AB (точка равноудалена)')
        print('Расстояние до сторон: {:7.4f}'.format(h1))
    else:
        print('\nБлижайшая сторона: AB')
        print('Расстояние до стороны: {:7.4f}'.format(h3))
elif h1 > h2:
    if h2 < h3:
        print('\nБлижайшая сторона: BC')
        print('Расстояние до стороны: {:7.4f}'.format(h2))
    elif h2 == h3:
        print('\nБлижайшие стороны: BC и AB (точка равноудалена)')
        print('Расстояние до сторон: {:7.4f}'.format(h2))
    else:
        print('\nБлижайшая сторона: AB')
        print('Расстояние до стороны: {:7.4f}'.format(h3))
else:
    if h1 < h3:
        print('\nБлижайшие стороны: AC и BC (точка равноудалена)')
        print('Расстояние до сторон: {:7.4f}'.format(h1))
    elif h1 == h3:
        print('\nТочка равноудалена от всех сторон')
        print('Расстояние до сторон: {:7.4f}'.format(h1))
    else:
        print('\nБлижайшая сторона: AB')
        print('Расстояние до стороны: {:7.4f}'.format(h3))
