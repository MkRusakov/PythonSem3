# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
def function (num):
    result = ""
    while num != 0:
        result = str(num % 2) + result
        num //= 2
    print(result)
function(45)
