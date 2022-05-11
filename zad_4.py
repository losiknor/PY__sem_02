# Показать последнюю цифру трёхзначного числа
# digit = input('--->  ')
# print(digit[-1])

# вариант записи того же решения
# digit = input('--->  ')[-1]
# print(digit)

# с числовым форматом
# number = int(input('Введи трехзначное число: '))
# if 99 < number < 1000 :
#     lastDigit = number % 10
#     print(f'Поcледняя цифра {lastDigit}')
# else:
#     print('Не трехзначное')

# то же самое с проверкой в цикле  while  корректности ввода
while True:
    number = int(input('Введи трехзначное число: '))
    if 99 < number < 1000 :
        print(f'Поcледняя цифра ---> {number % 10}')
        break
    else:
        print('Не трехзначное')

# генерация рандомных чисел в Python  - нужно импортировать библиотеку
# import random
# number = random.randint(101, 999)
