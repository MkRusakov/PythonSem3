# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
list = [1, 5, 7, 2, 0, 3]
count = int(len(list)/2)
current = int(len(list)-1)
for i in range(0, count, +1):
    result = list[i] * list[current]
    current -= 1
    print(result)