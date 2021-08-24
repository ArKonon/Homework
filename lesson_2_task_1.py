my_list = (1, 2.2, "three", -4, True, -10, None, False, [1, 2, 3])
for el in my_list:
    type_of = type(el)
    print(f'{el} is {type_of}')