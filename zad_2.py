# По заданному номеру дня недели вывести его название
 
# Первый способ решения
# week = ['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье']
# day = int(input('Введите номер дня недели: '))
# if 1 <= day <= 7:
#     print(f'Это {week[day-1]}')
# else:
#     print('Номер дня недели введен неверно.')


# Второй способ
WeekDays = ["Monday", 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
number = int(input('Enter the number: ')) - 1
if number <= 0 or number >= len(WeekDays):
    print("Not")
else:
    print(WeekDays[number])