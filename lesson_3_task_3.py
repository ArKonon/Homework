a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
c = int(input('Введите число c: '))


def my_func(*numbers):
    for number in numbers:
        if min(numbers) < number < max(numbers):
            return number + max(numbers)
        elif number == min(numbers):
            return min(numbers) + max(numbers)
        elif number == max(numbers):
            return max(numbers) * 2
        else:
            return number * 2

print(my_func(a, b, c))
