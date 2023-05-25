def p1():
    from PIL import Image
    name = "post.jpg"
    with Image.open(name) as img:
        img.load()

    img = img.crop((100, 200, 650, 500))
    img.save('newpost.jpg')
    img.show()

def p2():
    from PIL import Image

    p = {"8": "8m.jpg", "23": "23f.jpg", "9": "9m.jpg"}
    f = str(input("Какой праздник?(назовите число) "))
    file = p[f]
    with Image.open(file) as img:
        img.load()
    img.show()

def p3():
    from PIL import Image, ImageDraw, ImageFont

    name = str(input("Ваше имя? "))
    image = Image.open("post.jpg")

    font = ImageFont.truetype("calibri.ttf", 30)
    drawer = ImageDraw.Draw(image)
    drawer.text((50, 20), name + ", поздравляю!", font=font, fill='orange', stroke_width=1, stroke_fill="orange")
    image.save('new_img.png')
    image.show()

p1()
p2()
p3()