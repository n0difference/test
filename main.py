def data_input(str):
    print(str)
    num1 = float(input("введите 1 число: "))
    num2 = float(input("введите 2 число: "))
    return num1, num2


def choice_of_action(act, num_tuple):
    try:
        if act == "сложения":
            return (num_tuple[0] + num_tuple[1])
        elif act == "вычитания":
            return (num_tuple[0] - num_tuple[1])
        elif act == "умножения":
            return (num_tuple[0] * num_tuple[1])
        elif act == "деления":
            return (num_tuple[0] / num_tuple[1])
        else:
            return "error: неверное действие"
    except ZeroDivisionError:
        print("Делитель не может быть равен нулю")


action_array = ["сложения","вычитания","умножения","деления"]

for i in action_array:
    print(f"результат {i}:", choice_of_action(i, data_input(f"введите числа для {i}")))