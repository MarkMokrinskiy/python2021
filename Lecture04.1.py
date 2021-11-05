try:
	from random import randint
	l = []
	y = 0
	n = int(input('Сколько элементов нужно в спике:'))
	m = int(input('До какого числа генерировать:'))
	while y < n:
		l.append(randint(0,m))
		y += 1
	print(l)


except ValueError:
    print('Введите число')