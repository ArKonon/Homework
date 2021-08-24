count_elems = int(input('Введите количество элементов списка: '))
my_list = []
i = 0
el = 0
while i < count_elems:
    my_list.append(input('Введите следующий элемент списка: '))
    i += 1
for elem in range(int(len(my_list)/2)):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
    el += 2
print(my_list)

