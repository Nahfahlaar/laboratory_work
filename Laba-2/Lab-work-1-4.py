colorOne = input("Веедите цвет 1 (с маленькой буквы): ")
colorTwo = input("Введите цвет 2 (с маленькой буквы): ")

if colorOne.isdigit() or colorTwo.isdigit():
    print("Цифры тут не катят")

elif colorOne == colorTwo:
    print(colorOne)

elif (colorOne == "красный" or colorTwo == "красный") and (colorOne == "синий" or colorTwo == "синий"):
    print("фиолетовый")

elif (colorOne == "красный" or colorTwo == "красный") and (colorOne == "жёлтый" or colorTwo == "жёлтый"):
    print("оранжевый")

elif (colorOne == "синий" or colorTwo == "синий") and (colorOne == "жёлтый" or colorTwo == "жёлтый"):
    print("оранжевый")
else:
    print("В программе нет такого цвета, либо ты насписал не цвет вовсе")