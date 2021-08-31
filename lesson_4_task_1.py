from sys import argv

name, time, rate_per_hour, bonus = argv

try:
    time = int(time)
    rate_per_hour = int(rate_per_hour)
    bonus = int(bonus)
    earnings = time * rate_per_hour + bonus
    print(f'зарплата сотрудника: {earnings} ')
except ValueError:
    print('Введены неверные данные - только целые числа')