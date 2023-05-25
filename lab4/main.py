def p1():
    try:
        a = int(input("Введите число для проверки деления на 3: "))
        b = a % 3
    except ValueError:
        print("Введено не число")
    else:
        if a != 0 and b == 0:
            print("Число ", a, " делится на 3")
        elif a == 0:
            print("Введен ноль")
        else:
            print("Число ", a, " не делится на 3")

def p2():
    try:
        a = int(input("Введите число, на которое нужно поделить 100: "))
        b = 100 / a
    except ValueError:
        print("Введено не число")
    except ZeroDivisionError :
        print("Введен 0")
    else:
        print("результат: ", b)

def p3():
    try:
        a = input("Введите дату: ")
        a = a.split(".")
        b, god = int(a[0]) * int(a[1]), a[2]
    except IndexError:
        print("неправильная дата")
    except ValueError:
        print("Введена не дата")
    else:
        if int(a[0]) > 31:
            print("такого дня нет")
        if int(a[1]) > 12:
            print("такого месяца нет")
        c = list(god)
        d = int(c[-1] + c[-2])
        if b == d:
            print("Это магическая дата")
        else:
            print("Это не магическая дата")

def p4():
    try:
        a = input("Введите номер билета: ")
        b = list(a)
        if len(b) % 2 == 1:
            print("Это неправильный билет")

        k = int(len(b)/2)
        sum = 0
        for i in range(k):
            sum += int(b[i])
        sum2 = 0
        for i in range(k):
            sum2 += int(b[-(i+1)])
    except ValueError:
        print("Введен не номер")
    else:
        if sum == sum2:
            print("Это счастливый билет")
        else:
            print("Это не счастливый билет")

p1()
p2()
p3()
p4()
