def p1():
    from PIL import Image
    img = Image.open('F:\\sobaken.jpg')
    img.show()
    width, height = img.size
    print(width, height)
    a = img.format
    print(a)
    b = img.mode
    print(b)
def p2():
    from PIL import Image
    image = Image.open('2.jpg')
    image.show()

    new_size = (image.width // 3, image.height // 3)
    image.thumbnail(new_size)
    image.show()
    image.save('new.jpg')

    mirror_image = image.transpose(Image.FLIP_LEFT_RIGHT)
    mirror_image.show()
    mirror_image.save('mirror.jpg')

    rotate_image = image.rotate(180)
    rotate_image.show()
    rotate_image.save('rotate.jpg')
def p3():
    from PIL import Image, ImageFilter
    filename = ["1.jpg", "2.jpg", "3.jpg", "4.jpg", "5.jpg"]
    for file in filename:
        with Image.open(file) as i:
            i.load()
            b = i.filter(ImageFilter.FIND_EDGES)
            b.show()
            b.save("F:\ " + "new" + file)
def p4():
    from PIL import Image
    back = Image.open("img1.jpg")
    fore = Image.open("new.jpg")
    back.show()
    fore.putalpha(200)
    back.paste(fore, (100, 100), fore)
    back.show()
    back.save("new.jpg")
p4()
