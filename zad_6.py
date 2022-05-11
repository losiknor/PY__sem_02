# Выяснить кратно ли число заданному, если нет, вывести остаток.
# number = int(input('Enter 1- number: '))
# number2 = int(input('Enter 2- number: '))
# if number % number2 == 0:
#     print("Multiplicity")
# else:
#     print(f"Not multiple, reminder {number % number2}")

# второй вариант - через логику
n1 = int(input("Введите число 1: "))
n2 = int(input("Введите число 2: "))

if n1 % n2:
    print(f"остаток от деления:  {n1 % n2}")
else:
    print(f"{n1} кратно {n2}")