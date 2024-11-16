class Cat:

    def say(self):
        print("may")

    def climb(self):
        print("I am climbing")

class Dog:
    def say(self):
        print("gaf")

    def run(self):
        print("I am running")

class Bird:
    def say(self):
        print("ku ku")

    def fly(self):
        print("I am flying")

class Mutant(Dog, Cat, Bird):
    def kungfu(self):
        print("Kijaa")

    def say(self):
        Dog.say(self)
        Cat.say(self)
        Bird.say(self)

vasia = Mutant()
vasia.fly()
vasia.say()
vasia.kungfu()
vasia.climb()
vasia.run()