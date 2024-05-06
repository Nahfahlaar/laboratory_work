def one(n):
    number = n
    if number % 3 == 0:
        print("Число делится")
    else:
        print("Число не делится")


#-------------------------------------------------------------
def two():
    try:
        num = int(input("Введите число: "))
        divide_user_number(num)
    except ValueError:
        print("Вы ввели строку")
    except ZeroDivisionError:
        print("На ноль делить нельзя")


def divide_user_number(number):
    result = 100 / number
    print(int(result))
#-------------------------------------------------------------
def three(day, month, year):
    if day * month == int(str(year)[-2:]):
        print("True")
        return True
    else:
        print("False")
        return False
#-------------------------------------------------------------

def four(number: str):
    if len(number) %2 == 0:
        half_length = len(number) // 2
        first_half = number[:half_length]
        second_half = number[half_length:]

        if sum(int(digit) for digit in first_half) == sum(int(digit) for digit in second_half):
            print("Билет счасливый")
        else:
            print("Билет не счастливый")

    else:
        print("Вы ввели нечётное количество цифр")