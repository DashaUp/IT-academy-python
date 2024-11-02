class Human:

    def __init__(self, name = 'human'):
        self.name = name


class Auto:

    def __init__(self, brand):
        self.brand = brand
        self.passengers = []

    def add_passenger(self, *humans):
        for human in humans:
            self.passengers.append(human)

    def print_passengers_name(self):
        if self.passengers:
            print ( f'Names of {self.brand} passengers' )
            for passenger in self.passengers:
                print(passenger.name)
        else:
            print('There are no passengers =(')


kate = Human(name='kate')
nick = Human(name='nick')

car = Auto('mercedes')
car.add_passenger(kate, nick)
car.add_passenger(nick)
car.print_passengers_name()