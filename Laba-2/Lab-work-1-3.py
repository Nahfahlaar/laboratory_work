month = input("Введите год: ")

if month.isalpha():
    print("Мне нужны цифры")

elif int(month) % 4 == 0 and int(month) % 100 != 0 or int(month) % 400 == 0:
    print("Год " + str(month) + " високостный.")
else:
    print("Год " + str(month) + " не високостный.")