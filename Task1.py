# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
list = [1, 5, 7, 2, 0, 3, 6]
sum = 0
for i in range(1, len(list), +2):
    sum += list[i]
print(sum)