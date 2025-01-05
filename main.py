def max_number(a, b):
    if a > b:
        return a
    else:
        return b


def empty_function():
    pass


def even_numbers(n):
    i = 0
    while i <= n:
        yield i
        i += 2


def test_max_number():
    test_list = [[5, 2, 5], [-1, 3, 3], [-5, -4, -4], [2.2, 3, 3], [4.4, -1, 4.4], [-5.2, -99.1, -5.2]]
    for i in test_list:
        assert  ((type(i[0]) == int or type(i[0]) == float) and \
                (type(i[1]) == int or type(i[1]) == float) and \
                (type(i[2]) == int or type(i[2]) == float)), "аргументы должны быть числами"
        if max_number(i[0], i[1]) == i[2]:
            print(f"ok: {max_number(i[0], i[1])}")
        else:
            print("error in test_max_number, incorrect answer: ", max_number(i[2], i[1])," | ", i[2])


test_max_number()

try:
    print("введите чисело для отсчета")
    num = float(input())
except ValueError:
    print("error: необходимо ввести число")

for i in even_numbers(num):
    print(i)