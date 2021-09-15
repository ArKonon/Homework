class MyZeroDeivisionError(Exception):
    text = 'Делить на ноль запрещено!'

    def __str__(self):
        return self.text

class Number(float):
    def __truediv__(self, other):
        if other is not None and not other:
            raise MyZeroDeivisionError

        return Number(float(self) / float(other))


if __name__ == '__main__':
    while True:
        try:
            dividend, divider = map(Number, input('Введите делимое и делитель через пробел: ').split())
            print(dividend / divider)
        except MyZeroDeivisionError as e:
            print(e)
        except ValueError as e:
            print(e)
            break
