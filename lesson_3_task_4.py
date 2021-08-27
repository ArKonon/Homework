def my_func(x, y):
    return x ** y


def my_other_func(x, y):
    i = 1
    a = abs(y)
    b = x
    while i < a:
        b = b * x
        i = i + 1
    return 1 / b


x = int(input('Введите действительное положительное число: '))
y = int(input('Введите целое отрицательное число: '))

if x > 0 > y:
    print(my_func(x, y))
    print(my_other_func(x, y))

else:
    print('Некорректный ввод!')
