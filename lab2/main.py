def p1():
    par = input("Введите пароль: ")
    if len(par) < 6:
        print("Пароль слишком короткий")
    else:
        par1 = input("Введите повторный пароль: ")
        if par == par1:
            print("Пароль принят")

def p2():
    vag = int(input("Введите номер вагона: "))
    if vag <= 54 and vag >= 1:
        if vag <= 35 and vag % 2 == 1:
            print("Нижнее, плацкарт")
        elif (vag <= 54 and vag >= 38 and vag % 2 == 0):
            print("Верхнее, боковое")
        elif (vag <= 36 and vag % 2 == 0):
            print("Верхнее, плацкарт")
        else:
            print("Нижнее, боковое")
    else:
        print("Такого места нет")


def p3():
    god = int(input("Введите год: "))
    if god % 4 == 0:
        if god % 100 != 0:
            print("Високосный")
        else:
            if god % 400 == 0:
                print("Високосный")
            else:
                print("Невисокосный")
    else:
        print("Невисокосный")

def p4():
    cvet1 = input("Введите 1 цвет (красный, синий, желтый) : ")
    cvet2 = input("Введите 2 цвет (красный, синий, желтый) : ")
    if (cvet1 == "красный" and cvet2 == "синий") or (cvet2 == "красный" and cvet1 == "синий"):
        print("фиолетовый")
    elif (cvet1 == "красный" and cvet2 == "желтый") or (cvet2 == "красный" and cvet1 == "желтый"):
        print("оранжевый")
    elif (cvet1 == "синий" and cvet2 == "желтый") or (cvet2 == "синий" and cvet1 == "желтый"):
        print("зеленый")
    else:
        print("Ошибка")

def p5():
    N = int(input("Введите количество слов: "))
    a = 0
    s = ""
    while a < N:
        s += (input("Введите слово: ")) + " "
        a += 1
    print(s)


p1()
p2()
p3()
p4()
p5()
