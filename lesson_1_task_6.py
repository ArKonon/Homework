a = float(input('число километров в первый день: '))
b = float(input('число километров, которых необходимо достичь: '))
days = 1
km = a
while km < b:
    a = a + a/10
    days = days + 1
    km = a
print(f'трубуемые результаты будут достигнуты на {days} день')