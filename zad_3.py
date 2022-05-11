# Показать числа от -N до N
n = int(input('Введи число N: '))
# for i in range(-n, n + 1):
#     print(i, end = ';  ')
i = -n
while i <= n:
    print(i)
    i += 1


# Дополнительная информация по WHILE от препода
# break         прерывает цикл
# continue      пропускает итерацию, то что ниже него
# else          отрабатывает, когда условие в while становится false
