try:
    num1 = float(input("введите 1 число:"))
    num2 = float(input("введите 2 число:"))
except ValueError:
    print("необходимо ввести число")
except ZeroDivisionError:
    print("второе число не может быть 0")
else:
    print(f"{num1}/{num2}={num1 / num2}")
finally:
    print("конец программы")