from auto import *
from job import *
from house import *
class Human:

    def __init__(self,
        name="human", job=None, home=None, car=None
    ):
        self.name = name
        self.job = job
        self.home = home
        self.car = car

        self.monay = 1000
        self.gladness = 50
        self.food = 50
        self.alive = True

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

    def shopping(self, action):
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
            self.home.food_amount += 50

    def chill(self):
        self.gladness += 10
        self.home.mess +=5

    def clean_home(self):
        self.gladness -= 5
        self.home.mess = 0

    def to_repair(self):
        self.car.strength += 100
        self.monay -= 50

    def is_alive(self):
        if self.food < 0:
            print('Too hungry...')
            self.alive = False
        elif self.gladness <= 0:
            print('Depression')
            self.alive = False
        elif self.monay < 5:
                print('You are homeless')
                self.alive = False
    def days_indexes(self):
        # job: [job]; car: [car]; gladness: [gladness]; food: [food]; money: [money]
        print(
            f"job: {self.job.job}; "
            f"car: {self.car.brand}; "
            f"gladness: {self.gladness}; "
            f"food: {round ( self.food , 2 )}; "
            f"money: {round ( self.monay , 2 )}"
        )

    def live(self, day):
        print(
            f"Day #{day} of {self.name} life"
        )
        if self.food < 2:
            self.shopping("food")
        elif self.gladness < 5:
            self.chill()
        elif self.monay < 100:
            self.work()
        else:
            magic = random.randint ( 1 , 2 )
            if magic == 1:
                self.chill()
            elif magic == 2:
                self.shopping("food")

        self.days_indexes ()
        self.is_alive ()