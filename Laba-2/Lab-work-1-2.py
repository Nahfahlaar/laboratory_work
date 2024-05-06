place = input("Введите номер места: ")

if place.isalpha():
    print("Мне нужны цифры")

elif int(place) > 54:
    print("Такого места в вагоне нет")

elif int(place) in range(37, 54):
    print("Боковое место")

elif int(place) % 2 == 0:
    print("Верхнее место")

else:
    print("Нижнее место")