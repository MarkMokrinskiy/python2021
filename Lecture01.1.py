# Расчёт третей стороны треугольника по теореме косинусов
try:
	a = float(input('Введите длину первой стороны стреугольника: '))
	b = float(input('Введите длину второй стороны стреугольника: '))
	f = float(input('Введите градусную меру угола меду сторонами: '))

	if (a or b or f) < 0 or f >= 180:
		import sys
		sys.exit ("Введите корректные парамеры")

	import math
	f = math.radians(f)

	c = math.sqrt(a**2 + b**2 - 2*a*b*math.cos(f))
	print (c)

except ValueError:
    print('Введите число')