def data_input():
    try:
        num = int(input("введите число от 1 до 5: "))
        return num
    except ValueError:
        print("необходимо ввести 1 символ, из списка: \n\"1\", \"2\", \"3\", \"4\", \"5\"")


def num_translate(num):
    if num == 1:
        print("one")
    elif num == 2:
        print("two")
    elif num == 3:
        print("three")
    elif num == 4:
        print("four")
    elif num == 5:
        print("five")
    else:
        print("error: введено неправильное значение")


num_translate(data_input())
