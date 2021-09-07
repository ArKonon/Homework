class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} начал движение'

    def stop(self):
        return f'{self.name} остановился'

    def turn(self, direction):
        if direction == 'left':
            return f'автомобиль повернул налево'
        elif direction == 'right':
            return f'автомобиль повернул направо'
        else:
            return f'{direction} - невозможно задать направление'

    def show_speed(self):
        return f'автомобиль {self.name} движется со скоростью {self.speed} км в час'

    def police(self):
        if self.is_police is True:
            return f'{self.name} полицейская машина'
        else:
            return f'{self.name} не является полицейской машиной'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            return f'Скорость {self.speed} км в час - выше разрешенной для {self.name} на {self.speed - 60} км в час'
        else:
            return Car.show_speed(self)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            return f'Скорость {self.speed} км в час - выше разрешенной для {self.name} на {self.speed - 40} км в час'
        else:
            return Car.show_speed(self)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 80:
            return f'Скорость {self.speed} км в час - выше разрешенной для {self.name} на {self.speed - 80} км в час'
        else:
            return Car.show_speed(self)


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


opel = TownCar(35, 'red', 'Opel', False)
print(opel.show_speed())
print(opel.go())
print(opel.turn('left'))
print(opel.turn('right'))
print(opel.turn('???'))
print(opel.stop())
print(opel.police())

volga = WorkCar(50, 'white', 'Volga', False)
print(volga.show_speed())
print(volga.go())
print(volga.turn('left'))
print(volga.turn('right'))
print(volga.turn('???'))
print(volga.stop())
print(volga.police())

lexus = SportCar(90, 'black', 'Lexus', False)
print(lexus.show_speed())
print(lexus.go())
print(lexus.turn('left'))
print(lexus.turn('right'))
print(lexus.turn('???'))
print(lexus.stop())
print(lexus.police())

lada = PoliceCar(80,'blue and white', 'Lada Xray', True)
print(lada.show_speed())
print(lada.go())
print(lada.turn('left'))
print(lada.turn('right'))
print(lada.turn('???'))
print(lada.stop())
print(lada.police())