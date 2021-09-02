filename = "task_1.txt"


with open(filename, 'w', encoding='utf-8') as file:
    while True:
        user_input = input('Введите произвольную строку: ')
        if not user_input:
            break

        file.write(f'{user_input}\n')

