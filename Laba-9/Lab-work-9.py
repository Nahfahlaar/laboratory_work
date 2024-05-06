import csv
import pathlib
from PIL import Image, ImageFilter

def one_two():
    path = pathlib.Path("ImagesForFilters")
    files_in_directory = list(path.glob('*'))
    
    new_names = ["6.png", "7.png", "8.png", "9.png", "10.png"]

    new_folder = pathlib.Path("ImagesFilters")
    new_folder.mkdir()

    file_type = ["jpg", "png"]

    for i, file in enumerate(files_in_directory):
        if file.suffix[1:] in file_type:
            img = Image.open(file)
            img_filtered = img.filter(ImageFilter.EMBOSS)
            img_filtered.save("ImagesFilters/" + new_names[i])

def three():
    with open("ShoppingList.csv", "r") as file:
        shop_list = csv.reader(file)

        next(shop_list)

        products = {}

        for row in shop_list:
            products[row[0]] = {"Количество": int(row[1]), "Цена": int(row[2])}

    print("Нужно купить:")

    total_sum = 0

    for product, data in products.items():
        total_sum += data["Количество"] * data["Цена"]
        print(f"{product} - {data["Количество"]} шт. за {data["Цена"] * data["Количество"]} руб.")
    
    print(f"\nИтоговая сумма: {total_sum} руб.")
