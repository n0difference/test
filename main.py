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


def test_max_number(num1, num2, answer):
    if max_number(num1, num2) == answer:
        print(f"ok: {max_number(num1, num2)}")
    else:
        print("error in test_max_number, incorrect answer: ", max_number(num1, num2)," | ", answer)


try:
    print("введите 2 чисела и большее среди них")
    num1 = float(input())
    num2 = float(input())
    answer = float(input())
except ValueError:
    print("error: необходимо ввести число")

test_max_number(num1, num2, answer)

try:
    print("введите чисело для отсчета")
    num = float(input())
except ValueError:
    print("error: необходимо ввести число")

for i in even_numbers(num):
    print(i)