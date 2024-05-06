from PIL import Image, ImageFilter

def one():
    img = Image.open('Car.jpg')

    img.show()


    print("Ширина:", img.width, "\n",
        "Высота:", img.height, "\n",
        "Формат:", img.format, "\n",
        "Цветная модель:", img.mode)

def two():
    img = Image.open("Car.jpg")

    width, height = img.size

    new_width = int(width / 3)
    new_height = int(height / 3)

    img.thumbnail((new_width, new_height))
    img_horizontal = img.transpose(Image.FLIP_LEFT_RIGHT)
    img_vertical = img.transpose(Image.FLIP_TOP_BOTTOM)

    img.save("SmallCar.jpg")
    img_horizontal.save('CarHorizontal.jpg')
    img_vertical.save('CarVertical.jpg')

def three():
    img_one = Image.open("ImagesForFilters/1.jpg")
    img_two = Image.open("ImagesForFilters/2.jpg")
    img_three = Image.open("ImagesForFilters/3.jpg")
    img_four = Image.open("ImagesForFilters/4.jpg")
    img_five = Image.open("ImagesForFilters/5.jpg")

    new_names = ["6.jpg", "7.jpg", "8.jpg", "9.jpg", "10.jpg"]
    images = [img_one, img_two, img_three, img_four, img_five]

    for i in range(len(images)):
        img_filtered = images[i].filter(ImageFilter.EMBOSS)
        img_filtered.save("ImagesFilters/" + new_names[i])