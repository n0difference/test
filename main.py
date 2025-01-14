def book_list_view(library):
    if library:
        print("В библиотеке есть следующие книги:")
        for book in library.keys():
            print(f"\t{book}")
    else:
        print("В библиотеке нет книг")


def add_book(title, author, year):
    global library
    if not (title in library):
        library[title] = {"Автор": author,
                      "Год выпуска": year,
                      "Наличие в библиотеке": None}
        print(f"\nкнига успешно добавлена", end="\n\n")
    else:
        answer = input("\nДанная книга уже есть в библиотеке\n"
                       "Желаете обноить информацию о книге? \"Да\" или \"Нет\": ").strip().lower()
        if answer == "да":
            library[title] = {"Автор": author,
                              "Год выпуска": year,
                              "Наличие в библиотеке": None}
            print(f"\nкнига успешно обновлена", end="\n\n")


def remove_book(title):
    global library
    if title in library:
        del library[title]
        print(f"\nКнига \"{title}\" была удалена", end="\n\n")
    else:
        print(f"\nКнига \"{title}\" не найдена в библиотеке", end="\n\n")


def issue_book(title):
    global library
    if library[title["Наличие в библиотеке"]]:
        library[title["Наличие в библиотеке"]] = False
        print(f"Вы взяли \"{title}\"")
    else:
        print(f"Кто-то уже взял \"{title}\"")


def return_book(title):
    global library
    if not library[title["Наличие в библиотеке"]]:
        library[title["Наличие в библиотеке"]] = True
        print(f"Вы ввернули \"{title}\"")
    else:
        print(f"Вы уже вернули \"{title}\"")


library = {
    "Язык программирования С": {
        "Автор": "Брайн К., Деннис Р.",
        "Год выпуска": 2009,
        "Наличие в библиотеке": True
    },
    "Внутреннее устройство Microsoft Windows": {
        "Автор": "Руссинович М., Соломон Д., Ионеску А.",
        "Год выпуска": 2014,
        "Наличие в библиотеке": True
    },
    "Reverse Engineering для начинающих": {
        "Автор": "Юричев Д.",
        "Год выпуска": 2013,
        "Наличие в библиотеке": False
    }
}


issue_book("Язык программирования С")

issue_book("Reverse Engineering для начинающих")

return_book("Язык программирования С")