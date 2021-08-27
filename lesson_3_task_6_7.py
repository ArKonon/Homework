def my_func(*args):
    args = input('Введи слова на латинице в нижнем регистре: ')
    if not args.isascii():
        print('Слова не на латинице!')
    elif not args.islower():
        print('Слова не в нижнем регистре!')
    else:
        return args.title()

print(my_func())