my_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55, 56, 346]
new_list = [item for id, item in enumerate(my_list) if my_list[id - 1] < my_list[id]]

print(new_list)
