my_f = open("task_2.txt", "r")

lines = [line for line in list(my_f) if line != '\n']
print(f'количество строк в файле : {len(lines)}')

for line in lines:
    print(f' строка {line[:]} содержит {len(line.split())} слов. ')

my_f.close()