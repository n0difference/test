def data_input():
    try:
        num = int(input("введите целое положительное число: "))
        assert num > 0
        return num
    except:
        print("error: необходимо ввести целое положительное число")


def countdown(num):
    while num >= 0:
        print(num)
        num -= 1


countdown(data_input())