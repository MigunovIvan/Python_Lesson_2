# Задание 4

n = int(input("Введите число: "))

trash = 0

for i in range(1, n + 1):
    trash = trash + i

print("Сумма чисел от одного и до", n, "будет равна числу" ,trash)
