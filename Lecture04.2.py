try:
	from random import randint
	l = []
	y = 0
	n = int(input('Сколько элементов нужно в спике:'))
	m = int(input('До какого числа генерировать:'))
	while y < n:
		l.append(randint(0,m))
		y += 1

	for i in range (n-1):
		for j in range (n-i-1):
			if l[j] > l[j+1]:
				l[j], l[j+1] = l[j+1], l[j]

	print (l)

except ValueError:
    print('Введите число')