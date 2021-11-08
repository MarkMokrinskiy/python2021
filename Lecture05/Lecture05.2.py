s = input('Введите строку вида NdM, где:\nN - кол-во кубиков\nM - кол-во сторон одного кубика\n').split('d')

if len(s) != 2: #Проверка входящих данных
	import sys
	sys.exit('Введите корректные данные')
if s[0].isnumeric() == False or s[1].isnumeric() == False:
	import sys
	sys.exit('Введите корректные данные')

n = int(s[0])
m = int(s[1])
l = [i+1 for i in range(m)] 
lol = [i+1 for i in range(n-1,n*m)]

from itertools import *
try:
	ss = [0]*(m**n)
except MemoryError:
	import sys
	sys.exit('Не хватает оперативной памяти')

prod = product (l, repeat = n)
o = 0
for i in prod:
   for j in range(n): 
   	ss[o] = ss[o]+int(i[j])
   
   o += 1

print ('Результат:') #Вывод данных на экран
i = 0      
while i < m*n-(n-1):
	print (str(lol[i]) + ' = ' + str(round(ss.count(lol[i])*100/(m**n),2)) + '%')
	i += 1