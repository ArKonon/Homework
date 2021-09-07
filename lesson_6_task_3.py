class Worker:
    def __init__(self, name, surname, position=None, wage=0, bonus=0):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}


class Position(Worker):

    def full_income(self):
        return sum(self._income.values())

    def get_full_name(self):
        return '[Person: %s %s is %s ]' % (self.name, self.surname, self.position)


if __name__ == '__main__':
    rick = Position('Rick', 'Sanchez', position='scientist, alcoholic, realist and misanthrope', wage=10000, bonus=500)
    morty = Position('Morty', 'Smith', position="Rick's sidekick")
    print(rick.get_full_name())
    print(f'Total income: {rick.full_income()} Blemflarcks ')
    print(morty.get_full_name())
    print(f'Total income: {morty.full_income()} - sorry Morty, you are too young for salary')
