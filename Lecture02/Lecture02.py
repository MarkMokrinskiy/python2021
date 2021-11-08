try:
    a = float(input('Введите число от 0 до 99: '))
    if a == 0:
        print ('Нуль')
    elif a > 9 and a < 20:
        if a == 10:
            print('Десять')
        elif a == 11:
            print('Одиннадцать')
        elif a == 12:
            print('Двенадцать')
        elif a == 13:
            print('Тринадцать')
        elif a == 14:
            print('Четырнадцать')
        elif a == 15:
            print('Пятнадцать')
        elif a == 16:
            print('Шестнадцать')
        elif a == 17:
            print('Семнадцать')
        elif a == 18:
            print('Восемнадцать')
        else:
            print('Девятнадцать')
    else:
        import math
        b = a % 10
        c = math.floor(a/10)
        if b == 0:
            unit = ('')
        elif b == 1:
            unit = ('Один')
        elif b == 2:
            unit = ('Два')
        elif b == 3:
            unit = ('Три')
        elif b == 4:
            unit = ('Четыре')
        elif b == 5:
            unit = ('Пять')
        elif b == 6:
            unit = ('Шесть')
        elif b == 7:
            unit = ('Семь')
        elif b == 8:
            unit = ('Восемь')
        else:
            unit = ('Девять')
        if c == 0:
            dozen = ('')
        elif c == 2:
            dozen = ('Двадцать ')
        elif c == 3:
            dozen = ('Тридцать ')
        elif c == 4:
            dozen = ('Сорок ')
        elif c == 5:
            dozen = ('Пятьдесят ')
        elif c == 6:
            dozen = ('Шестьдесят ')
        elif c == 7:
            dozen = ('Семьдесят ')
        elif c == 8:
            dozen = ('Восемьдесят ')
        elif c == 9:
            dozen = ('Девяносто ')
        else:
            import sys
            sys.exit('Необходимо число от 0 до 99')
        print (dozen + unit)
          
except ValueError:
    print('Введите число')