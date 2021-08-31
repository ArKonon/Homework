from math import factorial


def fact(n):
    for i in range(1, n + 1):
        yield factorial(i)


x = int(input('введите число вычесленных факториалов: '))
for el in fact(x):
    print(el)
