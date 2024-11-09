import random

brands_of_car = {
"Volvo": { "fuel": 10, 'strength': 150,"consumption": 10},
"Volkswagen": { "fuel": 10, 'strength': 105,"consumption": 10},
"Toyota": { "fuel": 10, 'strength': 150,"consumption": 10},
"Ford": { "fuel": 10, 'strength': 105,"consumption": 10},
"Mercedes-Benz": { "fuel": 10, 'strength': 105,"consumption": 10},
"BMW": { "fuel": 10, 'strength': 105,"consumption": 10},
"Kia": { "fuel": 10, 'strength': 105,"consumption": 10},
"Audi": { "fuel": 10, 'strength': 105,"consumption": 10}
}
class Auto:

    def __init__(self, brands_list):
        self.brand = random.choice(list(brands_list))
        print(self.brand)
        self.fuel = brands_list[self.brand]['fuel']
        self.strength = brands_list[self.brand]['strength']
        self.consumption = brands_list[self.brand]['consumption']

    def drive(self):
        if self.strength > 0 and self.fuel >= self.consumption:
            self.fuel -= self.consumption
            self.strength -= 1
            return True
        else:
            print('car cannot move')
            return False
