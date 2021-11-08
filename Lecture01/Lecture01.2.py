# Перевод Цельсия в Фаренгейты
try:
	c = float(input('Введите температуру в градусах Цельсия: '))
	if c < -273.15:
		import sys
		sys.exit ('Введите корректное значение')

	f = 1.8*c + 32

	print (f)

except ValueError:
	print ('Введите число')