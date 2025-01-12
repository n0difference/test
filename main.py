def book_list_view(library):
    if library.keys():
        print("В библиотеке есть следующие книги:")
        for book in library.keys():
            print(f"\t{book}")
        print()
    else:
        print("В библиотеке нет книг")


def add_book(title, author, year):
    global library
    if title in library.keys():
        answer = input("Данная книга уже есть в библиотеке\nЖелаете обноить информацию о книге? \"Да\" или \"Нет\"")
        if answer == "Да":
            library[title] = {"Автор": author,
                              "Год выпуска": year,
                              "Наличие в библиотеке": None}
            print("книга успешно добавлена", end="\n\n")
    else:
        library[title] = {"Автор": author,
                          "Год выпуска": year,
                          "Наличие в библиотеке": None}
        print("книга успешно добавлена", end="\n\n")



library = {"Язык программирования С": {"Автор": "Брайн К., Деннис Р.",
                                       "Год выпуска": 2009,
                                       "Наличие в библиотеке": True},
           "Внутреннее устройство Microsoft Windows": {"Автор": "Руссинович М., Соломон Д., Ионеску А.",
                                                       "Год выпуска": 2014,
                                                       "Наличие в библиотеке": True},
           "Reverse Engineering для начинающих": {"Автор": "Юричев Д.",
                                                  "Год выпуска": 2013,
                                                  "Наличие в библиотеке": False}}

book_list_view(library)

add_book("Компьютерные вирусы изнутри и снаружи", "Крис Касперски", 2006)

book_list_view(library)