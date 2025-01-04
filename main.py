def max_number(a, b):
    try:
        if a > b:
            return a
        else:
            return b
    except:
        print("error max_number")


def empty_function():
    pass


def even_numbers(n):
    try:
        i = 0
        while i <= n:
            yield i
            i += 2
    except:
        print("error even_numbers")


def test_max_number(num1, num2):
    try:
        if max_number(num1, num2) == max(num1, num2):
            print(f"ok: {max_number(num1, num2)}")
        else:
            print("error in test_max_number, incorrect answer: ", max_number(num1, num2)," | ", max(num1, num2))
    except:
        print("error in test_max_number")


def data_input(n):
    try:
        print(f"введите {n} чисел")
        numbers_array = [0] * n
        for i in range(n):
            numbers_array[i] = float(input())
        return numbers_array
    except ValueError:
        print("error: необходимо ввести число")



test_array = data_input(2)  # когда я пытелся передать напрямую, он дважды вызывал функцию
                            # и я так и не понял как это сделать без промежуточного массива
test_max_number(test_array[0], test_array[1])

for i in even_numbers(data_input(1)[0]):
    print(i)