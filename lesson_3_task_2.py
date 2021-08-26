user = dict(
    name = input('Введите имя: '),
    surname = input('Введите фамилию: '),
    city = input('Введите город рождения: '),
    year = input('Введите год рождения: '),
    email = input('Введите адрес электронной почты: '),
    phonenumber = input('Введите номер телефона: ')
            )

def my_func(**kwargs):
    values = kwargs.values()
    values = list(values)
    print("Информация о пользователе : ", ', '.join(values))

my_func(**user)