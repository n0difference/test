def max_number(a, b):
    assert ((type(a) != bool) and type(b) != bool), "аргументы должны быть числами"
    #try/except пропускает bool и я не знаю, как ему сказать не делать это
    try:
        if a > b:
            return a
        else:
            return b
    except:
        print("аргументы должны быть числами")



def empty_function():
    pass


def even_numbers(n):
    i = 0
    while i <= n:
        yield i
        i += 2


def test(num1, num2):
    if max_number(num1, num2) == max(num1, num2):
        print("ok")
    else:
        print("error: ", max_number(num1, num2)," | ", max(num1, num2))

testArray1 = [13, 43, 55, -1000, 0.1, 1,]
testArray2 = [5, 55, -1, -500, -0.5, 1,]

for i in range(len(testArray1)):
    test(testArray1[i],testArray2[i])