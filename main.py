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
        assert max_number(i[0], i[1]) == i[2], f"error: max_number({i[0]}, {i[1]}) = {max_number(i[0], i[1])}, must: {i[2]}"
    return "ok"


print(test_max_number())

try:
    print("введите чисело для отсчета")
    num = float(input())
except ValueError:
    print("error: необходимо ввести число")

for i in even_numbers(num):
    print(i)