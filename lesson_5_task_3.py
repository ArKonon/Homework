with open('text_3.txt', 'r', encoding='utf-8') as my_file:
    sal = []
    worker_list = []
    my_list = my_file.read().split('\n')
    for i in my_list:
        i = i.split()
        if float(i[1]) < 20000:
            worker_list.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 : {worker_list}')
print(f'Средний оклад: {sum(map(float, sal)) / len(sal)}')
