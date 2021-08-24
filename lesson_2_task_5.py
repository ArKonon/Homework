my_list = [7, 5, 3, 3, 2]
print(f'{my_list} - текущий рейтинг.')
rating_num = int(input('Введите ваш балл, (404 - выход): '))
while rating_num != 404:
    index = None
    for i, num in enumerate(my_list):
        if rating_num > num:
            index = i
            break
    if index is None:
        my_list.append(rating_num)
    else:
        my_list.insert(index, rating_num)
    print(f'{my_list} - обновленный рейтинг.')
    rating_num = int(input('Введите ваш балл: '))
