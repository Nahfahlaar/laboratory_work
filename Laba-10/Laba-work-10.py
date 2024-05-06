import os
import json

def one():
    filename = "ShoppingList.json"
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, filename)

    with open(file_path, "r", encoding="utf-8") as file:
        shop_list = json.load(file)
    
    for product in shop_list["products"]:
        name = product["name"]
        price = product["price"]
        weight = product["weight"]
        available = product['available']

        print(f"Название: {name}\nЦена: {price}\nВес: {weight}")

        if available:
            print("В наличии")
        else:
            print("Нет в наличии!")

        print()


    new_product_name = input("Введите название нового продукта: ")
    new_product_price = int(input("Введите цену нового продукта: "))
    new_product_available = input("Есть ли новый продукт в наличии? (да/нет): ") == "да"
    new_product_weight = int(input("Введите вес нового продукта: "))

    shop_list["products"].append({
        "name": new_product_name,
        "price": new_product_price,
        "weight": new_product_weight,
        "available": new_product_available
    })

    with open(file_path, "w", encoding="utf-8") as file:
        json.dump(shop_list, file, indent=4, ensure_ascii=False)

        for product in shop_list["products"]:
            name = product["name"]
            price = product["price"]
            weight = product["weight"]
            available = product['available']

    
            print(f"Название: {name}\nЦена: {price}\nВес: {weight}")

            if available:
                print("В наличии")
            else:
                print("Нет в наличии!")

            print()

def three():
    file_name = "en-ru.txt"
    current_dir = os.path.dirname(__file__)
    file_path = os.path.join(current_dir, file_name)
    with open(file_path, 'r', encoding="utf-8") as file:
        ru_en = file.readlines()
    
    swapped_lines = []
    for line in ru_en:
        line = line.strip()
        words = line.split(" - ")
        words.reverse()
        swapped_line = ' - '.join(words)
        swapped_lines.append(swapped_line)

    with open("ru-en.txt", 'w', encoding="utf-8") as file:
        for line in swapped_lines:
            file.write(line + "\n")
