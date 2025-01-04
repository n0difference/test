def vvod(str):
    print(str)
    num1 = float(input("введите 1 число: "))
    num2 = float(input("введите 2 число: "))
    return [num1, num2]

def action(str, num1, num2):
    if str == "сложения":
        return (num1 + num2)
    elif str == "вычитания":
        return (num1 - num2)
    elif str == "умножения":
        return (num1 * num2)
    elif str == "деления":
        assert num2 != 0, print("Делитель не может быть равен нулю")
        return (num1 / num2)
    else:
        return "error"


strAraay = ["сложения","вычитания","умножения","деления"]
resultArray =[]

for i in strAraay:
    resultArray = vvod(f"введите числа для {i}")
    print(f"результат {i}:", action(i, resultArray[0], resultArray[1]))