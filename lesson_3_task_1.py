a = float(input('Число a = '))
b = float(input('Число b = '))
def delenie(a, b):
    x = a / b
    print(x)
try:
    delenie(a, b)
except ZeroDivisionError:
    print('На ноль делить нельзя!')



