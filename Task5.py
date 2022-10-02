# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
def fibonacci(num):
    nums = []
    x, y = 1, 1
    for i in range(num - 1):
        nums.append(x)
        x, y = y, x + y
    x, y = 0, 1
    for i in range(num):
        nums.insert(0, x)
        x, y = y, x - y
    return nums

result = fibonacci(8)
print(result)
