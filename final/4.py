
import random

rnd_number = random.randint(1, 10)

attemps = 3
while attemps > 0:
    answer = int(input('Guess number: '))
    if answer == rnd_number:
        print("you win")
        break
    else:
        attemps -= 1
        if rnd_number < answer:
            print("Менше")
        else:
            print("Більше")
else:
    print("You lose")