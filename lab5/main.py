def p1():
    a = [1, 2, 3, 4, 5]
    n = int(input("Какое число? "))
    print(*a)
    print("Ваше число ", n)
    if n in a:
        print("Поздравляю, вы угадали число!")
    else:
        print("Нет такого числа!")


def p2():
    a = [1, 1, 3, 4, 5, 3]
    print(a)
    s = "Повторяются: "
    for i in range(0, len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                s += " " + str(a[i])
    print(s)


def p3():
    a = ("ПН", "ВТ", "СР", "ЧТ", "ПТ", "СБ", "ВС")
    n = int(input("Сколько выходных? "))
    print("Ваши выходные дни ", a[-n:])
    print("Ваши рабочие дни ", a[:-n])


def p4():
    from random import randint

    a = ["А1", "А2", "А3", "А4", "А5", "А6", "А7", "А8", "А9", "А10"]
    b = ["Б1", "Б2", "Б3", "Б4", "Б5", "Б6", "Б7", "Б8", "Б9", "Б10"]
    members = []
    while len(members) < 5:
        member = a[randint(0,9)]
        if member not in members:
            members.append(member)
    while len(members) < 10:
        member = b[randint(0,9)]
        if member not in members:
            members.append(member)
    mem = tuple(members)

    print("Группа 1: ", a)
    print("Группа 2: ", b)
    print("Спортивная команда: ", mem)
    print("Количество участников: ", len(mem))
    print("Спортивная команда по алфавиту: ", tuple(sorted(members)))
    print("------------------------")
    print("Проверяем, входит ли в команду студент")
    x = input("Какого студента проверить(по-русски): ")
    k = 0
    for m in mem:
        if x == m:
            k += 1
    if k > 0:
        print("Входит", k, " раз")
    else:
        print("Не входит")

p1()
p2()
p3()
p4()