def data_input():
    try:
        num = int(input("введите целое положительное число: "))
        assert num > 0, "число должно быть больше 0"
        return num
    except ValueError:
        print("error: необходимо ввести целое положительное число")
        return 0


def countdown(num):
    while num >= 0:
        print(num)
        num -= 1


countdown(data_input())