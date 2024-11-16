class Cat:
    def __init__(self):
        self.nightVision = True
        print("New cat was born")

    def say(self):
        print("may")

    def climb(self):
        print("I am climbing")

class Dog: 
    def __init__(self):
        self.strongTeeth = True
        print("New dog was born")
        
    def say(self):
        print("gaf")

    def run(self):
        print("I am running")

class Bird:
    def __init__(self):
        self.wing = 2
        print("New bird was born")
        
    def say(self):
        print("ku ku")

    def fly(self):
        print("I am flying")

class Mutant(Dog, Cat, Bird):
    def __init__(self):
        super().__init__()
        Cat.__init__(self)
        Bird.__init__(self)
    
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
print(vasia.nightVision)
print(vasia.strongTeeth)
print(vasia.wing)