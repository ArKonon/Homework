def my_sum():
    sum_res = 0
    end = False
    while end == False:
        number = input('Введите числа через пробел или q для выхода - ').split()
        res = 0
        for el in range(len(number)):
            if number[el] == 'q':
                end = True
                break
            if number[el] != 'q':
                res = res + int(number[el])
                continue
        sum_res = sum_res + res
        print(f'Текущая сумма чисел: {sum_res}')
    print(f'Окончательная сумма чисел: {sum_res}')


my_sum()
