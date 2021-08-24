earnings = float(input('Введите значение выручки: '))
expenses = float(input('Введите значение издержек: '))
if earnings > expenses:
    profit = earnings - expenses
    print('Фирма отработала с прибылью в', profit, 'рентабельность = ', profit / earnings )
    workers = int(input('Введите число сотрудников'))
    print('Прибыль на одного сотрудника составила: ', profit / workers)
elif earnings < expenses:
    print('Фирма отработала с убытком')
else:
    print('Фирма сработала в ноль.')