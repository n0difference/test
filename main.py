def book_list_view(library):
    if library:
        print("В библиотеке есть следующие книги:")
        for book in library.keys():
            print(f"\t{book}")
    else:
        print("В библиотеке нет книг")


def add_book(title, author, year):
    global answer
    global library
    if title in library:
        answer = input("\nДанная книга уже есть в библиотеке\n"
                       "Желаете обноить информацию о книге? \"Да\" или \"Нет\": ").strip().lower()
        if answer == "нет":
            return
    library[title] = {"Автор": author,
                      "Год выпуска": year,
                      "Наличие в библиотеке": None}
    print(f"\nкнига успешно {'обновлена' if answer == 'да' else 'добавлена'}", end="\n\n")


library = {"Язык программирования С": {"Автор": "Брайн К., Деннис Р.",
                                       "Год выпуска": 2009,
                                       "Наличие в библиотеке": True},
           "Внутреннее устройство Microsoft Windows": {"Автор": "Руссинович М., Соломон Д., Ионеску А.",
                                                       "Год выпуска": 2014,
                                                       "Наличие в библиотеке": True},
           "Reverse Engineering для начинающих": {"Автор": "Юричев Д.",
                                                  "Год выпуска": 2013,
                                                  "Наличие в библиотеке": False}}


answer = ""

book_list_view(library)

add_book("Компьютерные вирусы изнутри и снаружи", "Крис Касперски", 2006)

book_list_view(library)

add_book("Компьютерные вирусы изнутри и снаружи", "Крис Касперски", 2002)

book_list_view(library)