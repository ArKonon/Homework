time = int(input('Введите время в секундах: '))
hours = time // 3600
mins = (time - hours * 3600) // 60
seconds = time - (hours * 3600 + mins * 60)
print(f"Время в формате чч:мм:сс {hours} : {mins} : {seconds}")