def one():
    countries_capitals = {
        "Россия": "Москва",
        "США": "Вашингтон",
        "Франция": "Париж",
        "Германия": "Берлин",
        "Италия": "Рим",
        "Испания": "Мадрид",
        "Канада": "Оттава",
        "Австралия": "Канберра"
    }
    for key, value in countries_capitals.items():
        print(key, "-", value)

    country = "Россия"
    capital = countries_capitals[country]
    print("Столица", capital)

    sorted_countries = sorted(countries_capitals.items())

    for key, value in sorted_countries:
        print(key, "-", value)

def two():
    scores = {
        'А': 1, 'В': 1, 'Е': 1, 'И': 1, 'Н': 1, 'О': 1, 'Р': 1, 'С': 1, 'Т': 1,
        'Д': 2, 'К': 2, 'Л': 2, 'М': 2, 'П': 2, 'У': 2,
        'Б': 3, 'Г': 3, 'Ё': 3, 'Ь': 3, 'Я': 3,
        'Й': 4, 'Ы': 4,
        'Ж': 5, 'З': 5, 'Х': 5, 'Ц': 5, 'Ч': 5,
        'Ш': 8, 'Э': 8, 'Ю': 8,
        'Ф': 10, 'Щ': 10, 'Ъ': 10
    }

    word = input("Введите слово: ")
    word = word.upper()

    count = 0
    for i in word:
        if i in scores:
            count += scores[i]

    print("В слове", word, count, "очков")

def three():
    import random
    languages = ["Русский", "Английский", "Французский", "Китайский", "Польский", "Сербский"]
    students = ["Саня", "Артём", "Витя", "Лена", "Макс", "Костя", "Серёга", "Ксюша", "Женя", "Полина"]

    students_languages = {}

    for i in students:
        num_elements = random.randint(1, len(languages))
        random_languages = random.sample(languages, num_elements)
        students_languages[i] = random_languages

    all_languages = set()

    for languages in students_languages.values():
        all_languages.update(languages)

    print(list(all_languages))

    ch_speakers = []

    for i, languages in students_languages.items():
        if "Китайский" in languages:
            ch_speakers.append(i)
    print("Эти студенты знают китайский язык: ", ch_speakers)

one()