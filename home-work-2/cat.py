import random
class Cat:
    def __init__(self , name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_eat(self):
        print ( 'time to eat' )
        self.progress += 0.12
        self.gladness -= 3

    def to_sleep(self):
        print ( 'time to sleep' )
        self.gladness += 3

    def to_chill(self):
        print ( 'time to chill' )
        self.gladness += 5
        self.progress -= 0.05

    def is_alive(self):
        if self.progress < - 0.5:
            print ( 'Too hungry...' )
            self.alive = False
        elif self.gladness <= 0:
            print ( 'Depression' )
            self.alive = False
        elif self.progress > 5:
            print ( 'Genius! passed!' )
            self.alive = False

    def end_of_day(self):
        print (
            f"gladness - {self.gladness}\n"
            f"progress - {round ( self.progress , 2 )}"
        )

    def live(self , day):
        print (
            f"Day#{day} of {self.name} life"
        )
        magic = random.randint ( 1 , 3 )
        if magic == 1:
            self.to_eat ()
        elif magic == 2:
            self.to_sleep ()
        elif magic == 3:
            self.to_chill ()

            self.end_of_day ()
            self.is_alive ()

    def name(self):
        pass