def one():
    import random
    list =[]
    for i in range(5):
        list.append(random.randint(1, 10))
    number = int(input("Введите число от 1 до 10: "))
    if number in list:
        print("Поздравляю, Вы угадали число!")
    else:
        print("Нет такого числа!")
#-----------------------------------------------------------
def two():
    import random
    list =[]
    duplicates = []
    for i in range(5):
        list.append(random.randint(1, 10))

    for i in list:
        if i in duplicates:
            print(i)
        elif list.count(i) > 1:
            duplicates.append(i)
#-----------------------------------------------------------
def three():
    week = ("Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье")
    number_of_days_off = int(input("Введите количество выходных дней: "))

    if number_of_days_off > len(week):
        print("Нет столько дней в неделе")
    elif number_of_days_off == 0:
        print("Политика нашей компании не позволяет сотрудникам работать без выходных")
    else:
        days_off = week[-number_of_days_off:]
        work_days = week[:-number_of_days_off]

        print("Ваши выходные дни: ", ", " .join(days_off))
        print("Ваши рабочие дни: ", ", " .join(work_days))
#-----------------------------------------------------------
def four():
    import random

    group_one = ["Иванов", "Петренко", "Кузнецов", "Сиденко", "Ковальчук", "Романенко", "Бондаренко", "Кравченко", "Литвиненко", "Савенко"]
    group_two = ["Смирнов", "Пономарев", "Федоров", "Морозов", "Волошин", "Соколов", "Лебедев", "Григорьев", "Михайлов", "Зайцев"]

    from_the_first_group = tuple(group_one[:5])
    from_the_second_group = tuple(group_two[:5])

    team = from_the_first_group + from_the_second_group

    print(f"Список первой группы: {group_one}", f"Список второй группы: {group_two}", f"Команда: {team}", f"Длина кортежа: {len(team)}", sep="\n")

    list_for_sort = list(team)
    list_for_sort.sort()

    team = tuple(list_for_sort)

    print("Отсортированный кортеж:", team)

    if "Иванов" in team:
        print("Студент Иванов входит в полученную команду")
    else:
        print("Студент Иванов не входит в полученную команду")

    count = 0
    for i in team:
        if i == "Иванов":
            count += 1
    print("Количество студентов в команде с фамилией Иванов:", count)