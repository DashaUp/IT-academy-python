import random

class Human:

    def __init__(self,
        name="human", job=None, home=None, car=None
    ):
        self.name = name
        self.job = job
        self.home = home
        self.car = car

        self.monay = 100
        self.gladness = 50
        self.food = 50

    def get_home(self):
        self.home = House()

    def get_car(self):
        self.car = Auto(brands_of_car)

    def get_job(self):
        if self.car.drive():
            pass
        else:
            self.to_repair()
            return

        self.job = Job(job_list)

    def eat(self):
        if self.home.food_amout <= 0:
            self.shopping('food')
        else:
            if self.food >= 100:
                self.food = 100

            self.food += 5
            self.home.food_amout -= 5

    def work(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                self.shopping('fuel')
                return
            else:
                self.to_repair()
                return

        self.monay += self.job.salary
        self.gladness -= self.job.gladness_less
        self.food -= 4

    def shopping(self):
        if self.car.drive():
            pass
        else:
            if self.car.fuel < 20:
                action = "fuel"
            else:
                self.to_repair()
                return
        if action == "fuel":
            print("I bought a fuel")
            self.monay -= 100
            self.car.fuel += 80
        elif action == 'food':
            print(' i bought some food')
            self.monay -=50
            self.home.food_amout += 50

    def chill(self):
        self.gladness += 10
        self.home.mess +=5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.sthrength +=100
        self.monay -= 50

    def is_alive(self):
        pass

    def days_indexes(self):
        pass

    def live(self):
        pass


brands_of_car = {}

class Auto:

    def __init__(self, brands_list):
        self.brand = random.choice = random.choice(list(brands_list))
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


class House:
    def __init__(self):
        self.mess = 0
        self.food_amount = 0


job_list = {}


class Job:
    def __init__(self, job_list):

        self.job = random.choice(list(job_list))
        self.salary = job_list[self.job]['salary']
        self.gladness_less = job_list[self.job]['gladness_less']
