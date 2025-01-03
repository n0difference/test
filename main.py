def max_number(a, b):
    assert ((type(a) == int or type(a) == float) and (type(b) == int or type(b) == float)), "аргументы должны быть числами"
    if a > b:
        return a
    else:
        return b


def empty_function():
    pass


def even_numbers(n):
    i = 0
    while i < n:
        yield i
        i += 2


testArray1 = [13, 43, 55, -1000, 0.1, 1]
testArray2 = [5, 55, -1, -500, -0.5, 1]
answerArray = [13, 55, 55, -500, 0.1, 1]

for i in range(len(answerArray)):
    if (max_number(testArray1[i], testArray2[i]) == answerArray[i]):
        print(f"{i} тест правильный")
    else:
        print(f"ошибка в тесте {i}")
