# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
list = [1.1, 1.2, 3.1, 5, 10.01]
newlist = [] * len(list)
for i in range(0, len(list), +1):
    current = list[i] - int(list[i])
    current = round(current, 5)
    newlist.append(current)
max = newlist[0]
min = newlist[0]
for j in range(1, len(newlist), +1):
    if newlist[j] != 0:
        if newlist[j] > max:
            max = newlist[j]
        elif newlist[j] < min:
            min = newlist[j]
result = max - min
print(result)
