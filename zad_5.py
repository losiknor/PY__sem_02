# Дано число из отрезка [10,99]. Показать наибольшую цифру числа.
# num = int(input('Введите число в отрезке [10, 99]: '))
# first_digit = num // 10
# second_digit = num % 10
# if first_digit > second_digit:
#     print(first_digit)
# elif first_digit < second_digit:
#     print(second_digit)
# else:
#     print("Они равны")

# Алгоритм разбора числа на цифры
number = 1233254565258789
numberList = []
while number > 0:
    numberList.append(number % 10)
    number //= 10

numberListLength = len(numberList)
maxNumber = numberList[0]
minNumber = numberList[0]

for i in range(numberListLength):
    if numberList[i] > maxNumber:
        maxNumber = numberList[i]
    elif numberList[i] < minNumber:
        minNumber = numberList[i]
print(f'maxNumber: {maxNumber}, minNumber: {minNumber}')

# Поиск min и max в массиве !!!
print(min(numberList))
print(max(numberList))