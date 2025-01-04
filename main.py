def data_input(str):
    print(str)
    num1 = float(input("введите 1 число: "))
    num2 = float(input("введите 2 число: "))
    return num1, num2


def choice_of_action(str, num_tuple):
    if str == "сложения":
        return (num_tuple[0] + num_tuple[1])
    elif str == "вычитания":
        return (num_tuple[0] - num_tuple[1])
    elif str == "умножения":
        return (num_tuple[0] * num_tuple[1])
    elif str == "деления":
        try:
            return (num_tuple[0] / num_tuple[1])
        except ZeroDivisionError:
            print("Делитель не может быть равен нулю")
    else:
        return "error"


strAraay = ["сложения","вычитания","умножения","деления"]

for i in strAraay:
    print(f"результат {i}:", choice_of_action(i, data_input(f"введите числа для {i}")))