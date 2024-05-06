def one():
    result = ""

    for i in range(2):
        word = input("Введите слово")
        result += word + " "
    print(result)

def two():
    result = ""

    while True:
        word = input("Введите слово")
        if word == "stop":
            break
        else:
            result += word + " "
    print(result)

def three():
    word = input("Введите слово")

    if "ф" in word or "Ф" in word:
        print("Ого! Это редкое слово!")
    else:
        print("Эх, это не очень редкое слово...")

def four():
    import random
    counter = 0
    counterError = 0
    while counterError != 3:
        numberOne = random.randint(1, 10)
        numberTwo = random.randint(1, 10)
        answer = numberOne + numberTwo

        playerAnswer = int(input(f"{numberOne} + {numberTwo} = "))

        if answer == playerAnswer:
            counter += 1
            print("Правильно!")
        else:
            counterError += 1
            print("Ответ неверный")
    print(f"«Игра окончена. Правильных ответов: {counter}")