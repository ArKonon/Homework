from itertools import count
from itertools import cycle

x = int(input("Введите первое число: "))
y = int(input("Введите последнее число: "))

my_list = []
el = x
while y >= el in count(x):
    my_list.append(el)
    el += 1
else:
    print(f'список: {my_list}')

w = int(input('введите количество повторений списка: '))
iter = cycle(my_list)
c = 0
while c < w * len(my_list):
    print(next(iter))
    c += 1
