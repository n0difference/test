def even_sum():
    even_sum = 0
    for i in range(0,101,2):
        even_sum += i
    return even_sum


def num_counter():
    num = 0
    count = 0
    while num >= 0:
        num = float(input("введите число: "))
        count += 1
    return count


print(even_sum())

squares = [n**2 for n in range(1,11,2)]
print(squares)

print(num_counter())