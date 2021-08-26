name = input('Введите имя: ')
surname = input('Введите фамилию: ')
year = input('Введите год рождения: ')
city = input('Введите город проживания: ')
email = input('Введите email: ')
telephone = input('Введите телефон:  ')

def user_info(*kwargs):
    print(*kwargs)

user_info(name, surname, year, city, email, telephone)