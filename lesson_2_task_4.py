my_str = input('Введите строку: ')
for idx, word in enumerate(my_str.split()):
    print(idx + 1, (word, word[:10])[len(word) > 10])

