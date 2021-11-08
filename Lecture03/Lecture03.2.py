
#Используя алгоритм Евклида

try:

	a = float(input('Введите первое число:'))
	b = float(input('Введите второе число:'))
	
	if a < 0 or b < 0:
		import sys
		sys.exit('Введите Натуральные числа n > 0')

	l = [a , b]
	l.sort ()

	i = 0
	while l[i+1] != 0:
		l.append (l[i] % l[i+1])
		i += 1
	else:
		print (l[i])

except ValueError:
    print('Введите число')