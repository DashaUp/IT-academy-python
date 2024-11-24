class PowThree:
    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 3 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration



'''numbers = PowTree(3)


i = iter(numbers)'''

for i in PowThree(3):
    print(i)