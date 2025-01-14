def book_list_view(library):
    if library.keys():
        print("В библиотеке есть следующие книги:")
        for i in library.keys():
            print(i)
    else:
        print("В библиотеке нет книг")


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