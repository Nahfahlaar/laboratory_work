password = input("Введите пароль ")

if len(password) >= 5:
    passwordRepeat = input("Повторите ввод пароля ")
    if password == passwordRepeat:
        print("Пароль принят")
    else:
        print("Пароль не принят")
else:
    print("Пароль должен быть длинной не меньше 5 символов.")