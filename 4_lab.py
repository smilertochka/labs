
def p1():
    try:
        a = int(input('Введите число: '))
        b = a % 3
    except ValueError:
        print('Вводить можно только числа!')
    else:
        if b == 0 and a != 0:
            print('число', a , 'делится на 3')
        elif a == 0:
            print('введён 0')
        else:
            print('число', a ,'не делится на 3')

def p2():
    try:
        a = int(input('введите число'))
        b = 100 / a
    except ZeroDivisionError:
        print('Введён 0')
    except ValueError:
        print('Введено не число!')
    else:
        print(b)

def p3():
    try:
        a = input("Введите дату в формате дд.мм.гггг")
        a = a.split('.')
        b = int(a[0]) * int(a[1])
        c = (int(a[2]) % 100)
    except ValueError:
        print("Введено не число!")
    if b == c:
        print("Дата магическая!")
    else:
        print('Обычная дата')
def p4():
    b = 0
    c = 0
    a = input("Введите номер")
    if  len(a) % 2 == 0:
        print("Количество цифр должно быть чётным")
    for i in range(len(a) // 2):
        b += int(a[i])
    for i in range(len(a) - 1, (len(a) // 2) - 1, -1):
        c += int(a[i])
    if c == b:
        print("Счастливый билет!")
    else:
        print("Обычный билет!")
p4()


