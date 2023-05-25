def p1():
    from PIL import Image
    name = "sobaken.jpg"
    with Image.open(name) as img:
        img.load()

    img.show()
    widht, height = img.size
    f = img.format
    m = img.mode
    print("Ширина", widht)
    print("Высота", height)
    print("Формат", f)
    print("Цвет", m)

def p2():
    from PIL import Image
    name = "sobaken.jpg"
    with Image.open(name) as img:
        img.load()

    nimg = img.resize((img.width // 3, img.height // 3))

    nimg.save("sobaken1.jpg")
    nimg = img.rotate(180)
    nimg.save("sobaken2.jpg")
    nimg = img.transpose(Image.FLIP_LEFT_RIGHT)
    nimg.save("sobaken3.jpg")

def p3():
    from PIL import Image, ImageFilter
    name = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    for f in name:
        with Image.open(f) as img:
            img.load()
            img = img.filter(ImageFilter.FIND_EDGES)
            img.save("new\ " + "new" + f)

def p4():
    from PIL import Image

    img = Image.open('sobaken.jpg')
    watermark = Image.open('watermark.png')

    img.paste(watermark, (50, 50), watermark)
    img.save("watermarksobaken.png")
    
import os
os.mkdir(path = ('new'))

p1()
p2()
p3()
p4()
