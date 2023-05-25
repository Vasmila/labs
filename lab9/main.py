
def p1():
    import os
    from PIL import Image, ImageFilter

    os.mkdir(path = ('new1'))

    rez = os.listdir(path=('files'))
    for f in rez:
        with Image.open('files\\' + f) as img:
            img.load()
            img = img.filter(ImageFilter.FIND_EDGES)
            img.save("new1\ " + "new" + f)


def p2():
    import os
    from os import path
    from PIL import Image, ImageFilter

    os.mkdir(path = 'new2')

    rez = os.listdir()
    for f in rez:
        r = str(path.splitext(f)[1])
        if r == '.jpg':
            with Image.open(f) as img:

                img.load()
                img = img.filter(ImageFilter.FIND_EDGES)
                img.save("new2\ " + "new" + f)


def p3():
    import csv
    print("Нужно купить:")
    sum = 0
    with open('file.csv', newline='') as f:
        r = csv.reader(f, delimiter=";")
        for n in r:
            sum += int(n[2]) * int(n[1])
            print(n[0] + ' - ' + n[1] + ' шт. за ' + n[2] + ' руб.')
    print("Итоговая сумма: " + str(sum))

p1()
p2()
p3()