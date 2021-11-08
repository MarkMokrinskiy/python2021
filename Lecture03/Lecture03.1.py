try:
	n = float(input('Введите Натуральное число до кoторого найти хотите простые числа:'))
	if n < 1:
		import sys
		sys.exit('Введите Натуральное число n > 0')

	k = 2
	l = []
	while k < n+1:      #Нахождение всех чисел до N
		l.append (k)
		k += 1

	i = 0
	while i < len(l) - 1:
		d = l[i]
		i += 1
		for t in l:
			if (t % d == 0) and t != d:
				l.remove(t)
	print (l)
	

except ValueError:
    print('Введите число')