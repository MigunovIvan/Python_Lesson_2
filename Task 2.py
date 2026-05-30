# Задание 2:

begin = int(input("Введите цифру начала диапазона:" ))
escape = int(input("Введите цифру конца диапазона:" ))

def ascending_odd(start, end):
    if start > end:
        start, end = end, start
    for number in range(start, end + 1):
        if number % 2 != 0:
            print(number)

ascending_odd(begin, escape)
