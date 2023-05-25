def p1():
    import json
    with open("file.json", "r", encoding='utf-8') as read_file:
        rf = json.load(read_file)

        f = rf["products"]
        for x in f:
            print("Название: ", x["name"])
            print("Цена: ", x["price"])
            print("Вес: ", x["weight"])
            if x["available"]:
                print("В наличии")
            else:
                print("Нет в наличии!")
            print("")


def p2():
    import json
    name = input("Введите название: ")
    price = input("Введите цену: ")
    weight = input("Введите вес: ")
    available = input("Есть наличии?(да/нет): ")
    if available == "да":
        available = True
    else:
        available = False

    f = {"name": name, "price": price, "weight": weight, "available": available}
    with open("file1.json", "w") as write_file:
        json.dump(f, write_file)

    with open("file1.json", "r") as read_file:
        x = json.load(read_file)
        print("Название: ", x["name"])
        print("Цена: ", x["price"])
        print("Вес: ", x["weight"])
        if x["available"]:
            print("В наличии")
        else:
            print("Нет в наличии!")
def p3():
    s = {}
    with open('en-ru.txt', 'r', encoding='utf-8') as f:
        for line in f:
            line = line.replace('\n', "")
            a = line.split(" - ")
            s[a[0]] = a[1]
    l = {}
    for x in s:
        a = s[x].split(", ")
        if len(a) > 1:
            l[a[0]] = x
            l[a[1]] = x
        else:
            l[a[0]] = x

    #сортировка
    l1 = list(l)
    l1.sort()
    l2 = {}
    for i in l1:
        l2[i] = l[i]

    #в файл
    s = ""
    for x in l2:
        s += x + " - " + l2[x] + "\n"
    print(s)
    with open('ru-en.txt', 'w') as f:
        f.write(s)

p1()
p2()
p3()



